height_cm = float(input('Height converter: enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48)

year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born,  'years old, provided you live this long!')

temp_c =input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + 'degrees Fahrenheit'
print(temp_statement)

#Type casting functions

float()
int()
str()

hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))
 
print('Last month, you earned', hours * rate ,'dollars')