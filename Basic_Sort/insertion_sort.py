'''
삽입정렬?
1. 삽입 정렬은 두 번째 인덱스부터 시작
2. 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 key 값이 더 작으면, B 값을 뒤 인덱스로 복사
3. 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

0   1   2   3   인덱스번호
--------------
5   3   2   4   초기값
2   3   5   4
2   3   4   5
2   3   4   5   정렬값

데이터길이      조건체크      턴
2               1             1
3               2             2
4               3             3

for index in range(데이터 길이 - 1):                   # 턴(index = 턴의 횟수)
    for index2 in range(index + 1, 0, -1):             # 인덱스부터 시작하여 0까지 -1씩 옮겨감
        if data[index2] < data[index2 -1]:
            swap(data[index2], data[index2 - 1])
        else:
            break
'''
import random


def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data


data_list = random.sample(range(100), 50)
print(insertion_sort(data_list))
