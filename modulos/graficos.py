# coding: utf-8

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def grafico_geracoes(gen):
    '''
        Plota um gráfico 3D exibindo a otimização dos indivúduos ao longo
        das gerações.

    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Gradiente de cores
    tr = ['#ff0000', '#ff1000', '#ff2000', '#ff3000', '#ff4000', '#ff5000', '#ff6000', '#ff7000', '#ff8000', '#ff9000']
    ty = ['#ffa000', '#ffb000', '#ffc000', '#ffd000', '#ffe000', '#fff000', '#ffff00', '#f0ff00', '#e0ff00', '#d0ff00']
    tg = ['#c0ff00', '#b0ff00', '#a0ff00', '#90ff00', '#80ff00', '#70ff00', '#60ff00', '#50ff00', '#40ff00', '#10ff00']
    
    total_c = len(tr) + len(ty) + len(tg)
    
    # Quantidade de gerações
    num_gen = len(gen)
    
    # Define as cores de cada geração
    if num_gen == 3:
        gradient = ['#ff0000', '#ffe000', '#10ff00']
    else:
        pos = 0
        l = [tr, ty, tg]
        while num_gen != total_c:
            if num_gen > total_c:
                l[pos].append(l[pos][-1])
                total_c += 1
            else:
                del l[pos][len(l[pos]) / 2]
                total_c -= 1
            pos += 1
            if pos == 3:
                pos = 0

        gradient = tr + ty + tg

    # Constrói o gráfico
    for c, z in zip(gradient, range(1, num_gen +1)):
        xs = np.arange(len(gen[0]))
        ys = gen[z - 1]
        
        # Ordena em ordem decrescete de otimização
        ys.sort()
        ys = ys[::-1]

        cs = [c] * len(xs)
        ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)

    # Labels dos eixos
    ax.set_xlabel(u'X - População')
    ax.set_ylabel(u'Y - Geração')
    ax.set_zlabel(u'Z - Custo do percurso')

    plt.show()


def test():
    GEN = [
        [100, 99, 99, 96, 90, 89, 89, 89, 87, 80],
        [100, 99, 99, 96, 80, 72, 71, 50, 50, 49],
        [80, 72, 72, 70, 51, 49, 41, 40, 40, 39],
        [110, 99, 70, 60, 55, 54, 53, 39, 38, 31],
        [94, 90, 83, 79, 55, 54, 53, 39, 20, 11],
        [110, 99, 70, 60, 55, 32, 31, 25, 11, 10]
    ]

    grafico_geracoes(GEN)


if __name__ == '__main__':
    test()

