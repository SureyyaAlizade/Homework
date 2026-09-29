name = input('Enter your name: ')
age = input('Enter your age: ')
fav_num = input('Enter your favourite number: ')
age = int(age)
fav_num = int(fav_num)

new_age = age+10
new_num = fav_num**2

if fav_num%2 == 0:
    type_ = 'even' 
else: type_ = 'odd'

print(f'Hi {name}! In 10 years you will be {new_age}. Your favourite number squared is {new_num}, and it is {type_}.')
