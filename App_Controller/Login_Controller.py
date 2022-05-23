import csv

from App_Model.user import User


class Login_Controller():
    def __init__(self):
        self.open_file('files/users.csv')

    def open_file(self,file):
        self.users = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            self.line_count = 0
            for row in csv_reader:
                role = ''
                if row[3] is 1:
                    role = 'Admin'
                else:
                    role = 'User'
                user = User(row[0],row[1],row[2],role)
                self.users.append(user)
                self.line_count += 1

    def getUser(self,email,password):
        for user in self.users:
            if(user.isUser(email, password) is True):
                return user
        return None


if __name__ == "__main__":
    LC = Login_Controller()
    LC.open_file()
