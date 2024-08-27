import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def rotate_x(self, theta):
        cos_theta, sin_theta = np.cos(theta), np.sin(theta)
        y, z = (
            self.y * cos_theta - self.z * sin_theta,
            self.y * sin_theta + self.z * cos_theta,
        )
        return Vec3(self.x, y, z)

    def rotate_y(self, theta):
        cos_theta, sin_theta = np.cos(theta), np.sin(theta)
        x, z = (
            self.x * cos_theta + self.z * sin_theta,
            -self.x * sin_theta + self.z * cos_theta,
        )
        return Vec3(x, self.y, z)

    def rotate_z(self, theta):
        cos_theta, sin_theta = np.cos(theta), np.sin(theta)
        x, y = (
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta,
        )
        return Vec3(x, y, self.z)

    def get_projection(self, distance, xy, offset_z):
        return (
            (distance * xy) / (self.z - offset_z)
            if self.z != offset_z
            else (distance * xy) / (0.001) + offset_z
        )


class Torus:
    def __init__(self, r, R, slices, stacks):
        self.r = r
        self.R = R
        self.slices = slices
        self.stacks = stacks
        self.vertices = []
        self.indices = self.generate_indices()
        self.generate_vertices()

    def generate_indices(self):
        indices = []
        num_vertices_per_slice = self.stacks + 1
        for i in range(self.slices):
            for j in range(self.stacks):
                p0, p1 = (
                    i * num_vertices_per_slice + j,
                    (i + 1) * num_vertices_per_slice + j,
                )
                p2, p3 = p0 + 1, p1 + 1
                indices.extend([p0, p1, p2, p2, p1, p3])
        return indices

    def generate_vertices(self):
        u = np.linspace(0, 2 * np.pi, self.slices + 1)
        v = np.linspace(0, 2 * np.pi, self.stacks + 1)
        U, V = np.meshgrid(u, v)
        U = U.flatten()
        V = V.flatten()

        cosU, sinU = np.cos(U), np.sin(U)
        cosV, sinV = np.cos(V), np.sin(V)

        x = (self.R + self.r * cosV) * cosU
        y = (self.R + self.r * cosV) * sinU
        z = self.r * sinV

        self.vertices = [Vec3(xi, yi, zi) for xi, yi, zi in zip(x, y, z)]

    def sources(self):
        return {"indices": self.indices, "vertices": self.vertices}


class Render:
    def __init__(self):
        self.WIDTH = 0.5
        self.HEIGHT = 0.5
        self.distance = 5
        self.alpha = 0.0
        self.beta = 0.0
        self.theta = 0.0
        self.torus = Torus(0.3, 0.5, 20, 15)
        self.sources = self.torus.sources()

    def draw(self, ax):
        ax.clear()
        ax.set_xlim(-self.WIDTH, self.WIDTH)
        ax.set_ylim(-self.HEIGHT, self.HEIGHT)

        vertices = self.sources["vertices"]

        for p in vertices:
            rotated_p = p.rotate_x(self.alpha).rotate_y(self.beta).rotate_z(self.theta)
            projected_x = rotated_p.get_projection(self.distance, rotated_p.x, 10)
            projected_y = rotated_p.get_projection(self.distance, rotated_p.y, 10)
            ax.plot(projected_x, projected_y, "o", color="black", markersize=2)

    def update(self):
        self.alpha += 0.05
        self.beta += 0.03
        self.theta += 0.02

    def animate(self, i):
        self.update()
        self.draw(self.ax)

    def run(self):
        fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        ani = FuncAnimation(fig, self.animate, frames=300, interval=1000 / 60)
        plt.show()


render = Render()
render.run()
