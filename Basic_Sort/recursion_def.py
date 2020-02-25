'''
재귀함수
1. 함수 안에서 동일한 함수를 호출
2. 여러 알고리즘 작성시 사용

2! = 1 x 2
3! = 1 x 2 x 3
4! = 1 x 2 x 3 x 4

n! = n x (n-())!

일반적 형태 1>
def function(입력):
    if 입력 > 일정값:
        return function(입력 - 1)
    else:
        return 일정값, 입력값 또는 특정값

일반적 형태 2>
def function(입력):
    if 입력 <= 일정값:
        return 일정값 또는 입력값
    funtion(입력 보다 작은값)
    return 결과값

깊이가 1000회 이하가 되어야 함
'''

# Case 1


import random


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


for num in range(10):
    print(factorial(num))

print(factorial(5))


# Case 2
def multiple_one(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value


def multiple_two(num):
    if num <= 1:
        return num
    return num * multiple_two(num - 1)


print(multiple_one(10))
print(multiple_two(10))

# Case 3
# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수(재귀함수)


def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


data = random.sample(range(100), 10)

print(sum_list(data))

# Case4
# 회문(Palindrome) : 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 생성
# ex> level


def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


print(palindrome('Dave'))           # 회문 X
print(palindrome('level'))          # 회문 O
