nums = []


for i in range(3):
    nums.append(list(map(str, input().split())))
    nums[i] = ''.join(nums[i])

for i in range(3):
    zero, one = 0, 0
    for j in range(4):  
        if nums[i][j] == '0':
            zero += 1
        else:
            one += 1 
    
    if one == 4:
        print("E")
    elif zero == 4:
        print("D")
    elif zero == 3 and one == 1:
        print("C")
    elif zero == 2 and one == 2:
        print("B")
    else:
        print("A")