'''
#Task1
mark = int(input('Enter your exam mark: '))
print('Your grade is: ',end = '')
if mark <= 50:
    print('F')
elif 50<mark<75:
    print('C')
elif 75<=mark<90:
    print('B')
else: print('A')
'''
'''
#Task2
num = int(input('Enter a number (0<n<=10): '))
for i in range(10):
    t = i+1
    pro = num*t
    print(f'{num}x{t}={pro}')

'''
'''
#Task 3
set_password = 'p@ssW07d!'
user_input = input('Enter password: ')
attempts = 1
while set_password != user_input:
    attempts += 1
    if attempts > 3:
        print('You have reached max limit of attempts!')
        break
    user_input = input('Try again: ')

print('Password is correct!')
'''