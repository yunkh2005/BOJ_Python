x_arr = []
y_arr = []

for _ in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

for i in range(3):
    if x_arr.count(x_arr[i]) == 1:
        x_arr.append(x_arr[i])

    if y_arr.count(y_arr[i]) == 1:
        y_arr.append(y_arr[i])

print(x_arr[3], y_arr[3])