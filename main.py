def FizzBuzz(input):
    if input % 3 == 0:
        print("Fizz")
    elif input % 5 == 0:
        print("Buzz")
    elif input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
    else:
        print(input)


print(FizzBuzz(3))
