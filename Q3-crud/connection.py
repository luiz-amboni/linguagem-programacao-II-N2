import psycopg2

class Connection():

    def getConnection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="brunaodeus",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="crud_N2_LPII")
        print("Banco conectado.")
        return connection