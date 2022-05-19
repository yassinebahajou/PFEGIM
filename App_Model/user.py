

class User():
    def __init__(self,mail,pwd,name,isAdmin):
        self.mail = mail
        self.pwd = pwd
        self.name = name
        self.isAdmin = isAdmin

    def isUser(self,mail,password):
        if(self.mail==mail and self.pwd == password):
            return True
        return False
