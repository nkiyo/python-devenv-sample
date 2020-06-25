def fizzbuzz(i: int) -> None:
    s: str = 123
    #s: str = ''
    if i % 3 == 0:
        s = 'Fizz'
    if i % 5 == 0:
        s = 'Buzz'
    if i % 15 == 0:
        s = 'FizzBuzz'
    if s:
        print(f'{i} {s} {type(s)}')

for i in range(1, 21):
    fizzbuzz(i)
