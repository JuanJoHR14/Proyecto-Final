import mysql.connector
from conector import conexion,cursor

def registrar():
    print("Ingresar los siguientes datos: ")
    ident = input("Nº Identificacion: ")
    nom = input("Nombre: ")
    apll = input("Apellido: ")
    rol1 = input("Rol.. (V) Vendedor / (C) Cliente: ")
    rol=rol1.lower()
    fec_nac = input("Fecha de nacimiento (aaaa/mm/dd): ")
    gene1 = input("Genero: ")
    gene = gene1.lower()
    pais = input("Pais: ")
    ciud = input("Ciudad: ")

    sql_query = "INSERT INTO usuario_b (id_usuario,rol,nom, apll,fec_nac, genero,pais,ciudad) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
    data = (ident, rol, nom, apll, fec_nac, gene, pais, ciud)

    try:
        cursor.execute(sql_query,data)
        conexion.commit()
        print("Datos guardados exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error al guardar los datos: {err}")
        # Es buena práctica hacer un rollback en caso de error
        conexion.rollback() 
    if conexion:
        conexion.close()
    if cursor:
        cursor.close()

    
registrar()

#registrar(None, None, None, None, None, None)



    

 