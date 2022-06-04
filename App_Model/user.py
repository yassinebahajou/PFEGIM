

class User():
    def __init__(self,mail,pwd,name,isAdmin):
        self.mail = mail
        self.pwd = pwd
        self.name = name
        self.isAdmin = isAdmin

    def isUser(self,email,password):
        if(self.mail==email and self.pwd == password):
            return True
        return False
