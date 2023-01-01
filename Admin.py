import re


class Admin:
    admins = dict()
    all_buses = dict()

    def __init__(self):
        self.buses = dict()

    def Sign_up(self):
        self.name = input()
        self.state = input()
        self.city = input()
        self.telephone = int(input())
        self.Email = input()
        self.username = input("Enter a username...")
        self.password = input("Enter a password...")
        UserCon = re.match('^\w+$', self.username) and len(self.username) >= 4
        PassCon = re.match('^.*(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$', self.password) and len(self.password) >= 8
        if UserCon and PassCon and Admin.admins[self.username] == None:
            Admin.admins[self.username] = {'password': self.password, 'name': self.name,
                                        'state': self.state, 'city': self.city,
                                        'telephone': self.telephone, 'Email': self.Email}
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
        if Admin.admins[getattr(self, inputed_username)]['password'] == inputed_password:
            print(f'Welcome {self.name}')
            return
        else:
            print('User not found!')
            self.Log_in()

    def New_Bus(self):
        self.road = str(self.pstate+'-'+self.dstate)
        self.dict_port = {'state': self.pstate, 'terminal': self.pterminal, 'date': self.pdate, 'time': self.ptime}
        self.dict_dest = {'state': self.dstate, 'terminal': self.dterminal}
        self.dict_bus = {'type': self.btype, 'capacity': self.bcapacity, 'time': self.btime, 'price': self.bprice}
        self.dict_driver = {'name': self.dname, 'id': self.did, 'phone': self.dphone}
        self.buses[self.road] = [{'port': self.dict_port}, {'destination': self.dict_dest},
                                 {'bus': self.dict_bus}, {'driver': self.dict_driver}]
        Admin.all_buses[self] = self.buses
