#from Admin import *
import re

class Client:
    clients = dict()

    def Sign_up(self):
        self.firstname = input()
        self.lastname = input()
        self.phone = int(input())
        self.Email = input()
        self.id = input()
        self.username = input("Enter a username...")
        self.password = input("Enter a password...")
        UserCon = re.match('^\w+$', self.username) and len(self.username) >= 4
        PassCon = re.match('^.*(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', self.password) and len(self.password) >= 8
        if UserCon and PassCon and Client.clients[self.username] == None:
            Client.clients[self.username] = {'password': self.password, 'first name': self.firstname,
                                        'last name': self.lastname, 'phone': self.phone,
                                        'Email': self.Email, 'id': self.id}
            return
        else:
            UserWarn = 'A valid username is at least 4 character long and contains only letters, numbers or _'
            PassWarn = 'A valid password is at least 8 character long and contains at least one uppercase, lowercase, number and @#$%^&+='
            if not UserCon and not PassCon:
                print(UserWarn)
                print(PassWarn)
                print('Please enter a valid username and password')
            elif not UserCon:
                print(UserWarn)
                print('Please enter a valid username')
            elif not PassCon:
                print(PassWarn)
                print('Please enter a valid password')
            else:
                print('this username exists...')
            self.Sign_up()

    def Log_in(self):
        inputed_username = input()
        inputed_password = input()
        if Client.clients[getattr(self, inputed_username)]['password'] == inputed_password:
            print(f'Welcome {self.firstname} {self.lastname}')
            return
        else:
            print('User not found!')
            self.Log_in()

    def Recovery_code(self):
        pass