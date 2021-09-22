# def nth_prime(n):
#     counter = 2
#     for i in range(3, n**2, 2):
#         k = 1
#         while k*k < i:
#             k += 2
#             if i % k == 0:
#                break
#         else:
#             counter += 1
#         if counter == n:
#             return i

# print(nth_prime(100001))


# counter = 2
# n = 10001
# for i in range(3, 1000000, 2):
#  k = 1
#  while k < i:
#   k += 2
#   if i % k == 0:
#    break
#   if k + 2 == i:
#    counter += 1
#   if counter == n:
#    print(i)