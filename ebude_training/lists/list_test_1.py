rabbit=int(input('Enter a number to replace another number:'))
numbers=[1,2,3,4,5]
numbers[2]=rabbit
numbers.append(3)
numbers.insert(2,99)
print(numbers)