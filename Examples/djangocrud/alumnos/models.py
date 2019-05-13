from django.db import models
import psycopg2

class Alumnos(models.Model):
    idalumno = models.AutoField(primary_key=True, serialize=True, verbose_name='idalumno')
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)



class Helper():
    def GetConection(self):
        return psycopg2.connect(dbname="UANL", user="postgres", password="123456")
    def GetSelect(self,query):
        connection = self.GetConection()
        cursor = connection.cursor()
        try:
              #ejecutamos el query
            cursor.execute(query)
            #pasamos el resultado a una variable, el fetchall obtiene todas las filas
            result = cursor.fetchall()
            return result
        except (Exception, psycopg2.Error) as error:
            print ("Error en la conexion", error)
        finally:
            #cerramos la conexion siempre
            if(connection):
                connection.close()


