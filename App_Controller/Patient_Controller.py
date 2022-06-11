import csv

from App_Model.patient import Patient
from App_Model.user import User


class Patient_Controller():
    def __init__(self):
        self.file = 'files/patient.csv'
        self.open_file()

    def open_file(self):
        self.patients = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            self.line_count = 0
            for row in csv_reader:
                patient = Patient(row[0],row[1],row[2],row[3],row[4],row[5])
                self.patients.append(patient)
                self.line_count += 1

    def remove(self,row):
        self.patients.pop(row)
        print(self.patients)
        with open(self.file, "w") as csv_file:
            lines = []
            for user in self.patients:
                lines.append(user.__str__()+"\n")
            print(lines)
            csv_file.writelines(lines)

    def add(self, patient):
        self.patients.append(patient)
        with open(self.file, "w") as csv_file:
            lines = []
            for patient in self.patients:
                lines.append(patient.__str__() + "\n")
            print(lines)
            csv_file.writelines(lines)


    # def getUser(self,email,password):
    #     for user in self.patients:
    #         if(user.isUser(email, password) is True):
    #             return user
    #     return None


if __name__ == "__main__":
    LC = Patient_Controller()
    LC.open_file()
