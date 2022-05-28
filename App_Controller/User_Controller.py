import csv

from App_Model.user import User


class User_Controller():
    def __init__(self):
        self.file = 'files/users.csv'
        self.open_file()

    def open_file(self):
        self.users = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            self.line_count = 0
            for row in csv_reader:
                role = ''
                print("rolw:"+row[3])
                if row[3] is 1:
                    role = 'Admin'
                else:
                    role = 'User'
                user = User(row[0],row[1],row[2],role)
                self.users.append(user)
                self.line_count += 1
        # self.users.pop(0)

    def remove(self,row):
        self.users.pop(row)
        print(self.users)
        with open(self.file, "w") as csv_file:
            lines = []
            for user in self.users:
                lines.append(user.__str__()+"\n")
            print(lines)
            csv_file.writelines(lines)

    def add(self, user):
        self.users.append(user)
        with open(self.file, "w") as csv_file:
            lines = []
            for user in self.users:
                lines.append(user.__str__() + "\n")
            print(lines)
            csv_file.writelines(lines)


    def getUser(self,email,password):
        for user in self.users:
            if(user.isUser(email, password) is True):
                return user
        return None


if __name__ == "__main__":
    LC = User_Controller()
    LC.open_file()
