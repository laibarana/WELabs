
from DB import DBHandler
from exception import *
from faculty import faculty
class  controller:
    def __init__(self):


        self.__faculty = None
        self.__student = None

    @property
    def faculty(self):
        if self.__faculty is None:
            self.__read_faculty()
        return self.__faculty

    @property
    def student(self):
        if self.__student is None:
            self.__read_student()
        return self.__student

    def __read_faculty(self):

        db = DBHandler()
        db.connect()
        self.__faculty = db.select("select * from faculty")

    def __read_student(self):

        db = DBHandler()
        db.connect()
        self.__student = db.select("select * from student")

    def __get_faculty(self, username, password):

        for faculty in self.faculty:
            if faculty.username.lower() == username.lower() and faculty.password == password:
                return faculty
        return None
    def __get_student(self, username, password):

        for student in self.faculty:
            if student.username.lower() == username.lower() and student.password == password:
                return student
        return None

    def __update_faculty(self,suject,user_id ):

        db = DBHandler()
        db.connect()
        db.update("update faculty set subject=%s where user_id=%s", (suject,user_id ))

    def __update_student(self,cgpa,user_id ):

        db = DBHandler()
        db.connect()
        db.update("update student set cgpa=%s where user_id=%s", (cgpa,user_id ))
    def __delete_faculty(self,id ):

        db = DBHandler()
        db.connect()
        db.update("delete from faculty  where id=%s", (id ))


    def __delete_student (self, id):
         db = DBHandler()
         db.connect()
         db.update("delete student where id=%s", (id))

    def loginfaculty(self):

        try:
            id = input('Enter your faculty id: ')
            designation = input('Enter your pin: ')
            subject = input('Enter your sebject: ')
            user_id = input('Enter your pin: ')
            faculty = self.__get_faculty(username, password)

            if faculty is None:
                raise IDNotFound("Invalid username. or password")
            try:
                choice = 1
                while True:

                    print('1. enter id')
                    print('2.enter designation')
                    print('3. enter subject')
                    print('4.  enter Sign')
                    print('5. enter  Exit')

                    try:
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            self.__id(faculty)
                        elif choice == 2:
                            self.__designation(faculty)
                        elif choice == 3:
                            self.__subject(faculty)
                        elif choice == 4:
                            print('Signed out successfully')

                            self.login()
                            break
                        elif choice == 5:
                            print('Thank you for using system')
                            exit()
                        else:
                            print('Invalid choice')
                    except ValueError as e:
                        print(str(e))
                        self.login()
            except ValueError as e:
                pass
        except AccountNotFound as e:
            print(str(e))
            self.login()
        except ValueError as e:
            print(str(e))
            self.login()

    def loginstudent(self):

        try:
            id = input('Enter your faculty id: ')
            semester = input('Enter your semester: ')
            cgpa= input('Enter your cgpa: ')
            major=input('Enter your cgpa: ')
            user_id = input('Enter your user_id: ')
            student = self.__get_student(username, password)

            if faculty is None:
                raise IDNotFound("Invalid username. or password")
            try:
                choice = 1
                while True:

                    print('1. enter id')
                    print('2.enter semester')
                    print('3. enter cgpa')
                    print('4. enter major')
                    print('5.  enter Sign')
                    print('6. enter  Exit')

                    try:
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            self.__id(student)
                        elif choice == 2:
                            self.__semester(student)
                        elif choice == 3:
                            self.__cgpa(student)
                        elif choice == 4:
                            self.__major(student)
                        elif choice == 5:
                            print('Signed out successfully')

                            self.login()
                            break
                        elif choice == 6:
                            print('Thank you for using system')
                            exit()
                        else:
                            print('Invalid choice')
                    except ValueError as e:
                        print(str(e))
                        self.login()
            except ValueError as e:
                pass
        except  AccountNotFound as e:
            print(str(e))
            self.login()
        except ValueError as e:
            print(str(e))
            self.login()





