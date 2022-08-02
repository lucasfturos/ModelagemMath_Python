from matplotlib import markers
import matplotlib.pyplot as plt

# Constroi o gráfico
def draw_graph(x, y):
    plt.plot(x, y, marker="o")
    plt.xlabel("Distancia em metros")
    plt.ylabel("Força Gravitacional em Newtons")
    plt.title("Gravitação força e distância")
    plt.show()


def generate_F_r():
    # Gera os valores para r = distancia
    r = range(100, 1001, 50)
    F = []
    # Contante gravitacional
    G = 6.674 * (10**-11)
    # Duas massas em kg
    m1 = 0.5
    m2 = 1.5
    # Calculo força and adiciona para a lista F
    for dist in r:
        force = G * (m1 * m2) / (dist**2)
        F.append(force)
    draw_graph(r, F)


if __name__ == "__main__":
    generate_F_r()
