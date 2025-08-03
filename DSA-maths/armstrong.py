                                          ## Armstrong number
## is not iterable, a number 
# num = 153
# n = len(str(num))
# temp = num

# sum = 0
# while(temp > 0):
#     lastd = temp % 10
#     sum = sum + (lastd**n)
#     temp = temp // 10

# if (sum == num):  
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")




#----------------------------------------------------------------------------------------------------------
                                      ## print all divisior of a num

# num = 36

# for n in range(1, num+1):
#     if num % n == 0:
#         print(n, end=" ")

#----------------------------------------------------------------------------------------------------------

                            ## divisior of a num

# import math

# def get_divisors(num):
#     divisors = []
#     for i in range(1, int(math.isqrt(num)) + 1):
#         if num % i == 0:
#             divisors.append(i)
#             if i != num // i:  # avoid duplicates for perfect squares
#                 divisors.append(num // i)
#     return sorted(divisors)

# print(get_divisors(36))

#----------------------------------------------------------------------------------------------------------

                              ## prime numbers

#----------------------------------------------------------------------------------------------------------

# 1 to n

# n = int(input())
# for i in range(1,n+1):
#     print(i)

#----------------------------------------------------------------------------------------------------------

# def printnum(n):
#     if n == 0:
#         return 0
#     print(n, end=" ")
#     printnum(n-1)

# printnum(10)


#----------------------------------------------------------------------------------------------------------
# def reversenum(n):
#     rev = 0
#     while n > 0:
#         digit  = n % 10
#         rev = (rev * 10 ) + digit
#         n = n // 10
#     return rev 

# print(reversenum(2937))

#----------------------------------------------------------------------------------------------------------


