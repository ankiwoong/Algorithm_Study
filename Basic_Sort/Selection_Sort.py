'''
선택 정렬?
다음과 같은 순서를 반복하며 정렬하는 알고리즘
1. 주어진 데이터 중, 최소값을 찾음
2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

0   1   2   3   인덱스번호
--------------
5   4   3   1   초기값
1   4   3   5
1   3   4   5
1   3   4   5   정렬값

for stand in range(len(data) - 1):    # stand = 기준점
    lowest = stand                      # 맨 처음 최소값이 들어갈 변수명
    for index in range(stand + 1, len(data)):
        if data[lowest] > data[index]:    # 최소값
            lowest = index
    swap(lowest, index)
'''
import random


def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


'''
Case 1 - Random 사용하여 케이스 생성
'''
data_list = random.sample(range(100), 10)
print(selection_sort(data_list))
'''
Case 2 - 지정된 데이터를 사용하여 케이스 생성
'''
# data_list = [17, 6, 8, 11, 2, 3]
# print(selection_sort(data_list))
