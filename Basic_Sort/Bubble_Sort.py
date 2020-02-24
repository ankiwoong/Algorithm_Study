'''
버블 정렬?
두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 잇는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

데이터길이      조건체크      턴
2               1             1
3               2             2
4               3             3

for index in range(데이터 길이 - 1):            # 턴
    for index2 in range(데이터 길이 - 1):       # 조건 체크
        if 앞 데이터 > 뒤 데이터:               # 조건 비교 후 변경 
            데이터 교체(앞 데이터, 뒤 데이터)   # 앞 데이터와 뒤 데이터 변경


for index in range(데이터 길이 - 1):            # 턴
    swap = False                                # 데이터를 바꿀시 변경 될 변수
    for index2 in range(데이터 길이 - 1):       # 조건 체크
        if 앞 데이터 > 뒤 데이터:               # 조건 비교 후 변경
            데이터 교체(앞 데이터, 뒤 데이터)   # 앞 데이터와 뒤 데이터 변경
            swap = True                         # 데이터 변경 후 swap 변수를 True로 변경

    if swap == Fasle:                           # swap가 Fasle일 경우 종료(데이터 변경 할것이 없다)
        break
'''
import random


def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break

    return data


'''
Case 1 - Random 사용하여 케이스 생성
'''
data_list = random.sample(range(100), 50)
print(bubblesort(data_list))

'''
Case 2 - 지정된 데이터를 사용하여 케이스 생성
'''
# data_list = [17, 6, 8, 11, 2, 3]
# print(bubblesort(data_list))
