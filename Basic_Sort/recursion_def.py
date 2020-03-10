'''
재귀 호출
1. 함수 안에서 동일한 함수를 호출
2. 여러 알고리즘 작성시 사용

2! = 1 x 2
3! = 1 x 2 x 3
4! = 1 x 2 x 3 x 4
규칙 : n! = n x (n-())!

일반적인 형태 1>
def function(입력):
    if 입력 > 일정값:                            # 입력이 일정 값 이상이면
        return function(입력 - 1)                # 입력보다 작은 값
    else:
        return 일정값, 입력값, 또는 특정값       # 재귀 호출 종료

일반적인 형태 2>
def function(입력):
    if 입력 <= 일정값:                           # 입력이 일정 값보다 작으면
        return 일정값, 입력값, 또는 특정값       # 재귀 호출 종료
    function(입력보다 작은 값)
    return 결과값

함수는 내부적으로 스택처럼 관리
깊이가 1000회 이하가 되어야 함
'''
import random

# Case 1


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


for num in range(10):
    print(factorial(num))

# print(factorial(5))


# Case 2
# 재귀 함수를 활용해서 완성해서 1부터 num까지의 곱이 출력
def multiple_one(num):
    return_value = 1
    for index in range(1, num + 1):
        return_value = return_value * index
    return return_value


def multiple_two(num):
    if num <= 1:
        return num
    return num * multiple_two(num - 1)


for num in range(10):
    print(multiple_one(num))

for num in range(10):
    print(multiple_two(num))

# print(multiple_one(10))
# print(multiple_two(10))

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

# Case5
# 1. n이 홀수 이면 n x 1
# 2. n이 짝수 이면 n / 2
# 3. 1이 될때까지 반복


def func(n):
    print(n)
    if n == 1:
        return n

    if n % 2 == 1:
        return (func((3 * n) + 1))
    else:
        return (func(int(n / 2)))


print(func(3))

# Case6
# 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지 있음
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2
# 1 + 3
# 3 + 1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수는?


def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4

    return func(data - 1) + func(data - 2) + func(data - 3)


print(func(5))
