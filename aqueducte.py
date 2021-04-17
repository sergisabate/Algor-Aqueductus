import sys
import math


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


def impossible():
    print("impossible")
    exit()


def wrong_cases(points_rec, radius, span_point):
    if radius > h:
        impossible()
    i = 0
    while i < 2:
        if points_rec[i][1] > span_point[1] and math.dist(span_point, points_rec[i]) >= radius:
            impossible()
        i += 1


def cost(height, x):
    return alpha * height + beta * x


def recursive(points_rec, sum_costs):
    dist_x = points_rec[1][0] - points_rec[0][0]
    radius = dist_x / 2
    center = h - radius
    span_point = [radius + points_rec[0][0], center]
    wrong_cases(points_rec, radius, span_point)
    if len(points_rec) == 2:
        return cost(sum_costs[0] + h * 2 - (points_rec[1][1] + points_rec[0][1]), sum_costs[1] + dist_x ** 2)
    total_cost = [sum_costs[0] + h - points_rec[0][1], sum_costs[1] + dist_x ** 2]
    return recursive(points_rec[1:], total_cost)


n, h, alpha, beta, points = readfile()
print(recursive(points, [0, 0]))
