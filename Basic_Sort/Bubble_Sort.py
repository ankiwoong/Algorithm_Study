'''
버블 정렬?
두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 잇는 데이터보다 크면, 자리를 바구는 정렬 알고리즘

데이터길이      조건체크      턴
2               1             1
3               2             2
4               3             3

for index in range(데이터 길이 - 1):
    for index2 in range(데이터길이 - 1):
        if 앞데이터 > 뒤데이터:
            swap(앞데이터, 뒤데이터)
'''
# import random


def bubbiesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True

        if swap == False:
            break

    return data


data_list = [17, 6, 8, 11, 2, 3]

print(bubbiesort(data_list))

# data_list = random.sample(range(100), 50)

# print(bubbiesort(data_list))
