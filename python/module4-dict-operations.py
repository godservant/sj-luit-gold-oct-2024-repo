grades = {}

grades['John'] = 'A-'

grades['Anne'] = 'B'

print(grades)

grades.update({'John': 'A'})

if 'John' in grades:
    print('John got:', grades['John'])
    
    
del grades ['John']
print(grades)

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

for el in grades:
    print(el)
    
    sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
 
while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!')
 
print('Bye!')

