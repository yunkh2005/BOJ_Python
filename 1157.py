words = input().upper()    # list의 모든 값을 대문자로 입력받음
unique_words = list(set(words))  # 중복값이 제거된 list

cnt_list = []      # count된 숫자를 넣는 리스트
for x in unique_words :
    cnt = words.count(x)  # count된 숫자를 세는 변수
    print(cnt)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])