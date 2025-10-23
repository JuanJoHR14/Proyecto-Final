import mysql.connector
from conector import conexion,cursor



def registrar():
    print("Ingresar los siguientes datos: ")
    usu = input("Nombre de usuario: ")
    contra = input("Contraseña: ")
    corr = input("Correo electronico: ")
    

    sql_query = "INSERT INTO usuario_b (usu,contra,corr,rol,nom, apll,fec_nac, genero,pais,ciudad) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
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

def completar():
    cursor = "SELECT FROM usuario_b ()"
    ident = input("Nº Identificacion: ")
    nom = input("Nombre: ")
    apll = input("Apellido: ")
    rol1 = input("Rol.. (V) Vendedor / (C) Cliente: ")
    rol=rol1.lower()
    fec_nac = input("Fecha de nacimiento (aaaa/mm/dd): ")
    gene1 = input("Genero... (F) / (M): ")
    gene = gene1.lower()
    pais = input("Pais: ")
    ciud = input("Ciudad: ")

    sql_query = "INSERT INTO usuario_b (usu,contra,corr,rol,nom, apll,fec_nac, genero,pais,ciudad) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)"
    data = (ident, rol, nom, apll, fec_nac, gene, pais, ciud)





#registrar(None, None, None, None, None, None)

from conector import conexion,cursor

def ini_sesion():
    
    print("Bienvenido señor usuario, por favor registrese.")
    usu = input("Nombre con el cual se registró: ")
    cont = input("Contraseña: ")


    if usu == nom





    

 