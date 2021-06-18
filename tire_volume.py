import math
from datetime import datetime
current_date = datetime.now()
print('Welcome to the tire volume calculator!')
print('')
yes_no = input('Would you like to use the claculator? ').lower()


if yes_no == 'yes' : 
    print('Please enter the following... ')
    print('')
    width = float(input('Enter the width of the tire in mm (ex 205): '))
    aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
    diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))
    v = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000
    v_dec = ('{:.1f}'.format(v))
    print(f"The approxiamte volume is {v_dec} milliliters ")
    print('')
    with open('volume.txt' , 'at') as text_file:
       print(f'{current_date} \t{width} \t{aspect_ratio} \t{diameter} \t{v_dec}' , file=text_file)
elif yes_no == 'no' :
    print('Thank you!')

name = input('Would you like to be on list to buy new tires \nwith the measurments you entered? ').lower()
if name == 'yes' :
    print('Please enter the following...')
    print('')
    f_name = input('First Name: ').capitalize()
    l_name = input('Last Name: ').capitalize()
    number = input('Phone Number: ')
    with open('volume.txt' , 'at') as text_file:
        print(f'{l_name}, {f_name}:\t{number}' , file=text_file)
    print('')
    print('Thank you, you have been added to the list.')
else: 
    print('Thank you')
