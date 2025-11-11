import mysql.connector
from conector import conexion,cursor

def cli():
    print("")
    print("--- VER ---")
    print("Bienvenido señor usuario")
    print("")
    sql_query = "SELECT * FROM producto"
    cursor.execute(sql_query)
    resultados = cursor.fetchall()
    for fila in resultados :
        
        print("---------------------------")
        print(f" ID: {fila[0]}")
        print(f" Nombre: {fila[1]}")
        print(f" Descripción: {fila[2]}")
        print(f" Precio: {fila[3]}")
        print(f" Cantidad: {fila[4]} | ")
        print("---------------------------")
        print("")
        
    n = input("Ingrese el ID del producto que desea comprar: ")
        
    print("")
    m = input("Desea comprar este producto? (S) Si / (No) No: ").lower()
        
    if m == 's':
        sql_delete_query = "DELETE FROM producto WHERE idproducto = %s"
        cursor.execute(sql_delete_query, (n,))
        conexion.commit()
        print("Producto en camino.")
        
    print("")
    print("¿Desea comprar otro producto? (S) Si / (N) No ")
    b = input("- ").lower()
    if b == "s":
        cli()
    else:
        print("")
        print("Gracias por su compra.")
        exit
        
    
    
    
    
    
    
    
    
    
    

def ag():
    
    print("---AGREGAR---")
    print("Agregue un producto al inventario")
    print("")
    id = int(input("ID del producto: "))
    nom = input("Nombre del producto: ")
    des = input("Descripción del producto: ")
    prec = int(input("Precio del producto: "))
    cant = int(input("Cantidad en inventario: "))

    sql_query = "INSERT INTO producto (idproducto, nom, des, precio, cant) VALUES (%s, %s, %s, %s, %s)"
    data = (id, nom, des, prec, cant)
    cursor.execute(sql_query, data)
    conexion.commit()
    print("")
    print("Producto agregado exitosamente.")
    
    print("")
    print("¿Desea agregar otro producto? (S) Si / (N) No ")
    ñ = input("- ").lower()
    if ñ == "s":
        ag()
    else:
       if ñ == "n":
            print("¿Desea regresar al menú? (S) Si / (N) No ")
            ñ = input("- ").lower()
            if ñ == "s":
                ven_men()
            else:
                exit
            








def leer():
    print("")
    print("--- VER ---")
    print("Inventario de Productos")
    print("")
    sql_query = "SELECT * FROM producto"
    cursor.execute(sql_query)
    resultados = cursor.fetchall()
    for fila in resultados :
        
        print("---------------------------")
        print(f" ID: {fila[0]}")
        print(f" Nombre: {fila[1]}")
        print(f" Descripción: {fila[2]}")
        print(f" Precio: {fila[3]}")
        print(f" Cantidad: {fila[4]} | ")
        print("---------------------------")
        print("")
        
    print("")
    print("¿Desea ver otro producto? (S) Si / (N) No ")
    ñ = input("- ").lower()
    if ñ == "s":
        leer()
    else:
       if ñ == "n":
            print("¿Desea regresar al menú? (S) Si / (N) No ")
            ñ = input("- ").lower()
            if ñ == "s":
                ven_men()
            else:
                exit
        









def act():
    print("")
    print("--- ACTUALIZAR ---")
    print("Inventario de Productos")
    print("")
    sql_query = "SELECT * FROM producto"
    cursor.execute(sql_query)
    resultados = cursor.fetchall()
    for fila in resultados :
        
        print("---------------------------")
        print(f" ID: {fila[0]}")
        print(f" Nombre: {fila[1]}")
        print(f" Descripción: {fila[2]}")
        print(f" Precio: {fila[3]}")
        print(f" Cantidad: {fila[4]} | ")
        print("---------------------------")
        print("")       
               
    print("")    
    o = input("Digite el ID del producto a actualizar: ")
    
    sql_query = "SELECT * FROM producto WHERE idproducto = %s"
    cursor.execute(sql_query, (o,))
    resultados = cursor.fetchall()
    
    for fila in resultados:
        print("")
        print(f"Seguro que desea actualizar el producto (S) Si / (N) No: ")
        print("")
        print(f" ID: {fila[0]}")
        print(f" Nombre: {fila[1]}")
        print(f" Descripción: {fila[2]}")
        print(f" Precio: {fila[3]}")
        print(f" Cantidad: {fila[4]} | ")
        print("")
        a = input("- ").lower()
        
        if a == 's':
            nid = input("ID: ") or fila[0]
            nnom = input("Nombre: ") or fila[1]
            ndes = input("Descripción: ") or fila[2]
            nprec = input("Precio: ") or fila[3]
            ncant = input("Cantidad: ") or fila[4]
            
            slq_update_query = ("""
                            UPDATE producto SET 
                            idproducto = %s, nom = %s, des = %s, precio = %s, cant = %s 
                            WHERE idproducto = %s
                            """)
            datos = (nid, nnom, ndes, nprec, ncant, (o))
            cursor.execute(slq_update_query, datos)
            conexion.commit()
            print("Producto actualizado exitosamente.")
            
    print("")
    print("¿Desea actualizar otro producto? (S) Si / (N) No ")
    ñ = input("- ").lower()
    if ñ == "s":
        act()
    else:
       if ñ == "n":
            print("¿Desea regresar al menú? (S) Si / (N) No ")
            ñ = input("- ").lower()
            if ñ == "s":
                ven_men()
            else:
                exit
            
            
            
            
            
            
