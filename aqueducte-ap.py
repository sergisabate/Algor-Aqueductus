import sys
import math


# FUNCIO QUE LLEGEIX L'ARXIU PASSAT COM A PARAMETRE
def readfile():
    filename = sys.argv[1]
    variables = []
    for line in open(filename):
        variables.append([int(i) for i in line.strip().split(' ')])
    points = []
    i = 0
    while i < variables[0][0]:
        points.append(variables[i + 1])
        i += 1
    variables[0].append(points)
    return variables[0]


# FUNCIO QUE PRINTA "impossible" I SURT DEL PROGRAMA
def impossible():
    print("impossible")
    exit()


# FUNCIO QUE COMPROVA UN POSSIBLE PONT O AQUEDUCTE NO VÀLID
def wrong_cases():
    if radius > h:
        impossible()
    i = 0
    while i < n - 2:
        if midpoints[i][1] > center and math.dist(span_point, midpoints[i]) >= radius:
            impossible()
        i += 1


# FUNCIO QUE CALCULA EL COST MITJANÇANT LA FORMULA PROPOSADA
def cost():
    print(int(alpha * sum_heights + beta * (dist_x ** 2)))


# FUNCIO PRINCIPAL ITERATIVA
if __name__ == "__main__":
    n, h, alpha, beta, points = readfile()
    dist_x = points[-1][0] - points[0][0]
    radius = dist_x / 2
    center = h - radius
    span_point = [radius + points[0][0], center]
    midpoints = points[1:-1]
    sum_heights = h * 2 - (points[0][1] + points[-1][1])
    wrong_cases()
    cost()

