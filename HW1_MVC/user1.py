
 class user1:
    def __init__(self,id,username,password):
        self.__id=id
        self.__username=username
        self.__password=password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id


    @property
    def username(self):
        return self.__username


    @username.setter
    def username(self, username):
        self.__username = username


    @property
    def password(self):
        return self.__password

    # password setter
    @password.setter
    def password(self, password):
        self.__password = password

    def __str__(self):
        print("id: ".ljust(20), self.id)
        print("username: ".ljust(20), self.username)
        print("Password: ".ljust(20), self.password)


