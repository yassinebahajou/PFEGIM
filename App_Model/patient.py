

class Patient():
    def __init__(self,nom,prenom,age,sex,xray_img,infection):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sex = sex
        self.xray_image = xray_img
        self.infected = infection


    def __str__(self):
        return f"{self.nom};{self.prenom};{self.age};{self.sex};{self.infected};{self.xray_image}"
