from ConexionBD import ConnexionBD
from Main import *

def loginUsuario():
    conexion = ConnexionBD()
    mcursor = conexion.cursor()
    
    usuario1 = usuarioEntry.get()  # Obtiene el correo ingresado
    clave1 = password.get()        # Obtiene la contraseña ingresada
    
    # Verifica que los campos no estén vacíos
    if usuarioEntry.get() == "" or password.get() == "":
        errorLogin("Tiene que llenar los datos solicitados...") 
    else:
        # Verifica si el correo tiene un formato válido
        if es_correo_valido(usuario1):
            # Consulta para verificar si el correo existe en la base de datos
            sql_verificar_correo = "SELECT correo, contraseña FROM usuario WHERE correo = %s"
            mcursor.execute(sql_verificar_correo, [(usuario1)])
            resultado = mcursor.fetchone()  # Obtiene el primer resultado
            
            if resultado:  # Si el correo existe en la base de datos
                correo_db = resultado[0]  # Correo almacenado en la base de datos
                contraseña_db = resultado[1]  # Contraseña almacenada en la base de datos
                
                # Compara la contraseña ingresada con la almacenada
                if clave1 == contraseña_db:
                    # Si la contraseña es correcta, limpia los campos y abre el menú
                    usuarioEntry.delete(0, END)
                    password.delete(0, END)
                    menu()  # Abre la ventana del menú
                else:
                    # Si la contraseña es incorrecta, muestra un mensaje de error
                    errorLogin("Contraseña incorrecta")
                    password.delete(0, END)  # Limpia el campo de la contraseña
            else:
                # Si el correo no existe en la base de datos, muestra un mensaje de error
                errorLogin("El correo no está registrado")
                usuarioEntry.delete(0, END)  # Limpia el campo del correo
                password.delete(0, END)       # Limpia el campo de la contraseña
        else:
            # Si el correo no tiene un formato válido, muestra un mensaje de error
            errorLogin("Ingrese un correo válido")
            usuarioEntry.delete(0, END)  # Limpia el campo del correo
    
    ##conexion.close()  # Cierra la conexión a la base de datos

def es_correo_valido(correop):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correop) is not None

def inserta_datos():
    conexion = ConnexionBD()
    mcursor = conexion.cursor()
    
    nombre = nombreRegistro.get()
    apellido = apellidoRegistro.get()
    correo = correoRegistro.get()
    clave = passwordRegistro.get()
    direccion = direccionRegistro.get()
    estrato = estratoRegistro.get()
    celular = celularRegistro.get()
    
    if nombre == "" or apellido == "" or correo == "" or clave == "" or direccion == "" or estrato == "" or celular == "":
        errorLogin("Ingrese los datos solicitados") 
    else:
        if es_correo_valido(correo):
            sql_verificar = "SELECT * FROM usuario WHERE correo = %s"
            mcursor.execute(sql_verificar, (correo,))
            resultado = mcursor.fetchone()
            if resultado:
                errorLogin("El usuario ya existe")
            else:
                sql = "INSERT INTO usuario (nombre, apellido, correo, contraseña, direccion, estrato, celular) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(nombre, apellido, correo, clave, direccion, estrato, celular) 
    
                try:
                    mcursor.execute(sql)
                    conexion.commit()
                    nombreRegistro.delete(0, END)
                    apellidoRegistro.delete(0, END)
                    correoRegistro.delete(0, END)
                    passwordRegistro.delete(0, END)
                    direccionRegistro.delete(0, END)
                    estratoRegistro.delete(0, END)
                    celularRegistro.delete(0, END)
 
                    LoginCorrecto("Se realizo correctamente el registro")
        
                except:
                    conexion.rollback()
        
                    nombreRegistro.delete(0, END)
                    apellidoRegistro.delete(0, END)
                    correoRegistro.delete(0, END)
                    passwordRegistro.delete(0, END)
                    direccionRegistro.delete(0, END)
                    estratoRegistro.delete(0, END)
                    celularRegistro.delete(0, END)
        
                    conexion.close()
        else:
            errorLogin("Ingrese un correo valido")
    