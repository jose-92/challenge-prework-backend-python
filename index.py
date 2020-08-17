import random


def password_generator():

    capitalize = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 
                'L', 'N', 'M', 'R', 'T', 'S' 'U', 'W', 'X', 'Y', 'Z'
    ]
    lower_case = ['a', 'b', 'd', 'e', 'f', 'g', 'i', 'j', 'k'
                'l', 'n', 'm', 'r', 't', 's', 'u', 'w', 'x', 'y', 'z'
    ]
    symbols = ['#', '[', ')', '$', '!', '/', '&', '%']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters =  capitalize + lower_case + numbers + symbols
    password = []

    for i in range(10):
        random_characters = random.choice(characters)
        password.append(random_characters)

    password = ''.join(password)

    return password


def main():
    password = password_generator();
    print('Your new password is: ' + password)


if _name_ == '_main_':
    main()