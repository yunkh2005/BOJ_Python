num = set(range(1, 10000))
constructor = set()

for n in num:
    for i in str(n):
        n += int(i)
    constructor.add(n)

selfNumber = num - constructor
for i in sorted(selfNumber):
    print(i)