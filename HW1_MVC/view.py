
from user1 import user1

def main():

    print('Welcome to system')
    print('1. Register')
    print('2. Login')
    print('3. Exit')


    um = user1()

    choice = 1
    while True:
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                um.register() #
            elif choice == 2:
                um.login() #
                print('Thank you for using ATM')
                break
            else:
                raise ValueError('Invalid choice')
        except ValueError as e:
            print('Invalid choice: ' + str(str(e)))
            continue

# call to main function
if __name__ == '__main__':
    main()
