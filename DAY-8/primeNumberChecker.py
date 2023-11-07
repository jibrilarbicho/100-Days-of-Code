def prime_number_checker(number):
    for i in range(2,number-1):
     if number%i==0:
        print(f"{number} is prime  Number")
        break
     else:
         print(f"{number} is not prime")
         break
num=int(input("Enter  the number you want to check wether prime or not"))
prime_number_checker(num)