def fizzbuzz(i: int) -> None:
    #s: str = 123 # mypy error
    s: str = '' # mypy success
    if i % 3 == 0:
        s = 'Fizz'
    if i % 5 == 0:
        s = 'Buzz'
    if i % 15 == 0:
        s = 'FizzBuzz'
    if s:
        print(f'{i} {s} {type(s)}')

#import wdb; wdb.set_trace() # for wdb
import web_pdb; web_pdb.set_trace()  # for python-web-pdb
for i in range(1, 21):
    fizzbuzz(i)

