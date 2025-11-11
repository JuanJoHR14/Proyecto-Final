import mysql.connector
# Importa el conector de MySQL (mddulo necesario para conectar con bases de datos MySQL)



conect={
    "host":"localhost", # Cambia el puerto si es necesario
    "user":"root",
    "password":"honey1308", #El de ustedes es: Estudiante2025
    "database":"tec", 
    "port":"3306" #Asegúrense del nombre de la base de datos
}

conexion = mysql.connector.connect(**conect)
 #usando **kwarfs paa  pasar un número variable de parámetros.
   
cursor = conexion.cursor() 
# Crea un cursor para ejecutar consultas SQL

print("Conexion exitosa a la base de datos")
