import random
from password import User

def main():
    
    while True:
        print('Welcome to password locker')
        print('\n')
        print('Select a short code to navigate through:to create new user use "cn":To log to your account "log" or "ex" to exit')
        short_code = input().lower()
        print('\n')
        
        if short_code == 'cn':
            print('Create username')
            created_user_name = input()
            
            print('Create password')
            created_user_password = input()
            
            print('Confirm password')
            confirm_password = input()
            
            while confirm_password != created_user_password:
                print('Invalid password')
                
                print('Enter your password:')
                
                created_user_password = input()
                
                print('Confirm your password')
                
                confirm_password = input()
            
            else:
                print('Account creation successful,{created_user_name}welcome to password locker')
                print('\n')
                print('Proceed to login')
                
                print('username')
                
                entered_username = input()
                
                print('Your password')
                
                entered_password = input()
                
            while entered_username != created_user_name  or entered_password != created_user_password :
                print('Invalid username or password')
                
                print('Username')
                
                entered_username = input()
                
                print('Your password')
                
                entered_password = input()
                
            else:
                print('Welcome{entered_username} to your account')
                print('\n')
        
        
        elif short_code == 'log':
            print('Welcome')
            
            print('Enter your username')
            default_username = input()
            
            print('Enter password')
            default_password = input()
            
            print('\n')
            
            while default_username!='testuser' or default_password != '1234':
                print('Wrong username or password. Username "testuser" and pasword "1234"')
                print('Enter user name')
                
                default_username=input()
                
                print('Enter password')
                
                default_password = input() 
                print('/n')
                
            
            
            else:
                print('Login success')
                print('\n')
                print('\n')
        
        elif short_code == 'ex':
            break
        else:
            print('Enter valid code to continue')
if __name__ == '__main__':
    main()
            