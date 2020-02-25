'''
Case 1 n! 팩토리얼 구하기
n! = 1 x 2 x ... x n
n의 값에 상관없이 변수 n, 변수 fac, 변수 index 만 필요함
공간 복잡도는 O(1)

n번 호출
n개의 변수 생성
'''

# Case 1


def factorial_one(n):
    fac = 1
    for index in range(2, n + 1):
        fac = fac * index
    return fac


print(factorial_one(3))

# Case 2(재귀호출)


def factorial_two(n):
    if n > 1:
        return n * factorial_two(n - 1)
    else:
        return 1


print(factorial_two(3))
