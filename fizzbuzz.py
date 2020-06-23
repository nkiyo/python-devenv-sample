import pysnooper

@pysnooper.snoop()
def fizzbuzz(i):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)

for i in range(1, 21):
    fizzbuzz(i)
