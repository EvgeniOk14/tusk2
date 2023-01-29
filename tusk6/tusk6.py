number = int(input('Ведите шестизначное число number: '))
print('Вы ввели шестизначное число number равное: ', number)
leftHalfNumber = int(number // 1000) # первое трёхзначное число
leftNumber1 = leftHalfNumber // 100          # первое число, первого трёхзначного числа
leftNumber3 = leftHalfNumber % 10            # третье число, первого трёхзначного числа
leftNumber2 = (leftHalfNumber % 100) // 10  # второе число, первого трёхзначного числа
print('первое число: ', leftNumber1) 
print('второе число: ', leftNumber2) 
print('третье число: ', leftNumber3)
sum1 = leftNumber1 + leftNumber2 + leftNumber3
print('сумма первых трёх цифр левой половины шестизначного числа', number, 'равна: ', sum1)

rightHalfNumber = int(number % 1000) # второе трёхзначное число
rightNumber1 = rightHalfNumber // 100          # первое число, второго трёхзначного числа
rightNumber3 = rightHalfNumber % 10            # третье число, второго трёхзначного числа
rightNumber2 = (rightHalfNumber % 100) // 10  # второе число, второого трёхзначного числа
print('первое число: ', rightNumber1) 
print('второе число: ', rightNumber2) 
print('третье число: ', rightNumber3)
sum2 = rightNumber1 + rightNumber2 + rightNumber3
print('сумма первых трёх цифр правой половины шестизначного числа', number, 'равна: ', sum2)
if (sum1 == sum2):
    print('Да, данный билет является счастливым, суммы справа и слева совпадают! ')
else:
    print('нет, данный билет обычный и суммы слева и справа не совпадают')
    

