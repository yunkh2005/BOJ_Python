T = int(input())
polyhedron = []

for i in range(T):
    polyhedron.append(list(map(int, input().split())))
    print(2-polyhedron[i][0]+polyhedron[i][1])