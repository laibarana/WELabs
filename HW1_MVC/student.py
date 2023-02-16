
from user1 import user1
class student(user1):
    def __init__(self,id,semester,cgpa,major,user_id):
        self.__id=id
        self.__semester=semester
        self.__cgpa = cgpa
        self.__major = major
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def semester (self):
        return self.__semester

    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    @property
    def cgpa(self):
        return self.__cgpa


    @cgpa.setter
    def cgpa(self, cgpa):
        self.__cgpa = cgpa

        @property
        def major(self):
            return self.__major

        @major.setter
        def major(self, major):
            self.__major= major

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    def __str__(self):
        print("id: ".ljust(20), self.id)
        print("semester: ".ljust(20), self.semester)
        print("cgpa: ".ljust(20), self.cgpa)
        print("major: ".ljust(20), self.major)
        print("user_id: ".ljust(20), self.user_id)


