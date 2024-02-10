for i in range(1,61):
    if i%3==0:
        if i%3==0 and i%5==0:
            print("FizzBuzz\n")
        else:
            print("Fizz\n")
        
    elif i%5==0:
        if i%3==0 and i%5==0:
                print("FizzBuzz\n")
        else:
            print("Buzz\n")

    else:
        print(i,"\n")