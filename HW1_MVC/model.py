
import pymysql

class DBHANDLER:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = pymysql.connect(host='localhost', user='root', password='laibarana@123', database='sys')
            self.__cursor = self.__connection.cursor()
        except Exception as e:
            print(str(e))

    def disconnect(self):
        if self.__connection is not None:
            self.__connection.close()

    def update(self,sql,args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()
    def update(self,sql,args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()

    def delete(self, sql, args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()

    def delete(self, sql, args):
        try:
            # check if the connection is established or not
            if self.__connection is None:
                self.connect()

            # execute the sql
            self.__cursor.execute(sql, args)

            # commit the changes
            self.__connection.commit()
        except Exception as e:
            print(str(e))
        finally:
            self.disconnect()












