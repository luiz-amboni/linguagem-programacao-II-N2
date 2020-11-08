import psycopg2

class Connection():

    def get_connection(self):
        connection = psycopg2.connect(user="postgres",
                                      password="brunaodeus",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="prova")
        return connection