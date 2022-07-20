#total_even = 0
#for number in range(2 , 101 ,2):
   # total_even += number
   #print (f'The total of all even numbers between 1 and 100 is \n {total_even}')

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
       print ("Fizzbuzz")
    elif number % 5 == 0:
       print ('Buzz')
    elif number % 3 == 0:
         print ('Fizz')
    else:
        print (number)