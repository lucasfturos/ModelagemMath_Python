from matplotlib import pyplot as plt
import math as m


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.title("Projeção do Movimento de uma Bola")


def frange(inicio, final, intervalo):
    numbers = []
    while inicio < final:
        numbers.append(inicio)
        inicio = inicio + intervalo
    return numbers


def draw_trajectory(u, theta):
    theta = m.radians(theta)
    g = 9.8
    # Tempo no ar
    t_ar = 2 * u * m.sin(theta) / g
    # Encontra o intervalo de tempo
    intervalos = frange(0, t_ar, 0.001)
    # Lista das coordenadas x e y
    x = []
    y = []
    for t in intervalos:
        x.append(u * m.cos(theta) * t)
        y.append(u * m.sin(theta) * t - 0.5 * g * t * t)
    draw_graph(x, y)


if __name__ == "__main__":
    try:
        u_list = [20, 40, 60]
        theta = 45
    except ValueError:
        print("Você informou um valor inválido")
    else:
        for u in u_list:
            draw_trajectory(u, theta)
        plt.legend(["20", "40", "60"])
        plt.show()