def elim():
    print("")
    print("--- ELIMINAR ---")
    print("Inventario de Productos")
    print("")
    sql_query = "SELECT * FROM producto"
    cursor.execute(sql_query)
    resultados = cursor.fetchall()
    for fila in resultados :
        
        print("---------------------------")
        print(f" ID: {fila[0]}")
        print(f" Nombre: {fila[1]}")
        print(f" Descripción: {fila[2]}")
        print(f" Precio: {fila[3]}")
        print(f" Cantidad: {fila[4]} | ")
        print("---------------------------")
        print("")
        
    n = input("Ingrese el ID del producto que desea eliminar: ")
        
    print("")
    m = input("Desea eliminar este producto? (S) Si / (No) No: ").lower()
        
    if m == 's':
        sql_delete_query = "DELETE FROM producto WHERE idproducto = %s"
        cursor.execute(sql_delete_query, (n,))
        conexion.commit()
        print("Producto eliminado exitosamente.")
        
    print("")
    print("¿Desea eliminar otro producto? (S) Si / (N) No ")
    ñ = input("- ").lower()
    if ñ == "s":
        elim()
    else:
       if ñ == "n":
            print("¿Desea regresar al menú? (S) Si / (N) No ")
            ñ = input("- ").lower()
            if ñ == "s":
                ven_men()
            else:
                exit






def ven_men():
    
    print("")
    print("--- MENÚ ---")
    print("")
    print("Bienvenido señor usuario")
    print("Elija una opción: ")
    print("")
    print("1 - Agregar producto")
    print("2 - Ver producto")
    print("3 - Actualizar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")
    print("")
    o = int(input("- "))
    print("")
    
    if o == 1:
        ag()
    elif o == 2:
        leer()
    elif o == 3:
        act()
    elif o == 4:
        elim()
    elif o == 5:
        exit








def login():
    
    print("")
    print("--- Bienvenido a inicio de sesión ---")
    print("")
    identificacion = input("Ingrese su identificación: ")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    sql_query = "SELECT usuario, contra, rol FROM usuario_b WHERE usu = %s"
    cursor.execute(sql_query, (identificacion,))
    resultado = cursor.fetchone()
    usu1, con1, roll= resultado
    
    if usuario == usu1 and contraseña == con1:
        print("")
        print("Inicio de sesión exitoso.")
        print("")
    else:
        print("Credenciales inválidas. Intente de nuevo.")
        
    if roll == "Vendedor":
        ven_men()
    elif roll == "Cliente":
        cli()
        


def regis():
    print("")
    print("--- Bienvenido a registro de usuarios ---")
    print("")
    print("Ingrese los siguientes datos ")

    ident = input("Identificación: ")
    usu = input("Usuario: ")
    con = input("Contraseña: ")
    rol = input("Rol (V) Vendedor / (C) Cliente: ").lower()
    if rol == 'v':
        rol = "Vendedor"
    elif rol == 'c':
        rol = "Cliente"
    else:
        print("Rol no válido. No se insertarán datos.")
        return
    nom = input("Nombres: ")
    apll = input("Apellidos: ")
    corr = input("Correo: ")
    gene = input("Genero (F) Femenino / (M) Masculino: ").lower()
    if gene == 'm':
        gene = "Masculino"
    elif gene == 'f':
        gene = "Femenino"
    else:
        print("ERROR: Género no válido. No se insertarán datos.")
    ciud = input("Ciudad: ")

    sql_query = "INSERT INTO usuario_b (usu, usuario, contra, rol, nom, apll, correo, gene, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (ident, usu, con, rol, nom, apll, corr, gene, ciud)
    cursor.execute(sql_query,data)
    conexion.commit()
    print("Datos guardados exitosamente.")
    
    login()


        
def inicio():
    print("")
    print("--- Bienvenido señor usuario ---")
    
    print("")
    print("1 - Iniciar sesión ")
    print("2 - Registrarse ")
    print("")
    
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        login()
    elif opcion == '2':
        regis()
    else:
        print("Opción no válida. Intente de nuevo.")            
    
    
inicio()










   



    

 