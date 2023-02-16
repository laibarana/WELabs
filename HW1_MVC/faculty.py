
from user1 import user1

class faculty(user1):
    def __init__(self,id,designation,subject,user_id):
        self.__id=id
        self.__designation=designation
        self.__subjec=subject
        self.__user_id=user_id

        @property
        def id(self):
            return self.__id

        @id.setter
        def id(self, id):
            self.__id = id

        @property
        def designation(self):
            return self.__designation

        @designation.setter
        def designation(self, designation):
            self.__designation = designation

        @property
        def subject(self):
            return self.__subject


        @subject.setter
        def subject(self, subject):
            self.__subject = subject

        @property
        def user_id(self):
            return self.__user_id

        @user_id.setter
        def user_id(self, user_id):
            self.__user_id = user_id




        def __str__(self):
            print("id: ".ljust(20), self.id)
            print("designation: ".ljust(20), self.designation)
            print("subject: ".ljust(20), self.subject)
            print("user_id: ".ljust(20), self.user_id)

