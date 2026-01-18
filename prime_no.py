# # # num = 15
# # # flag = 0
# # # for i in range(2,num):
# # #     if num % i ==0:
# # #         flag=1
# # #         break
# # #     if flag == 1:
# # #         print("Not Prime")
# # #     else:
# # #         print("prime")

# # num = 15
# # flag = 0
# # if num < 2:
# #     flag=1
# # else:
# #     for i in range(2,num):
# #         if num%i==0:
# #             flag = 1
# #             break

# # if flag == 1:
# #      print("Not Prime")
# # else:
# #     print("Prime")

# num=15
# flag=0
# if num<2:
#     flag=1
# else:
#     for i in range(2,num):
#         if num%i==0:
#             flag=1
#             break

# if flag == 1:
#     print("Not Prime")
# else:
#     print("Prime")

# num=15
# flag=0
# if num<2:
#     flag=1
# else:
#     for i in range(2,int((num/2)+1)):
#         if num%i==0:
#             flag=1
#             break
# if flag==1:
#     print("Not Prime")
# else:
#     print("Prime")

num=15
def checkPrime(num,iter=2):
    if num == iter:
        return True
    if num%iter==0:
        return False
    if num<2:
     return False
    return checkPrime(num,iter+1)
if checkPrime(num) == True:
   print("Prime")
else:
   print("Not Prime")