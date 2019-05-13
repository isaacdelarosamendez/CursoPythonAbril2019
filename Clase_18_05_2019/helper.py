import psycopg2

#Creamos la conexion
connection = psycopg2.connect(dbname="UANL", user="postgres", password="123456")

try:
  #abrimos el cursor a la base de datos
  cursor = connection.cursor()
  
  '''#creamos el query a ejecutar
  query = "select * from alumnos"
  #ejecutamos el query
  cursor.execute(query)
  #pasamos el resultado a una variable, el fetchall obtiene todas las filas
  result = cursor.fetchall() 
  for x in result:
    print(x)'''
    
  '''
  postgres_insert_query = """ INSERT INTO alumnos (nombres, apellidos) VALUES (%s,%s)"""
  record_to_insert = ('Eliud','De la rosa')
  cursor.execute(postgres_insert_query, record_to_insert)
  connection.commit()
  count = cursor.rowcount
  if count>0:
    print ("Insercion correcta")'''
except (Exception, psycopg2.Error) as error :
    connection.rollback()
    print ("Error en la conexion", error)
finally:
    #cerramos la conexion siempre
        if(connection):
            cursor.close()
            connection.close()