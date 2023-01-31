#1- тапсырма
# n = int(input("n = "))
# i = 1
# while i ** 2 <= n:
#     print(i ** 2)
#     i += 1
#2 - тапсырма
# res = 1
# n = int(input("n = "))
# for i in range(1, n + 1):
#     res *= i
# print(res)
#3 - тапсырма (1)
# langs = ["Python", "Java", "JS", "Kotlin"]
# enumNames = enumerate(langs, 1)
# print(list(enumNames))
#(2)
# import random
#
# massive=[]
#
# n=int(input())
#
# for i in range(1, n+1):massive.append(random.randint(1,10))
#
# print(massive)
#4 - тапсырма (1)
# a = int(input("A = "))
# b = int(input("B = "))
#
# for i in range(a, b + 1):
#     print(i)
# (2)
# a = int(input("A = "))
# b = int(input("B = "))
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)
# (3)
# a = int(input("A = "))
# b = int(input("B = "))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')

#(4)
# n = int(input("N = "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# for i in range(n - 1):
#     sum -= int(input())
# print("x = ", sum)
