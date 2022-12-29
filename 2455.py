people = []
result = 0

for i in range(4):
    OUT, IN = map(int, input().split())
    result += IN - OUT
    people.append(result)
    
print(max(people))