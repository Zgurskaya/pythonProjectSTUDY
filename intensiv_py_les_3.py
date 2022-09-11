# Реализуйте проверку ввода на число.
# Программа должна выводить “Correct”, если введено целое или вещественное число (в качестве разделителя
# должна использоваться одна точка).
# Во всех остальных случаях должно выводиться “Wrong”.
# Для выполнения задания необходимо изучить методы строк
# Практическое задание
#   5       3.4   3.4.1   1a    a3   -123   -5.321
# Correct Correct Wrong Wrong Wrong Correct Correct


number = input('Введите число number =  ')
pt = "."
znak = "-"
if number.isdigit():
    for i in range(len(number)):
        if number[i].isdigit():
            print('correct')
elif number[0] == znak and number[1:].isdigit():
    print('correct')
elif pt in number:
    print('correct')
elif number.isdigit() and number.count('.'):
    print('correct')
else:
    print('wrong')

