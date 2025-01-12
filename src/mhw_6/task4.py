"""Странные рекурсивные отношения.
Функция f определена для всех
натуральных аргументов следующим образом:

f(1)=1
f(3)=3
f(2n)=f(n)
f(4n+1)=2f(2n+1)−f(n)
f(4n+3)=3f(2n+1)−2f(n)
Функция S(n) определена как ∑ni=1f(i).

S(8)=22 и S(100)=3604.

Найдите S(337)
. В качестве ответа приведите последние 9 цифр полученного числа.
"""
# import time

# Буду благодарен если скажете почему оно не работает
# def strange_recursion(num, answer=0):
#     # if answer:
#     #     return answer
#     if num == 0:
#         return int(str(answer)[-9:])
#     if num == 1:
#         answer += 1
#         print(num, 1)
#         return strange_recursion(num - 1, answer)
#     if num == 3:
#         answer += 3
#         print(num, 3)
#         return strange_recursion(num - 1, answer)
#     if num % 2 == 0:
#         temp = num
#         while not temp % 2:
#             temp /= 2
#         answer += int(temp)
#         print(num, int(temp))
#         return strange_recursion(num - 1, answer)
#     if (num - 1) % 4 == 0:
#         temp = num // 4
#         while not temp % 2:
#             temp /= 2
#         answer += 2 * (2 * (num // 4) + 1) - temp
#         print(num, 2 * (2 * (num // 4) + 1) - temp)
#         return strange_recursion(num - 1, int(answer))
#     if (num - 3) % 4 == 0:
#         temp = num // 4
#         while not temp % 2:
#             temp /= 2
#         answer += 3 * (2 * (num // 4) + 1) - 2 * temp
#         print(num, 3 * (2 * (num // 4) + 1) - 2 * temp)
#         return strange_recursion(num - 1, int(answer))


# This one works, but it will take 500 - 1000 years to compute
# (at least on my PC) :(.
def optimized_recursion(num):
    answer = 0
    for i in range(1, num + 1):
        reversed_i = 0
        temp = i
        while temp > 0:
            reversed_i = (reversed_i << 1) | (temp & 1)  # Efficient bit reversal
            temp >>= 1
        answer += reversed_i
        # if not i % 1000000:
        #     print((time.time()-start)/(i / 3**37 * 100)/3600/24/365.2422)
    return answer


# start = time.time()
print(str(optimized_recursion(3**37))[-9::])
