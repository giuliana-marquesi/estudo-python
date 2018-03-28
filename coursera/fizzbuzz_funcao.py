#Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
#
#'Fizz' se o número for divisível por 3 e não for divisível por 5;
#
#'Buzz' se o número for divisível por 5 e não for divisível por 3;
#
#'FizzBuzz' se o número for divisível por 3 e por 5;
#
#Caso a função não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.
#
#Note que
#
#fizzbuzz(3) deve devolver Fizz
#
#fizzbuzz(5) deve devolver Buzz
#
#fizzbuzz(15) deve devolver FizzBuzz
#
#fizzbuzz(4) deve devolver 4
#
#As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas

def fizzbuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num

def test_fizzbuzz_3():
    assert fizzbuzz(3) == 'Fizz'

def test_fizzbuzz_5():
    assert fizzbuzz(5) == 'Buzz'

def test_fizzbuzz_15():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz_4():
    assert fizzbuzz(4) == 4

def test_fizzbuzz_30():
    assert fizzbuzz(30) == 'FizzBuzz'
