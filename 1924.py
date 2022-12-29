day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]     #일~토요일
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    #1월~12월
x, y = map(int, input().split())                            #x월 y일
z = 0

for i in range(x-1):
    z += month[i]
z = (z+y) % 7
print(day[z])


#https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-1924%EB%B2%88-2007%EB%85%84-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython