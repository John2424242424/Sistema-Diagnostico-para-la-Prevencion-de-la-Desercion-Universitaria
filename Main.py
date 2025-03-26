from customtkinter import *
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Sistema_experto import orientar
from BancoPreguntas import preguntas
from ConexionBD import ConnexionBD
import re
import getpass

logo= CTkImage(light_image= Image.open("Images/logo.png"), dark_image=Image.open("Images/logo.png"), size=(200, 200))
img_facebook = CTkImage(light_image= Image.open("Images/facebook.png"), dark_image=Image.open("Images/facebook.png"), size=(20,20))
img_google = CTkImage(light_image= Image.open("Images/google.png"), dark_image= Image.open("Images/google.png"), size=(20,20))

def ventanaInicio():
    global root

    root = CTk()
    root.geometry("500x600+350+20")
    root.minsize(480, 500)
    root.config(bg = "black")
    root.title("Inicio de Sesion")
    
    global verifica_usuario
    global verifica_contraseña
    
    verifica_usuario = StringVar()
    verifica_contraseña = StringVar()

    frame = CTkFrame(root, fg_color="white")
    frame.grid(column=0, row=0, sticky = 'nsew', padx = 50, pady = 50)

    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5],weight=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0,weight=1)

    CTkLabel(frame, image = logo, text="").grid(columnspan=2, row=0)
    
    global usuarioEntry, password

    usuarioEntry = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Correo',
                  border_color="green", fg_color="black", width = 220, height = 40)
    usuarioEntry.grid(columnspan=2, row=1, padx=4, pady=4)

    password = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Contraseña',
                  border_color="green", fg_color="black", width = 220, height = 40, show="*")
    password.grid(columnspan=2, row=2, padx=4, pady=4)

    checkbox = CTkCheckBox(frame, font=('sans rerif', 12), border_color="green", fg_color="black", text="Recuerdame")
    checkbox.grid(columnspan=2, row=3, padx=4, pady=4)

    btniniciar = CTkButton(frame, font=('sans rerif', 12), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="INICIAR SESION", height=40, command=loginUsuario)
    btniniciar.grid(columnspan=2, row=4, padx=4, pady=4)

    btngoogle = CTkButton(frame, image=img_google, font=('sans rerif', 12), border_color="purple", fg_color="black",
                       hover_color="purple", corner_radius=12, border_width=2, text="INICIAR SESION", height=40)
    btngoogle.grid(column=0, row=5, padx=4, pady=4)

    btnfacebook = CTkButton(frame, image=img_facebook, font=('sans rerif', 12), border_color="purple", fg_color="black",
                       hover_color="purple", corner_radius=12, border_width=2, text="INICIAR SESION", height=40)
    btnfacebook.grid(column=1, row=5, padx=4, pady=4)

    btnregistro = CTkButton(frame, font=('sans rerif', 12), border_color="purple", fg_color="black",
                       hover_color="purple", corner_radius=12, border_width=2, text="REGISTRO", height=40, command=formularioRegistro)
    btnregistro.grid(columnspan=2, row=6, padx=4, pady=4)

    root.mainloop()

def volver_a_inicio():
    
    ventanaRegistro.destroy()  # Cierra la ventana de registro
    root.deiconify()  # Muestra nuevamente la ventana principal
   
def formularioRegistro():
    
    global ventanaRegistro
    root.withdraw()

    ventanaRegistro = CTkToplevel(root)
    ventanaRegistro.geometry("500x600+350+20")
    ventanaRegistro.minsize(480, 500)
    ventanaRegistro.config(bg = "black")
    ventanaRegistro.title("Registro")
    
    frame = CTkFrame(ventanaRegistro, fg_color="white")
    frame.grid(column=0, row=0, sticky = 'nsew', padx = 50, pady = 50)
    
    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5],weight=1)

    ventanaRegistro.columnconfigure(0, weight=1)
    ventanaRegistro.rowconfigure(0,weight=1)
    
    CTkLabel(frame, image = logo, text="").grid(columnspan=2, row=0)
    
    global nombreRegistro, apellidoRegistro, correoRegistro, passwordRegistro, direccionRegistro, estratoRegistro, celularRegistro
    
    nombreRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Nombre',
                  border_color="green", fg_color="black", width = 220, height = 40)
    nombreRegistro.grid(columnspan=2, row=1, padx=4, pady=4)
    
    apellidoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Apellido',
                  border_color="green", fg_color="black", width = 220, height = 40)
    apellidoRegistro.grid(columnspan=2, row=2, padx=4, pady=4)

    correoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Correo',
                  border_color="green", fg_color="black", width = 220, height = 40)
    correoRegistro.grid(columnspan=2, row=3, padx=4, pady=4)

    passwordRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Contraseña',
                  border_color="green", fg_color="black", width = 220, height = 40, show = '*')
    passwordRegistro.grid(columnspan=2, row=4, padx=4, pady=4)
    
    direccionRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Direccion',
                  border_color="green", fg_color="black", width = 220, height = 40)
    direccionRegistro.grid(columnspan=2, row=5, padx=4, pady=4)

    estratoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Estrato',
                  border_color="green", fg_color="black", width = 220, height = 40)
    estratoRegistro.grid(columnspan=2, row=6, padx=4, pady=4)
    
    celularRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Celular',
                  border_color="green", fg_color="black", width = 220, height = 40)
    celularRegistro.grid(columnspan=2, row=7, padx=4, pady=4)
    
    btnregistro = CTkButton(frame, font=('sans rerif', 12), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="REGISTRAR USUARIO", height=40, command=inserta_datos)
    btnregistro.grid(columnspan=2, row=8, padx=4, pady=4)


    btnvolver = CTkButton(frame, font=('sans serif', 12), border_color="red", fg_color="black",
                          hover_color="red", corner_radius=12, border_width=2, text="VOLVER",
                          height=40, command=volver_a_inicio)
    btnvolver.grid(columnspan=2, row=9, padx=4, pady=4)

def salir_sesion():
    global ventanaMenu  # Asegura que accedemos a la ventana correcta
    ventanaMenu.destroy()  # Cierra la ventana del menú
    root.deiconify()  # Muestra nuevamente la ventana de inicio

def menu():
    global ventanaMenu
    root.withdraw()

    ventanaMenu = CTkToplevel(root)
    ventanaMenu.geometry("500x600+350+20")
    ventanaMenu.minsize(480, 500)
    ventanaMenu.config(bg = "black")
    ventanaMenu.title("Menu")
    
    frame = CTkFrame(ventanaMenu, fg_color="black")
    frame.grid(column=0, row=0, sticky = 'nsew', padx = 50, pady = 50)
    
    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5],weight=1)

    ventanaMenu.columnconfigure(0, weight=1)
    ventanaMenu.rowconfigure(0,weight=1)
    
    titulo = CTkLabel(frame, text="Menu Principal", font=('sans serif', 24), text_color="white")
    titulo.grid(columnspan=2, row=0, padx=4, pady=20)
    
    btnperfil = CTkButton(frame, font=('sans rerif', 16), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="PERFIL USUARIO", height=40, command=Perfil)
    btnperfil.grid(columnspan=2, row=1, padx=4, pady=4)
    
    btntest = CTkButton(frame, font=('sans rerif', 16), border_color="green", fg_color="black",
                        hover_color="green", corner_radius=12, border_width=2, text="REALIZAR TEST", height=40, 
                        command=lambda: testVentana(ventanaMenu))  # Pasa ventanaMenu como argumento
    btntest.grid(columnspan=2, row=2, padx=4, pady=4)

    btnCerrarSesion = CTkButton(frame, font=('sans serif', 12), border_color="red", fg_color="black",
                          hover_color="red", corner_radius=12, border_width=2, text="CERRAR SESION",
                          height=40, command=salir_sesion)
    btnCerrarSesion.grid(columnspan=2, row=3, padx=4, pady=4)
    
def volver_a_menu():
    global ventanaPerfil  # Asegura que accedemos a la ventana correcta
    ventanaPerfil.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu

def Perfil():
    global ventanaPerfil, ventanaMenu
    ventanaMenu.destroy()

    ventanaPerfil = CTkToplevel(root)
    ventanaPerfil.geometry("500x600+350+20")
    ventanaPerfil.minsize(480, 500)
    ventanaPerfil.config(bg = "black")
    ventanaPerfil.title("Perfil del usuario")
    
    frame = CTkFrame(ventanaPerfil, fg_color="white")
    frame.grid(column=0, row=0, sticky = 'nsew', padx = 50, pady = 50)
    
    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5],weight=1)

    ventanaPerfil.columnconfigure(0, weight=1)
    ventanaPerfil.rowconfigure(0,weight=1)

    btnVolverM = CTkButton(frame, font=('sans serif', 12), border_color="red", fg_color="black",
                          hover_color="red", corner_radius=12, border_width=2, text="VOLVER",
                          height=40, command=volver_a_menu)
    btnVolverM.grid(columnspan=2, row=3, padx=4, pady=4)

def testVentana(parent=None):
    if parent:
        parent.destroy()  # Cierra el menú antes de abrir el test
    
    ventanaTest = CTkToplevel(root)
    ventanaTest.geometry("500x600+350+20")
    ventanaTest.minsize(480, 500)
    ventanaTest.config(bg="black")
    ventanaTest.title("Test Vocacional")

    frame = CTkScrollableFrame(ventanaTest, fg_color="black")
    frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
    
    for i, pregunta in enumerate(preguntas):
        CTkLabel(frame, text=preguntas[pregunta], font=('sans rerif', 20)).grid(column=0, row=i * 2, padx=4, pady=4, sticky='w')
        btnSi = CTkButton(frame, font=('sans rerif', 12), border_color="green", fg_color="black",
                      hover_color="green", corner_radius=12, border_width=2, text="Si", height=40,
                      command=lambda i=i: set_response(i, 'Si'))
        btnNo = CTkButton(frame, font=('sans rerif', 12), border_color="red", fg_color="black",
                      hover_color="red", corner_radius=12, border_width=2, text="No", height=40,
                      command=lambda i=i: set_response(i, 'No'))
        btnSi.grid(column=1, row=(i * 2), padx=4, pady=4, sticky='e')
        btnNo.grid(column=2, row=(i * 2), padx=4, pady=4, sticky='e')

    respuestas = {}

    def set_response(i, response):
        respuestas[i] = response
            
    def enviar_datos():
        global vocacion_recomendada
    # Verifica si se han respondido todas las preguntas
        if len(respuestas) == len(preguntas):
            respuestas_estudiante = {}
            for i in range(0, 12):
                response = respuestas.get(i)
                respuestas_estudiante[i + 1] = response 
            vocacion_recomendada = orientar(respuestas_estudiante)
            Resultado()
            graficar_respuestas()
        else:
            print("Por favor, responde todas las preguntas antes de enviar.")
    
    def graficar_respuestas():
        if len(respuestas) == len(preguntas):
            categorias = {
                "Ingeniería de Sistemas": [1, 7, 12],
                "Ambiental": [4, 9],
                "Arte y Creatividad": [3, 6, 11],
                "Administración": [2, 5, 8, 10]
            }

            # Contar cuántas preguntas de cada categoría el usuario respondió con "Si"
            categoria_respuestas = {categoria: sum(1 for p in preguntas_categorias if respuestas.get(p) == 'Si') for categoria, preguntas_categorias in categorias.items()}

            # Crear la gráfica de pastel
            fig, ax = plt.subplots()
            colors = ['blue', 'green', 'orange', 'red']  # Colores para cada categoría
            wedges, texts, autotexts = ax.pie(categoria_respuestas.values(), labels=categoria_respuestas.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title('Respuestas "No" por Categoría')

            # Mostrar la gráfica en la ventana de resultados
            chart_frame = CTkFrame(ventanaResultado)
            chart_frame.grid(column=0, row=2, padx=4, pady=4)

            canvas = FigureCanvasTkAgg(fig, master=chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
        else:
            print("Por favor, responde todas las preguntas antes de graficar.")

    
    btnVocacion = CTkButton(frame, font=('sans rerif', 12), border_color="green", fg_color="black",
                              hover_color="red", corner_radius=12, border_width=2, text="Terminar test",
                              height=40, command=enviar_datos)
    btnVocacion.grid(columnspan=2, row=len(preguntas) * 2, padx=4, pady=4)

    ventanaTest.columnconfigure(0, weight=1)
    ventanaTest.rowconfigure(0, weight=1)
        

    ventanaTest.mainloop()

def Resultado():
    global ventanaResultado
    ventanaResultado = CTkToplevel(root)
    ventanaResultado.geometry("500x600+350+20")
    ventanaResultado.minsize(480, 500)
    ventanaResultado.config(bg = "black")
    ventanaResultado.title("Resultados")
    
    frame = CTkFrame(ventanaResultado, fg_color="black")
    frame.grid(column=0, row=0, sticky = 'nsew', padx = 50, pady = 50)
    
    frame.columnconfigure([0,1], weight=1)
    frame.rowconfigure([0,1,2,3,4,5],weight=1)

    ventanaResultado.columnconfigure(0, weight=1)
    ventanaResultado.rowconfigure(0,weight=1)
    
    titulo = CTkLabel(frame, text="Resultados", font=('sans serif', 24), text_color="white")
    titulo.grid(columnspan=2, row=0, padx=4, pady=20)
    
    vocacion = CTkLabel(frame, text=vocacion_recomendada, font=('sans serif', 24), text_color="white")
    vocacion.grid(columnspan=2, row=1, padx=4, pady=20)
    
    btnregresar = CTkButton(frame, font=('sans rerif', 16), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="Finalizar programa", height=40, command=root.quit)
    btnregresar.grid(columnspan=2, row=2, padx=4, pady=4)
        
    
def error():
    global err
    err = CTkToplevel()
    err.title("Error")
    err.geometry("500x100+350+20")
    err.minsize(480, 500)
    err.config(bg = "white")
    err.title("Registro")
    CTkLabel(err,text="Todos los campos son necesarios..",fg_color="red",font=('sans rerif', 12)).grid(column=0, row=0, padx = 50, pady = 50)
    CTkLabel(err,text="").grid(column=1, row=0, padx = 50, pady = 50)
    CTkButton(err, font=('sans rerif', 12), text="Ok",bg="grey",width=8,height=1,command=err.destroy).grid(column=2, row=0, padx = 50, pady = 50)
    
def errorLogin(message):
    global err
    err = CTkToplevel()
    err.title("Error")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg = "white")
    err.title("Registro")
    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="red", fg_color="black",
                       hover_color="red", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack(pady=10)
    
def LoginCorrecto(message):
    global err
    err = CTkToplevel()
    err.title("Exito")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg = "white")
    err.title("Registro")
    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack()
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
    
ventanaInicio()