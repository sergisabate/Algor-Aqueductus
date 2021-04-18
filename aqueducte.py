import sys
import math


# FUNCIO QUE LLEGEIX L'ARXIU PASSAT COM A PARAMETRE --> readfile()
def readfile():
    filename = sys.argv[1]
    variables = []
    # Transforma els espais del fitxer en posicions de nombres de 2 en 2 de la llista 'variables'
    for line in open(filename):
        variables.append([int(i) for i in line.strip().split(' ')])
    # Trasllada les variables de punts a la llista 'points'
    points = []
    i = 0
    while i < variables[0][0]:
        points.append(variables[i + 1])
        i += 1
    # Prepara el return perque retorni el nombre de punts, l'alçada, cost alpha, cost beta i la llista dels punts
    variables[0].append(points)
    return variables[0]


# FUNCIÓ QUE PRINTA "impossible" I SURT DEL PROGRAMA --> impossible()
def impossible():
    print("impossible")
    exit()


# FUNCIO QUE COMPROVA UN POSSIBLE PONT O AQUEDUCTE NO VÀLID --> wrong_cases()
def wrong_cases(points_rec, radius, span_point):
    # Si un radi de l'arc fos major que l'alçada requerida, seria impossible generar un arc valid
    if radius > h:
        impossible()
    # Si un punt per sobre del centre de l'arc estigues fora del seu radi,
    # voldra dir que el pont xocaria contra el terreny considerant-ho no valid.
    i = 0
    while i < 2:
        if points_rec[i][1] > span_point[1] and math.dist(span_point, points_rec[i]) >= radius:
            impossible()
        i += 1


# FUNCIO QUE CALCULA EL COST MITJANÇANT LA FORMULA PROPOSADA --> cost()
def cost(height, x):
    return alpha * height + beta * x


# FUNCIO PRINCIPAL QUE COMPROVA TOT L'ANTERIOR DE FORMA RECURSIVA FINS QUE ARRIBA A L'ULTIM PUNT --> recursive()
def recursive(points_rec, sum_costs):
    # Es calcula la distancia en l'eix X entre els dos punts
    dist_x = points_rec[1][0] - points_rec[0][0]
    # Es calcula el radi sent aquest la meitat de la distancia X.
    radius = dist_x / 2
    # Es calcula el centre de l'arc:
    # - La X sera la meitat de la distancia X dels dos punts, es a dir, radi més l'X del primer punt.
    # - La Y sera l'alçada requerida menys el radi.
    span_point = [radius + points_rec[0][0], h - radius]
    # Es comprova que sigui valid.
    wrong_cases(points_rec, radius, span_point)
    # Quan nomes quedin dos punts es sumara al total els dos pilars + la seva distancia al quadrat.
    if len(points_rec) == 2:
        return cost(sum_costs[0] + h * 2 - (points_rec[1][1] + points_rec[0][1]), sum_costs[1] + dist_x ** 2)
    # En cada "iteracio" recursiva, es suma l'alçada del primer pilar i la distancia amb el seguent.
    total_cost = [sum_costs[0] + h - points_rec[0][1], sum_costs[1] + dist_x ** 2]
    # En cada "iteracio" recursiva, es pasa la llista sense el punt ja tractat i el cost acumulat.
    return recursive(points_rec[1:], total_cost)


n, h, alpha, beta, points = readfile()
sys.setrecursionlimit(len(points) + 100)
print(recursive(points, [0, 0]))
