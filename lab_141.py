#list all prime numbers between 1 and 250


i = 2      #initializes the variable i to 2, the starting point for finding prime numbers.

while i <= 250:   #outer while loop: Continues as long as i is less than or equal to 250, which is the range of numbers we need to check for primality.
    j = 2
    while j < 250:   #Inner while loop: For each value of i, initializes j to 2 and iterates while j is less than 250.
        if i%j == 0:   #if i is divisible by j, ir means it is not prime number.  i % j == 0 checks if the remainder of dividing i by j is equal to zero
            break       #it breaks out of the inner loop using the break
        j += 1         #incrementing the value of the variable j by 1. It is equivalent to writing j = j + 1
    if i == j:        #aftter inner loop if checks if i equals to j. If it is then it is a prime number meaning it can only be divided by 1 and itself
        print(i,end=',')   #it prints the numbers separated by comma. to avoid going to a new line.
    i += 1    # then it increments and repeats the process  for the next value.  

    # It used whiile loops and conditional statesmens as follows
    