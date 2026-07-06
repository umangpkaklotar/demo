import random
jackpot = random.randint(1, 20)
user_num= int(input("Enter a number between 1 and 20: "))
c= 1 # c use for counting the number of attempts
while jackpot != user_num :
    
    if user_num<jackpot:
        print("choose the higher !!")
    else:
        print("choose the lower !!")
    user_num = int(input("Enter a number between 1 and 20: "))
    c+= 1
else:
    print("you won the game and your jackpot number is ", user_num)
    print("you took ", c)