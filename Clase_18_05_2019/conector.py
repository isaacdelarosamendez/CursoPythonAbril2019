import psycopg2

class Helper():
    def GetConnection(self):
        #Creamos la conexion
        connection = psycopg2.connect(host="localhost",
        dbname="uanl", 
        user="postgres", 
        password="123456")
        return connection
    
    def GetCursor(self,con):
        return con.cursor()
    
    def Execute(self,query):
        cursor = self.GetCursor(self.GetConnection())
        cursor.execute(query)
        return cursor.fetchall()

_helper = Helper()
print(_helper.Execute("select * from cursos"))


