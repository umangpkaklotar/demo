# import random
# jackpot = random.randint(1, 20)
# user_num= int(input("Enter a number between 1 and 20: "))
# c= 1 # c use for counting the number of attempts
# while jackpot != user_num :
    
#     if user_num<jackpot:
#         print("choose the higher !!")
#     else:
#         print("choose the lower !!")
#     user_num = int(input("Enter a number between 1 and 20: "))
#     c+= 1
# else:
#     print("you won the game and your jackpot number is ", user_num)
#     print("you took ", c)

print("=====================1th question=============================")
#this is output [7,9,11,13,15]
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
result = list(map(lambda x, y: x + y, l1, l2)) # map applies the lambda function to corresponding elements of l1 and l2
print(result)


print("=====================2th question=============================")

# which one starts with p
l=["php","python","java","c++"]
result = list(filter(lambda x: x.startswith("p"), l))
print(result)

print("=====================3th question=============================")

# 1 square of every number
l = [1,2,3,4,5,6,7,8,9,10]
# this is using list comprehension
result1 = [i**2 for i in l]
print(result1)
# this is same as above but using map function
result2 = list(map(lambda x: x**2, l))
print(result2)


# 2 even numbers
result3 = list(filter(lambda x: x%2==0, l))
print(result3)

# 3 odd numbers
result4 = list(filter(lambda x: x%2!=0, l))
print(result4)

# 4 sum of all numberssss
a=[1,2,3,4,5,6,7,8,9,10]
result6 = sum(a)
from functools import reduce
# use another way to find sum of all numbers
result7 = reduce(lambda x, y: x + y, a)
print(result6)
print(result7)