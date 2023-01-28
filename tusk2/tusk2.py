number = int(input('Ведите трёхзначное число: '))
print('Вы ввели трёхзначное число: ', number)
firstNumber = number // 100 # первое число
thirdNumber = number % 10   # третье число
secondNumber = (number % 100) // 10 # второе число
print('первое число: ', firstNumber, 
      '  второе число: ', secondNumber, 
      '  третье число: ', thirdNumber)
sum = firstNumber + secondNumber + thirdNumber
print('сумма трёх цифр трёхзначного числа', number, 'равна: ', sum)
