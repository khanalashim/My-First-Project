#making conditonal expression

# if this then (that)
# else
# this
import os
import random

a = random.randrange(1000,10000)
print("Instructions:")
print("1. You must type four digits to play this game")
print("2. you will be notified if you guessed any of the digits right")
print("3. But it will not notify if two or more digits are right at the same time")

print("4. For example; if i type 1234 and it tells me _*2*_*_ then 1 is not correct but 2 is correct but other two might be correct or might not be correct.")
print(" we will not be sure. To find out, we will have to guess it again but this time we must not type 2 or else it will not show if other two are correct")
print(" or not. so for that we will type 1745 then we can say 1 is incorrect,7 is incorect, and if 4 is correct it will notify itself.") 
print("5. But you must remember the correct guessess or it will dissappear in a blink.")
print("_*_*_*_")
con = True

life = 10

def failed_game():
 print("You Lose.......")
 



while con:
 print("\n\n\n\n\tRemaining Life = ", life)
 if life==0:
  con = False
  failed_game()
  
 life = life - 1
 ask = int(input(" Guess the four digit number "))
 i = ask%1000
 i_digit = int((ask - i)/1000)

 ii = i%100
 ii_digit = int((i - ii)/100)

 iii = ii%10
 iii_digit = int((ii- iii)/10)

 iv = iii%1
 iv_digit = int((iii - iv)/1)




 first = a%1000
 first_digit = int((a - first)/1000)
 
 second = first%100
 second_digit = int((first - second)/100)

 third = second%10
 third_digit = int((second - third)/10)

 fourth = third%1
 fourth_digit = int((third - fourth)/1)
 
 if i_digit==first_digit and ii_digit==second_digit and iii_digit==third_digit and iv_digit==fourth_digit:
      os.system('cls')
      print(i_digit,ii_digit,iii_digit,iv_digit)
      print("You have guessed my number")
 elif i_digit==first_digit:
      os.system('cls')
      print(i_digit, " _*_*_")
      print("only one digits guessed")
 elif ii_digit==second_digit:
      os.system('cls')
      print("_*", ii_digit, "_*_")
      print("only one digits guessed")
 elif iii_digit==third_digit:
      os.system('cls')
      print("_*_*", iii_digit, "_")
      print("only one digits guessed")
 elif iv_digit==fourth_digit:
      os.system('cls')
      print("_*_*_", iv_digit)
      print("only one digits guessed")
 else:
  os.system('cls')


 


  






# print(first_digit)
# print(second_digit)
# print(third_digit)
# print(fourth_digit)



