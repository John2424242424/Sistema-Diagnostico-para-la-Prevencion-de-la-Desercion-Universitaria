from customtkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Sistema_experto import orientar
from BancoPreguntas import obtener_preguntas
from Carreras import obtener_carreras
import re
import getpass
from conexion import db
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import ttk
from CTkMessagebox import CTkMessagebox


from google.cloud.firestore_v1.base_query import FieldFilter, BaseCompositeFilter

import requests
import uuid
from datetime import datetime

usuario_logueado = None

# Obtener la ruta correcta al archivo
def resource_path(relative_path):
    """ Obtiene la ruta absoluta del recurso, compatible con PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Usar la ruta correcta al abrir la imagen
logo_path = resource_path("Images/logo.png")
image = Image.open(logo_path)

logo= CTkImage(light_image= Image.open("Images/logo.png"), dark_image=Image.open("Images/logo.png"), size=(200, 200))
img_facebook = CTkImage(light_image= Image.open("Images/facebook.png"), dark_image=Image.open("Images/facebook.png"), size=(20,20))
img_google = CTkImage(light_image= Image.open("Images/google.png"), dark_image= Image.open("Images/google.png"), size=(20,20))

def ventanaInicio():
    global root

    root = CTk()

   # Maximiza la ventana de forma manual obteniendo las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()  # Obtiene el ancho de la pantalla
    screen_height = root.winfo_screenheight()  # Obtiene la altura de la pantalla

    # Establece el tamaño de la ventana al tamaño completo de la pantalla
    root.geometry(f"{screen_width}x{screen_height}+0+0") 

    root.config(bg="black")
    root.title("Inicio de Sesion")
    
    global verifica_usuario
    global verifica_contraseña
    
    verifica_usuario = StringVar()
    verifica_contraseña = StringVar()

    frame = CTkFrame(root, fg_color="white")
    frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

    frame.columnconfigure([0, 1], weight=1)
    frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    CTkLabel(frame, image=logo, text="").grid(columnspan=2, row=0)
    
    global usuarioEntry, password

    usuarioEntry = CTkEntry(frame, font=('sans serif', 12), placeholder_text='Correo',
                            border_color="green", fg_color="white", width=220, height=40)
    usuarioEntry.grid(columnspan=2, row=1, padx=4, pady=4)

    password = CTkEntry(frame, font=('sans serif', 12), placeholder_text='Contraseña',
                        border_color="green", fg_color="white", width=220, height=40, show="*")
    password.grid(columnspan=2, row=2, padx=4, pady=4)

    checkbox = CTkCheckBox(frame, font=('sans serif', 12), border_color="green", fg_color="black", text="Recuerdame")
    checkbox.grid(columnspan=2, row=3, padx=4, pady=4)

    btniniciar = CTkButton(frame, font=('sans serif', 12), border_color="green", fg_color="black",
                           hover_color="green", corner_radius=12, border_width=2, text="INICIAR SESION", height=40, command=loginUsuario)
    btniniciar.grid(columnspan=2, row=4, padx=4, pady=4)

    btngoogle = CTkButton(frame, image=img_google, font=('sans serif', 12), border_color="purple", fg_color="black",
                          hover_color="purple", corner_radius=12, border_width=2, text="INICIAR SESION", height=40)
    btngoogle.grid(column=0, row=5, padx=4, pady=4)

    btnfacebook = CTkButton(frame, image=img_facebook, font=('sans serif', 12), border_color="purple", fg_color="black",
                            hover_color="purple", corner_radius=12, border_width=2, text="INICIAR SESION", height=40)
    btnfacebook.grid(column=1, row=5, padx=4, pady=4)

    btnregistro = CTkButton(frame, font=('sans serif', 12), border_color="purple", fg_color="black",
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
    ventanaRegistro.state('zoomed')  # Maximiza la ventana

    
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
    
    global admin, idRegistro, nombreRegistro, apellidoRegistro, correoRegistro, passwordRegistro, direccionRegistro, estratoRegistro, celularRegistro
    
    idRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Cedula',
                  border_color="green", fg_color="white", width = 220, height = 40)
    idRegistro.grid(columnspan=2, row=1, padx=4, pady=4)

    nombreRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Nombre',
                  border_color="green", fg_color="white", width = 220, height = 40)
    nombreRegistro.grid(columnspan=2, row=2, padx=4, pady=4)
    
    apellidoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Apellido',
                  border_color="green", fg_color="white", width = 220, height = 40)
    apellidoRegistro.grid(columnspan=2, row=3, padx=4, pady=4)

    correoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Correo',
                  border_color="green", fg_color="white", width = 220, height = 40)
    correoRegistro.grid(columnspan=2, row=4, padx=4, pady=4)

    passwordRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Contraseña',
                  border_color="green", fg_color="white", width = 220, height = 40, show = '*')
    passwordRegistro.grid(columnspan=2, row=5, padx=4, pady=4)
    
    direccionRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Direccion',
                  border_color="green", fg_color="white", width = 220, height = 40)
    direccionRegistro.grid(columnspan=2, row=6, padx=4, pady=4)

    estratoRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Estrato',
                  border_color="green", fg_color="white", width = 220, height = 40)
    estratoRegistro.grid(columnspan=2, row=7, padx=4, pady=4)
    
    celularRegistro = CTkEntry(frame, font=('sans rerif', 12), placeholder_text='Celular',
                  border_color="green", fg_color="white", width = 220, height = 40)
    celularRegistro.grid(columnspan=2, row=8, padx=4, pady=4)
    
    btnregistro = CTkButton(frame, font=('sans rerif', 12), border_color="green", fg_color="black",
                       hover_color="green", corner_radius=12, border_width=2, text="REGISTRAR USUARIO", height=40, command=inserta_datos)
    btnregistro.grid(columnspan=2, row=9, padx=4, pady=4)


    btnvolver = CTkButton(frame, font=('sans serif', 12), border_color="red", fg_color="black",
                          hover_color="red", corner_radius=12, border_width=2, text="VOLVER",
                          height=40, command=volver_a_inicio)
    btnvolver.grid(columnspan=2, row=10, padx=4, pady=4)

def salir_sesion():
    global ventanaMenu  # Asegura que accedemos a la ventana correcta
    ventanaMenu.destroy()  # Cierra la ventana del menú
    root.deiconify()  # Muestra nuevamente la ventana de inicio

def menu():
    
    global ventanaMenu, admin
    root.withdraw()  # Ocultar la ventana principal
    
    ventanaMenu = CTkToplevel(root)
    ventanaMenu.state('zoomed')  # Maximiza la ventana
    ventanaMenu.config(bg="#121212")  # Fondo oscuro elegante
    ventanaMenu.title("Menú Principal")
    
    # Crear marco principal con estilo premium
    frame = CTkFrame(ventanaMenu, fg_color="white")
    frame.grid(column=0, row=0, sticky='nsew', padx=30, pady=30)

    ventanaMenu.columnconfigure(0, weight=1)
    ventanaMenu.rowconfigure(0, weight=1)

    frame.columnconfigure([0, 1], weight=1)
    frame.rowconfigure(list(range(6)), weight=1)

    # Imagen alineada a la izquierda y más arriba
    CTkLabel(frame, image=logo, text="").grid(columnspan=2, row=0)

    # Título más arriba
    titulo = CTkLabel(frame, text="Menú Principal", font=('Helvetica', 28, 'bold'), text_color="#1E1E1E")
    titulo.grid(columnspan=2, row=1, padx=10, pady=5)

    # Botón de perfil del usuario
    btnPerfil = CTkButton(frame, text="👤 Perfil de Usuario", font=('Helvetica', 16), border_color="Green",
                          fg_color="#222", hover_color="Green", text_color="white",
                          corner_radius=20, border_width=2, height=50, width=280, command=Perfil)
    btnPerfil.grid(columnspan=2, row=0, sticky='ne', padx=20, pady=12)

    # Verifica si el usuario tiene permisos de administrador
    if usuario_logueado.get("admin", False):
        btnAdminUsuarios = CTkButton(frame, text="🔧 Administrar Usuarios", font=('Helvetica', 16), border_color="Green",
                                     fg_color="#222", hover_color="Green", text_color="white",
                                     corner_radius=20, border_width=2, height=50, width=280, command=lambda: abrir_admin_usuarios())
        btnAdminUsuarios.grid(columnspan=2, row=3, padx=20, pady=12)

        btnAdminPreguntas = CTkButton(frame, text="📜 Administrar Preguntas", font=('Helvetica', 16), border_color="Green",
                                      fg_color="#222", hover_color="Green", text_color="white",
                                      corner_radius=20, border_width=2, height=50, width=280, command=lambda: abrir_admin_preguntas())
        btnAdminPreguntas.grid(columnspan=2, row=4, padx=20, pady=12)
    else:
        btnTest = CTkButton(frame, text="📝 Realizar Test", font=('Helvetica', 16), border_color="Green",
                            fg_color="#222", hover_color="Green", text_color="white",
                            corner_radius=20, border_width=2, height=50, width=280, command=lambda: testVentana(ventanaMenu))
        btnTest.grid(columnspan=2, row=3, padx=20, pady=12)

    # Botón de cerrar sesión
    btnCerrarSesion = CTkButton(frame, text="🚪 Cerrar Sesión", font=('Helvetica', 14), border_color="#D50000",
                                fg_color="#222", hover_color="#D50000", text_color="white",
                                corner_radius=20, border_width=2, height=50, width=280, command=salir_sesion)
    btnCerrarSesion.grid(columnspan=2,column=0, row=5, sticky='w', padx=20, pady=20)  # Bajamos el botón un poco

  
def volver_a_menu():
    global ventanaPerfil  # Asegura que accedemos a la ventana correcta
    ventanaPerfil.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu

def Perfil():
    global ventanaPerfil, ventanaMenu, usuario_logueado

    ventanaMenu.destroy()

    ventanaPerfil = CTkToplevel(root)
    ventanaPerfil.state('zoomed')
    ventanaPerfil.minsize(480, 500)
    ventanaPerfil.config(bg="black")
    ventanaPerfil.title("Perfil del usuario")

    frame = CTkFrame(ventanaPerfil, fg_color="#222222", corner_radius=15)
    frame.pack(pady=30, padx=50, fill="both", expand=True)

    label_font_title = ('Arial', 18, 'bold')
    label_font_data = ('Arial', 14)

    titulo = CTkLabel(frame, text="Perfil de Usuario", font=('Arial', 24, 'bold'), text_color="white")
    titulo.pack(pady=20)

    if usuario_logueado.get("admin", False):
        datos_frame = CTkFrame(frame, fg_color="transparent")
        datos_frame.pack(pady=10)

        datos_usuario = [
            ("Admin", usuario_logueado['admin']),
            ("Cedula", usuario_logueado['id']),
            ("Nombre", usuario_logueado['nombre']),
            ("Apellido", usuario_logueado['apellido']),
            ("Correo", usuario_logueado['correo']),
            ("Dirección", usuario_logueado['direccion']),
            ("Estrato", usuario_logueado['estrato']),
            ("Celular", usuario_logueado['celular'])
        ]

        for i, (campo, valor) in enumerate(datos_usuario):
            CTkLabel(datos_frame, text=f"{campo}:", font=label_font_title, text_color="white").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            CTkLabel(datos_frame, text=valor, font=label_font_data, text_color="#cccccc").grid(row=i, column=1, sticky="w", padx=10, pady=5)

    else:
        contenido_frame = CTkFrame(frame, fg_color="transparent")
        contenido_frame.pack(padx=20, pady=10, fill="both", expand=True)

        contenido_frame.grid_columnconfigure(0, weight=1)
        contenido_frame.grid_columnconfigure(1, weight=1)

        # Frame IZQUIERDO - datos del usuario
        datos_frame = CTkFrame(contenido_frame, fg_color="transparent")
        datos_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 30), pady=10)

        datos_usuario = [
            ("Cedula", usuario_logueado['id']),
            ("Nombre", usuario_logueado['nombre']),
            ("Apellido", usuario_logueado['apellido']),
            ("Correo", usuario_logueado['correo']),
            ("Dirección", usuario_logueado['direccion']),
            ("Estrato", usuario_logueado['estrato']),
            ("Celular", usuario_logueado['celular'])
        ]

        for i, (campo, valor) in enumerate(datos_usuario):
            CTkLabel(datos_frame, text=f"{campo}:", font=label_font_title, text_color="white").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            CTkLabel(datos_frame, text=valor, font=label_font_data, text_color="#cccccc").grid(row=i, column=1, sticky="w", padx=10, pady=5)

        # Frame DERECHO - gráfico del usuario
        grafico_frame = CTkFrame(contenido_frame, fg_color="white")
        grafico_frame.grid(row=0, column=1, sticky="nsew", padx=(30, 10), pady=10)

        

        user_id = usuario_logueado.get("id")
        graficos_path = os.path.join(os.getcwd(), "graficos")
        imagen_usuario = None

        if user_id:
            for archivo in os.listdir(graficos_path):
                if user_id in archivo:
                    imagen_usuario = os.path.join(graficos_path, archivo)
                    break

        if imagen_usuario:
            img = Image.open(imagen_usuario)
            img = img.resize((350, 350))
            img_tk = ImageTk.PhotoImage(img)
            label_img = CTkLabel(grafico_frame, image=img_tk, text="")
            label_img.image = img_tk
            label_img.pack(pady=20)
        else:
            CTkLabel(grafico_frame, text="No se ha realizado el Test.", text_color="black").pack(pady=20)

    CTkButton(frame, font=('Arial', 14), border_color="red", fg_color="black",
              hover_color="red", corner_radius=12, border_width=2, text="VOLVER",
              height=40, width=120, command=volver_a_menu).pack(pady=20)



def volver_a_menudtest():
    global ventanaTest  # Asegura que accedemos a la ventana correcta
    ventanaTest.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu

def testVentana(parent=None):

    global ventanaTest
    if parent:
        parent.destroy()

    # Obtener las preguntas desde Firestore
    preguntas = obtener_preguntas()

    ventanaTest = CTkToplevel(root)
    ventanaTest.state('zoomed')
    ventanaTest.minsize(480, 500)
    ventanaTest.config(bg="black")
    ventanaTest.title("Test Vocacional")

    frame = CTkScrollableFrame(ventanaTest, fg_color="white")
    frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
    titulo = CTkLabel(frame, text="Test Vocacional", font=('sans serif', 24), text_color="black")
    titulo.grid(columnspan=2, row=0, padx=4, pady=20)

    respuestas = {i: 'No' for i in range(len(preguntas))}
    variables_checkboxes = {}

    def toggle_response(i):
        respuestas[i] = 'Si' if variables_checkboxes[i].get() else 'No'

    for i, datos in preguntas.items():
        texto_pregunta = datos["texto"]
        fila = i * 2
        CTkLabel(frame, text=texto_pregunta, font=('sans serif', 20)).grid(column=0, row=fila+1, padx=4, pady=4, sticky='w')
        variables_checkboxes[i] = IntVar(value=0)
        checkbox = CTkCheckBox(frame, text="", variable=variables_checkboxes[i], command=lambda i=i: toggle_response(i))
        checkbox.grid(column=1, row=fila+1, padx=50, pady=4, sticky='e')


    def graficar_respuestas():
        categoria_respuestas = {}

        for i, datos in preguntas.items():
            categoria = datos["categoria"]
            if respuestas.get(i) == 'Si':
                categoria_respuestas[categoria] = categoria_respuestas.get(categoria, 0) + 1

        if not categoria_respuestas:
            return [], None

        fig, ax = plt.subplots(figsize=(3.5, 3.5), dpi=100)
        colors = plt.cm.Set3.colors

        wedges, texts, autotexts = ax.pie(
            categoria_respuestas.values(),
            labels=categoria_respuestas.keys(),
            autopct='%1.1f%%',
            startangle=90,
            colors=colors
        )

        for text in texts + autotexts:
            text.set_fontsize(5.5)

        fig.tight_layout(pad=0)

        # Guardar la imagen local
        # Asegurarte de que la carpeta exista
        carpeta_graficos = "graficos"
        os.makedirs(carpeta_graficos, exist_ok=True)

        nombre_archivo = os.path.join(carpeta_graficos, f"grafico_{usuario_logueado.get("id")}.png")
        fig.savefig(nombre_archivo, bbox_inches='tight')

        # Subir a Imgur
        with open(nombre_archivo, "rb") as image_file:
            imgur_response = requests.post(
                url="https://api.imgur.com/3/upload",
                headers={"Authorization": "Client-ID c083ffd0a8101e0"},  # Reemplaza por tu ID
                files={"image": image_file}
            )
        
        # Eliminar el archivo después de subir
        #if os.path.exists(nombre_archivo):
            #os.remove(nombre_archivo)

        if imgur_response.status_code == 200:
            url_imagen = imgur_response.json()["data"]["link"]
        else:
            url_imagen = "Error al subir imagen"

        # Guardar en Firestore
        if 'usuario_logueado' in globals():
            user_id = usuario_logueado.get("id")
            if user_id:
                db.collection('resultados').document(user_id).set({
                    'usuario_id': user_id,
                    'fecha': datetime.now().isoformat(),
                    'carreras_sugeridas': list(categoria_respuestas.keys()),
                    'grafico_url': url_imagen,
                    
                })

        return list(categoria_respuestas.keys()), fig

    def mostrar_grafico(fig, chart_frame):
        for widget in chart_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=0, padx=150, pady=10)
    



    def enviar_datos():
        if all(resp == 'No' for resp in respuestas.values()):
            messagebox.showwarning(
            "Sin respuestas afirmativas",
            "Debes seleccionar al menos una respuesta afirmativa para generar resultados."
        )
        
        elif len(respuestas) == len(preguntas):
            global vocacion_recomendada
            respuestas_estudiante = {i + 1: respuestas[i] for i in range(len(preguntas))}
            vocacion_recomendada = orientar(respuestas_estudiante)

            carreras_mostradas, figura = graficar_respuestas()

             


            ventanaTest.destroy()
            chart_frame = Resultado(carreras_mostradas)
            if figura:
                mostrar_grafico(figura, chart_frame)
 

    btnVocacion = CTkButton(
        frame, font=('sans serif', 12), border_color="green", fg_color="black",
        hover_color="green", corner_radius=12, border_width=2, text="Terminar test",
        height=40, command=enviar_datos)

    btnVocacion.grid(columnspan=2, row=len(preguntas) * 2, padx=4, pady=4)
    btnVolvermen = CTkButton(
        frame, font=('sans serif', 12), border_color="green", fg_color="black",
        hover_color="red", corner_radius=12, border_width=2, text="regresar",
        height=40, command=volver_a_menudtest)

    btnVolvermen.grid(columnspan=2, row=len(preguntas) * 2, padx=50, pady=4,sticky="e")

    ventanaTest.columnconfigure(0, weight=1)
    ventanaTest.rowconfigure(0, weight=1)

    

    ventanaTest.mainloop()

def cerrarYMenu():
    global ventanaResultado  # Asegura que accedemos a la ventana correcta
    ventanaResultado.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu

def Resultado(carreras_mostradas):
    global ventanaResultado
    ventanaResultado = CTkToplevel(root)
    ventanaResultado.state('zoomed')
    ventanaResultado.minsize(800, 600)
    ventanaResultado.title("Resultados")
    ventanaResultado.configure(bg="white")

    carreras_data = obtener_carreras()
    nombres_carreras = [c for c in carreras_mostradas if c in carreras_data]

    frame = CTkFrame(ventanaResultado, fg_color="white")
    frame.pack(expand=True, fill='both', padx=20, pady=20)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    for i in range(10):
        frame.grid_rowconfigure(i, weight=1)

    CTkLabel(frame, text="Resultados", font=("Arial", 24), text_color="black").grid(row=0, column=0, columnspan=2, pady=10)
    CTkLabel(frame, text="Los resultados de su test son los siguientes", font=("Arial", 14), text_color="black").grid(row=1, column=0, columnspan=2)

    chart_frame = CTkFrame(frame, fg_color="white")
    chart_frame.grid(row=2, column=0, rowspan=6, padx=10, pady=10, sticky="nsew")

    info_frame = CTkScrollableFrame(frame, fg_color="white", width=400, height=400)
    info_frame.grid(row=2, column=1, rowspan=6, padx=10, pady=10, sticky="nsew")

    CTkLabel(info_frame, text="Descripción:", font=("Arial", 14, "bold"), text_color="black").pack(anchor="w", padx=(50,50),pady=(0, 5))
    descripcion_label = CTkLabel(info_frame, text="", text_color="black", wraplength=350, justify="left")
    descripcion_label.pack(anchor="w", padx=(50,50), pady=(0, 20))

    CTkLabel(info_frame, text="Campo laboral:", font=("Arial", 14, "bold"), text_color="black").pack(anchor="w", padx=(50,50), pady=(0, 5))
    campo_laboral_label = CTkLabel(info_frame, text="", text_color="black", wraplength=350, justify="left")
    campo_laboral_label.pack(anchor="w", padx=(50,50), pady=(0, 20))

    def actualizar_informacion(carrera):
        info = carreras_data.get(carrera, {})
        campo_laboral_label.configure(text=info.get("campo_laboral", "Sin info"))
        descripcion_label.configure(text=info.get("descripcion", "Sin descripción"))

    combo = CTkOptionMenu(frame, values=nombres_carreras, command=actualizar_informacion)
    combo.grid(row=8, column=0, padx=10, pady=10, sticky="w")

    if nombres_carreras:
        combo.set(nombres_carreras[0])
        actualizar_informacion(nombres_carreras[0])

    CTkButton(frame, text="Volver a la pantalla de inicio de sesión", command=cerrarYMenu).grid(row=8, column=1, pady=20, sticky="e", padx=20)

    return chart_frame

def error():
    global err
    err = CTkToplevel()
    err.title("Error")
    err.geometry("500x100+350+20")
    err.minsize(480, 500)
    err.config(bg="white")
    err.title("Registro")
    
    # Asegura que la ventana emergente se quede al frente
    err.grab_set()
    err.lift()
    err.focus_force()

    CTkLabel(err, text="Todos los campos son necesarios..", fg_color="red", font=('sans rerif', 12)).grid(column=0, row=0, padx=50, pady=50)
    CTkLabel(err, text="").grid(column=1, row=0, padx=50, pady=50)
    CTkButton(err, font=('sans rerif', 12), text="Ok", bg="grey", width=8, height=1, command=err.destroy).grid(column=2, row=0, padx=50, pady=50)


def errorLogin(message):
    global err
    err = CTkToplevel()
    err.title("Error")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg="white")
    err.title("Registro")
    
    # Asegura que la ventana emergente se quede al frente
    err.grab_set()
    err.lift()
    err.focus_force()

    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="red", fg_color="black",
               hover_color="red", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack(pady=10)


def LoginCorrecto(message):
    global err
    err = CTkToplevel()
    err.title("Exito")
    err.geometry("100x100")
    err.minsize(300, 100)
    err.config(bg="white")
    err.title("Registro")
    
    # Asegura que la ventana emergente se quede al frente
    err.grab_set()
    err.lift()
    err.focus_force()

    CTkLabel(err, text=message, font=('sans rerif', 12)).pack()
    CTkButton(err, font=('sans rerif', 12), border_color="green", fg_color="black",
               hover_color="green", corner_radius=12, border_width=2, text="Ok", height=40, command=err.destroy).pack()




def loginUsuario():
    global usuario_logueado  # Declarar como global para almacenar el usuario
    usuario1 = usuarioEntry.get().lower()  # Obtiene el correo ingresado
    clave1 = password.get()        # Obtiene la contraseña ingresada

    # Verifica que los campos no estén vacíos
    if usuario1 == "" or clave1 == "":
        errorLogin("Tiene que llenar los datos solicitados...")
    else:
        if es_correo_valido(usuario1):
            usuarios_ref = db.collection('usuarios')
            query = usuarios_ref.where(filter=FieldFilter('correo', '==', usuario1)).get()

            if query:  # Si hay resultados (el correo está registrado)
                usuario_doc = query[0]
                datos = usuario_doc.to_dict()
                contraseña_db = datos.get('contraseña')

                if clave1 == contraseña_db:
                    usuario_logueado = datos
                    usuarioEntry.delete(0, END)
                    password.delete(0, END)
                    menu()  # Abre el menú
                else:
                    errorLogin("Contraseña incorrecta")
                    password.delete(0, END)
            else:
                errorLogin("El correo no está registrado")
                usuarioEntry.delete(0, END)
                password.delete(0, END)
        else:
            errorLogin("Ingrese un correo válido")
            usuarioEntry.delete(0, END)


def es_correo_valido(correop):
    # Expresión regular para validar un correo electrónico
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correop) is not None
        
def inserta_datos():
    admin = admin.get()
    id = idRegistro.get()
    nombre = nombreRegistro.get()
    apellido = apellidoRegistro.get()
    correo = correoRegistro.get()
    clave = passwordRegistro.get()
    direccion = direccionRegistro.get()
    estrato = estratoRegistro.get()
    celular = celularRegistro.get()

    if id == "" or nombre == "" or apellido == "" or correo == "" or clave == "" or direccion == "" or estrato == "" or celular == "":
        errorLogin("Ingrese los datos solicitados")
    else:
        if es_correo_valido(correo):
            # Verificar si el usuario ya existe
            usuarios_ref = db.collection('usuarios')
            query = usuarios_ref.where(filter=FieldFilter('correo', '==', correo)).get()

            if query:  # Si la lista no está vacía, el usuario ya existe
                errorLogin("El usuario ya existe")
            else:
                nuevo_usuario = {
                    'id': id,
                    'nombre': nombre,
                    'apellido': apellido,
                    'correo': correo,
                    'contraseña': clave,
                    'direccion': direccion,
                    'estrato': estrato,
                    'celular': celular
                }

                try:
                    db.collection('usuarios').document(id).set(nuevo_usuario)
                    #db.collection('usuarios').add(nuevo_usuario)

                    # Limpiar los campos
                    idRegistro.delete(0, END)
                    nombreRegistro.delete(0, END)
                    apellidoRegistro.delete(0, END)
                    correoRegistro.delete(0, END)
                    passwordRegistro.delete(0, END)
                    direccionRegistro.delete(0, END)
                    estratoRegistro.delete(0, END)
                    celularRegistro.delete(0, END)

                    LoginCorrecto("Se realizó correctamente el registro")

                except Exception as e:
                    errorLogin(f"Error al registrar usuario: {e}")

                    # También puedes limpiar los campos si deseas
                    idRegistro.delete(0, END)
                    nombreRegistro.delete(0, END)
                    apellidoRegistro.delete(0, END)
                    correoRegistro.delete(0, END)
                    passwordRegistro.delete(0, END)
                    direccionRegistro.delete(0, END)
                    estratoRegistro.delete(0, END)
                    celularRegistro.delete(0, END)
        else:
            errorLogin("Ingrese un correo válido")



def volver_a_menu_adminu():
    global ventana_admin  # Asegura que accedemos a la ventana correcta
    ventana_admin.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu

def abrir_admin_usuarios():
    global ventana_admin, tabla_usuarios, ventanaMenu

    if ventanaMenu:
        ventanaMenu.destroy()
        ventanaMenu = None  

    ventana_admin = CTkToplevel(root)
    ventana_admin.state('zoomed')  
    ventana_admin.title("Administrar Usuarios")

    # Marco principal
    frame_admin = CTkFrame(ventana_admin, fg_color="white")
    frame_admin.pack(padx=20, pady=20, fill='both', expand=True)

    # Título
    titulo = CTkLabel(frame_admin, text="Administración de Usuarios", font=('Helvetica', 20, 'bold'))
    titulo.pack(pady=10)

    # Marco para los botones
    frame_botones = CTkFrame(frame_admin, fg_color="white")
    frame_botones.pack(pady=10)

    # Botones alineados
    btn_agregar = CTkButton(frame_botones, text="➕ Agregar Usuario", command=agregar_usuario)
    btn_agregar.grid(row=0, column=0, padx=5)

    btn_editar = CTkButton(frame_botones, text="✏️ Editar Usuario", command=editar_usuario)
    btn_editar.grid(row=0, column=1, padx=5)

    btn_eliminar = CTkButton(frame_botones, text="🗑️ Eliminar Usuario", command=eliminar_usuario)
    btn_eliminar.grid(row=0, column=2, padx=5)

    btn_regresar = CTkButton(frame_botones, text=" Regresar", command=volver_a_menu_adminu)
    btn_regresar.grid(row=0, column=5,sticky='e', padx=5)


    # Marco para la tabla
    frame_tabla = CTkFrame(frame_admin, fg_color="white")
    frame_tabla.pack(pady=10, fill="both", expand=True)

    columnas = ("ID", "Nombre", "Correo", "Contraseña", "Direccion", "Estrato", "Celular", "Admin")

    # Crear tabla (Treeview)
    tabla_usuarios = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

    # Encabezados
    tabla_usuarios.heading("ID", text="ID")
    tabla_usuarios.heading("Nombre", text="Nombre")
    tabla_usuarios.heading("Correo", text="Correo Electrónico")
    tabla_usuarios.heading("Contraseña", text="Contraseña")
    tabla_usuarios.heading("Direccion", text="Direccion")
    tabla_usuarios.heading("Estrato", text="Estrato")
    tabla_usuarios.heading("Celular", text="Celular")
    tabla_usuarios.heading("Admin", text="Administrador")

    # Ajustar tamaño de columnas
    tabla_usuarios.column("ID", width=50, anchor="center")
    tabla_usuarios.column("Nombre", width=100, anchor="w")
    tabla_usuarios.column("Correo", width=120, anchor="w")
    tabla_usuarios.column("Contraseña", width=100, anchor="center")
    tabla_usuarios.column("Direccion", width=120, anchor="center")
    tabla_usuarios.column("Estrato", width=50, anchor="center")
    tabla_usuarios.column("Celular", width=100, anchor="center")
    tabla_usuarios.column("Admin", width=50, anchor="center")

    # Agregar barra de desplazamiento
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla_usuarios.yview)
    tabla_usuarios.configure(yscrollcommand=scrollbar.set)

    tabla_usuarios.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Cargar usuarios en la tabla
    cargar_usuarios()

def cargar_usuarios():
    global tabla_usuarios

    # Si la tabla ya está creada, limpiarla antes de actualizar
    if tabla_usuarios:
        for row in tabla_usuarios.get_children():
            tabla_usuarios.delete(row)

    usuarios = db.collection('usuarios').get()
    for usuario in usuarios:
        data = usuario.to_dict()
        tabla_usuarios.insert("", "end", values=(
            data['id'],
            f"{data['nombre']} {data['apellido']}",
            data['correo'],
            data['contraseña'],
            data['direccion'],
            data['estrato'],
            data['celular'],
            "Sí" if data.get('admin', False) else "No"
        ))

def agregar_usuario():
    ventana_add = CTkToplevel(root)
    ventana_add.title("Agregar Usuario")
    ventana_add.geometry("400x680")

    ventana_add.transient(ventana_admin)
    ventana_add.grab_set()
    ventana_add.focus_force()

    contenedor_scroll = CTkFrame(ventana_add, fg_color="white")
    contenedor_scroll.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor_scroll, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_interno = CTkFrame(canvas, fg_color="white")
    ventana_canvas = canvas.create_window((0, 0), window=frame_interno, anchor="n")

    def configurar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(ventana_canvas, width=canvas.winfo_width())

    frame_interno.bind("<Configure>", configurar_scroll)

    CTkLabel(frame_interno, text="Nuevo Usuario", font=('Helvetica', 18, 'bold'), anchor="center", justify="center").pack(pady=10)

    campos = ["ID", "Nombre", "Apellido", "Correo", "Contraseña", "Direccion", "Estrato", "Celular"]
    entradas = {}

    for campo in campos:
        CTkLabel(frame_interno, text=campo, font=('Helvetica', 12), anchor="center", justify="center").pack()
        entrada = CTkEntry(frame_interno, justify="center")
        entrada.pack(pady=5)
        entradas[campo.lower()] = entrada

    admin_var = tk.BooleanVar()
    checkbox_admin = CTkCheckBox(frame_interno, text="Administrador", variable=admin_var)
    checkbox_admin.pack(pady=10)

    def guardar_usuario():
        nuevo_usuario = {k: v.get().strip() for k, v in entradas.items()}
        nuevo_usuario["admin"] = admin_var.get()

        # Validar campos vacíos
        if any(valor == "" for clave, valor in nuevo_usuario.items() if clave != "admin"):
            CTkMessagebox(title="Campos vacíos", message="Por favor, completa todos los campos.", icon="warning")
            return

        # Validar si el ID ya existe
        doc_ref = db.collection('usuarios').document(nuevo_usuario['id']).get()
        if doc_ref.exists:
            CTkMessagebox(title="ID existente", message="Ya existe un usuario con ese ID.", icon="cancel")
            return

        # Guardar en Firestore
        try:
            db.collection('usuarios').document(nuevo_usuario['id']).set(nuevo_usuario)
            CTkMessagebox(title="Éxito", message="Usuario guardado exitosamente.", icon="check")
            ventana_add.destroy()
            cargar_usuarios()
        except Exception as e:
            CTkMessagebox(title="Error", message=f"No se pudo guardar el usuario: {e}", icon="cancel")

    btn_guardar = CTkButton(frame_interno, text="Guardar", command=guardar_usuario)
    btn_guardar.pack(pady=10)

    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    def scroll_start(event):
        canvas.scan_mark(event.x, event.y)

    def scroll_move(event):
        canvas.scan_dragto(event.x, event.y, gain=1)

    canvas.bind("<ButtonPress-1>", scroll_start)
    canvas.bind("<B1-Motion>", scroll_move)


def editar_usuario():
    ventana_edit = CTkToplevel(root)
    ventana_edit.title("Editar Usuario")
    ventana_edit.geometry("400x680")

    ventana_edit.transient(ventana_admin)
    ventana_edit.grab_set()
    ventana_edit.focus_force()

    contenedor_scroll = CTkFrame(ventana_edit, fg_color="white")
    contenedor_scroll.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor_scroll, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_interno = CTkFrame(canvas, fg_color="white")
    ventana_canvas = canvas.create_window((0, 0), window=frame_interno, anchor="n")

    def configurar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.itemconfig(ventana_canvas, width=canvas.winfo_width())

    frame_interno.bind("<Configure>", configurar_scroll)

    CTkLabel(frame_interno, text="Editar Usuario", font=('Helvetica', 18, 'bold'), anchor="center", justify="center").pack(pady=10)

    CTkLabel(frame_interno, text="ID del Usuario a Editar:", font=('Helvetica', 12), anchor="center", justify="center").pack()
    entry_id = CTkEntry(frame_interno, justify="center")
    entry_id.pack(pady=5)

    campos = ["Nombre", "Apellido", "Correo", "Contraseña", "Direccion", "Estrato", "Celular"]
    entradas = {}

    for campo in campos:
        CTkLabel(frame_interno, text=campo, font=('Helvetica', 12), anchor="center", justify="center").pack()
        entrada = CTkEntry(frame_interno, justify="center")
        entrada.pack(pady=5)
        entradas[campo.lower()] = entrada

    admin_var = tk.BooleanVar()
    checkbox_admin = CTkCheckBox(frame_interno, text="Administrador", variable=admin_var)
    checkbox_admin.pack(pady=10)

    def cargar_datos_usuario(event=None):
        user_id = entry_id.get()
        if not user_id:
            return
        usuario_ref = db.collection('usuarios').document(user_id).get()
        if usuario_ref.exists:
            data = usuario_ref.to_dict()
            for k in entradas:
                entradas[k].delete(0, "end")
                entradas[k].insert(0, data.get(k, ""))
            admin_var.set(data.get("admin", False))
        else:
            CTkMessagebox(title="Error", message="Usuario no encontrado", icon="cancel")

    entry_id.bind("<FocusOut>", cargar_datos_usuario)
    entry_id.bind("<Return>", cargar_datos_usuario)

    def actualizar_usuario():
        user_id = entry_id.get()
        if not user_id:
            CTkMessagebox(title="Advertencia", message="Debes ingresar un ID válido.", icon="warning")
            return
        usuario_ref = db.collection('usuarios').document(user_id)
        data_actualizada = {k: v.get() for k, v in entradas.items() if v.get()}
        data_actualizada["admin"] = admin_var.get()
        try:
            usuario_ref.update(data_actualizada)
            CTkMessagebox(title="Éxito", message="Usuario actualizado correctamente", icon="check")
            ventana_edit.destroy()
            cargar_usuarios()
        except Exception as e:
            CTkMessagebox(title="Error", message=f"No se pudo actualizar: {e}", icon="cancel")

    btn_actualizar = CTkButton(frame_interno, text="Actualizar", command=actualizar_usuario)
    btn_actualizar.pack(pady=10)

    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    def scroll_start(event):
        canvas.scan_mark(event.x, event.y)

    def scroll_move(event):
        canvas.scan_dragto(event.x, event.y, gain=1)

    canvas.bind("<ButtonPress-1>", scroll_start)
    canvas.bind("<B1-Motion>", scroll_move)




def eliminar_usuario():
    ventana_del = CTkToplevel(root)
    ventana_del.title("Eliminar Usuario")
    ventana_del.geometry("300x200")

    ventana_del.transient(ventana_admin)
    ventana_del.grab_set()
    ventana_del.focus_force()

    frame_del = CTkFrame(ventana_del, fg_color="white")
    frame_del.pack(padx=20, pady=20, fill='both', expand=True)

    CTkLabel(frame_del, text="Eliminar Usuario", font=('Helvetica', 18, 'bold')).pack(pady=10)

    CTkLabel(frame_del, text="ID del Usuario:", font=('Helvetica', 12)).pack()
    entry_id = CTkEntry(frame_del)
    entry_id.pack(pady=5)

    def confirmar_eliminar():
        user_id = entry_id.get().strip()

        if not user_id:
            CTkMessagebox(title="Campo vacío", message="Por favor ingresa un ID.", icon="warning")
            return

        usuario_ref = db.collection('usuarios').document(user_id)
        usuario = usuario_ref.get()

        if not usuario.exists:
            CTkMessagebox(title="ID no encontrado", message="No existe un usuario con ese ID.", icon="cancel")
            return

        # Confirmación antes de eliminar
        confirm = CTkMessagebox(
            title="Confirmar eliminación",
            message=f"¿Estás seguro de que deseas eliminar al usuario con ID '{user_id}'?",
            icon="warning",
            option_1="Sí",
            option_2="No"
        )

        if confirm.get() == "Sí":
            try:
                usuario_ref.delete()
                CTkMessagebox(title="Eliminado", message="Usuario eliminado exitosamente.", icon="check")
                ventana_del.destroy()
                cargar_usuarios()
            except Exception as e:
                CTkMessagebox(title="Error", message=f"No se pudo eliminar el usuario: {e}", icon="cancel")

    btn_eliminar = CTkButton(frame_del, text="Eliminar", command=confirmar_eliminar)
    btn_eliminar.pack(pady=10)



   

def volver_a_menu_adminp():
    global ventana_admin_preguntas # Asegura que accedemos a la ventana correcta
    ventana_admin_preguntas.destroy()  # Cierra la ventana del menú
    menu()  # Muestra nuevamente la ventana menu


def abrir_admin_preguntas():
    global ventana_admin_preguntas, tabla_preguntas, ventanaMenu

    if ventanaMenu:
        ventanaMenu.destroy()
        ventanaMenu = None  

    ventana_admin_preguntas = CTkToplevel(root)
    ventana_admin_preguntas.state('zoomed')  
    ventana_admin_preguntas.title("Administrar Preguntas del Test")

    frame_admin = CTkFrame(ventana_admin_preguntas, fg_color="white")
    frame_admin.pack(padx=20, pady=20, fill='both', expand=True)

    titulo = CTkLabel(frame_admin, text="Administración de Preguntas del Test", font=('Helvetica', 20, 'bold'))
    titulo.pack(pady=10)

    frame_botones = CTkFrame(frame_admin, fg_color="white")
    frame_botones.pack(pady=10)

    btn_agregar = CTkButton(frame_botones, text="➕ Agregar Pregunta", command=agregar_pregunta)
    btn_agregar.grid(row=0, column=0, padx=5)

    btn_editar = CTkButton(frame_botones, text="✏️ Editar Pregunta", command=editar_pregunta)
    btn_editar.grid(row=0, column=1, padx=5)

    btn_eliminar = CTkButton(frame_botones, text="🗑️ Eliminar Pregunta", command=eliminar_pregunta)
    btn_eliminar.grid(row=0, column=2, padx=5)

    btn_regresar = CTkButton(frame_botones, text=" Regresar", command=volver_a_menu_adminp)
    btn_regresar.grid(row=0, column=5, sticky='e', padx=5)

    frame_tabla = CTkFrame(frame_admin, fg_color="white")
    frame_tabla.pack(pady=10, fill="both", expand=True)

    columnas = ("ID", "Pregunta", "Categoria")
    
    tabla_preguntas = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

    for col in columnas:
        tabla_preguntas.heading(col, text=col)
        tabla_preguntas.column(col, width=100, anchor="center")

    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla_preguntas.yview)
    tabla_preguntas.configure(yscrollcommand=scrollbar.set)

    tabla_preguntas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    cargar_preguntas()

def cargar_preguntas():
    for row in tabla_preguntas.get_children():
        tabla_preguntas.delete(row)

    preguntas = db.collection('preguntas').get()
    for pregunta in preguntas:
        data = pregunta.to_dict()
        tabla_preguntas.insert("", "end", values=(data['id'], data['texto'], data['categoria']))

def agregar_pregunta():
    ventana_add = CTkToplevel(root)
    ventana_add.title("Agregar Pregunta")
    ventana_add.geometry("400x500")

    ventana_add.transient(ventana_admin_preguntas)
    ventana_add.grab_set()
    ventana_add.focus_force()

    frame_add = CTkFrame(ventana_add, fg_color="white")
    frame_add.pack(padx=20, pady=20, fill='both', expand=True)

    CTkLabel(frame_add, text="Nueva Pregunta", font=('Helvetica', 18, 'bold')).pack(pady=10)

    entradas = {}

    # Campo ID
    CTkLabel(frame_add, text="ID", font=('Helvetica', 12)).pack()
    entry_id = CTkEntry(frame_add)
    entry_id.pack(pady=5)
    entradas["id"] = entry_id

    # Campo Texto (más grande con CTkTextbox)
    CTkLabel(frame_add, text="Texto", font=('Helvetica', 12)).pack()
    entry_texto = CTkTextbox(frame_add, height=100)  # Altura mayor
    entry_texto.pack(pady=5)
    entradas["texto"] = entry_texto

    # Campo Categoría
    CTkLabel(frame_add, text="Categoria", font=('Helvetica', 12)).pack()
    entry_categoria = CTkTextbox(frame_add, height=100)
    entry_categoria.pack(pady=5)
    entradas["categoria"] = entry_categoria

    def guardar_pregunta():
        nueva_pregunta = {
            "id": entradas["id"].get().strip(),
            "texto": entradas["texto"].get("1.0", "end").strip(),  # Obtener texto desde el CTkTextbox
            "categoria": entradas["categoria"].get().strip()
        }

        if any(not valor for valor in nueva_pregunta.values()):
            CTkMessagebox(title="Campos vacíos", message="Por favor completa todos los campos.", icon="warning")
            return

        pregunta_ref = db.collection('preguntas').document(nueva_pregunta['id'])
        if pregunta_ref.get().exists:
            CTkMessagebox(title="ID existente", message="Ya existe una pregunta con ese ID.", icon="cancel")
            return

        try:
            pregunta_ref.set(nueva_pregunta)
            CTkMessagebox(title="Guardado", message="Pregunta agregada exitosamente.", icon="check")
            ventana_add.destroy()
            cargar_preguntas()
        except Exception as e:
            CTkMessagebox(title="Error", message=f"No se pudo guardar la pregunta: {e}", icon="cancel")

    btn_guardar = CTkButton(frame_add, text="Guardar", command=guardar_pregunta)
    btn_guardar.pack(pady=10)



def editar_pregunta():
    ventana_edit = CTkToplevel(root)
    ventana_edit.title("Editar Pregunta")
    ventana_edit.geometry("400x500")

    ventana_edit.transient(ventana_admin_preguntas)
    ventana_edit.grab_set()
    ventana_edit.focus_force()

    frame_edit = CTkFrame(ventana_edit, fg_color="white")
    frame_edit.pack(padx=20, pady=20, fill='both', expand=True)

    CTkLabel(frame_edit, text="Editar Pregunta", font=('Helvetica', 18, 'bold')).pack(pady=10)

    CTkLabel(frame_edit, text="ID de la Pregunta a Editar:", font=('Helvetica', 12)).pack()
    entry_id = CTkEntry(frame_edit)
    entry_id.pack(pady=5)

    entradas = {}

    # Campo Texto ampliado
    CTkLabel(frame_edit, text="Texto", font=('Helvetica', 12)).pack()
    entry_texto = CTkTextbox(frame_edit, height=100)
    entry_texto.pack(pady=5)
    entradas["texto"] = entry_texto

    # Campo Categoría normal
    CTkLabel(frame_edit, text="Categoria", font=('Helvetica', 12)).pack()
    entry_categoria = CTkTextbox(frame_edit, height=100)
    entry_categoria.pack(pady=5)
    entradas["categoria"] = entry_categoria

    # Función para cargar datos si el ID existe
    def cargar_datos_pregunta(event):
        pregunta_id = entry_id.get().strip()
        if not pregunta_id:
            return
        pregunta_ref = db.collection('preguntas').document(pregunta_id)
        doc = pregunta_ref.get()
        if doc.exists:
            data = doc.to_dict()
            entry_texto.delete("1.0", "end")
            entry_texto.insert("1.0", data.get("texto", ""))
            entry_categoria.delete(0, "end")
            entry_categoria.insert(0, data.get("categoria", ""))
        else:
            CTkMessagebox(title="No encontrado", message="No existe una pregunta con ese ID.", icon="warning")

    entry_id.bind("<Return>", cargar_datos_pregunta)

    def actualizar_pregunta():
        pregunta_id = entry_id.get().strip()
        nuevo_texto = entry_texto.get("1.0", "end").strip()
        nueva_categoria = entry_categoria.get().strip()

        if not pregunta_id or not nuevo_texto or not nueva_categoria:
            CTkMessagebox(title="Campos vacíos", message="Todos los campos son obligatorios.", icon="warning")
            return

        pregunta_ref = db.collection('preguntas').document(pregunta_id)
        if not pregunta_ref.get().exists:
            CTkMessagebox(title="No encontrado", message="No se encontró una pregunta con ese ID.", icon="cancel")
            return

        try:
            pregunta_ref.update({
                "texto": nuevo_texto,
                "categoria": nueva_categoria
            })
            CTkMessagebox(title="Éxito", message="Pregunta actualizada correctamente.", icon="check")
            ventana_edit.destroy()
            cargar_preguntas()
        except Exception as e:
            CTkMessagebox(title="Error", message=f"No se pudo actualizar la pregunta: {e}", icon="cancel")

    btn_actualizar = CTkButton(frame_edit, text="Actualizar", command=actualizar_pregunta)
    btn_actualizar.pack(pady=10)


def eliminar_pregunta():
    ventana_del = CTkToplevel(root)
    ventana_del.title("Eliminar Pregunta")
    ventana_del.geometry("300x200")

    ventana_del.transient(ventana_admin_preguntas)
    ventana_del.grab_set()
    ventana_del.focus_force()

    frame_del = CTkFrame(ventana_del, fg_color="white")
    frame_del.pack(padx=20, pady=20, fill='both', expand=True)

    CTkLabel(frame_del, text="Eliminar Pregunta", font=('Helvetica', 18, 'bold')).pack(pady=10)

    CTkLabel(frame_del, text="ID de la Pregunta:", font=('Helvetica', 12)).pack()
    entry_id = CTkEntry(frame_del)
    entry_id.pack(pady=5)

    def confirmar_eliminar():
        pregunta_id = entry_id.get().strip()

        if not pregunta_id:
            CTkMessagebox(title="Campo vacío", message="Por favor, ingresa un ID.", icon="warning")
            return

        pregunta_ref = db.collection('preguntas').document(pregunta_id)
        doc = pregunta_ref.get()

        if not doc.exists:
            CTkMessagebox(title="No encontrado", message="No se encontró una pregunta con ese ID.", icon="cancel")
            return

        respuesta = CTkMessagebox(title="Confirmar eliminación", message="¿Estás seguro que deseas eliminar esta pregunta?", icon="question", option_1="Sí", option_2="No")
        
        if respuesta.get() == "Sí":
            try:
                pregunta_ref.delete()
                CTkMessagebox(title="Éxito", message="Pregunta eliminada correctamente.", icon="check")
                ventana_del.destroy()
                cargar_preguntas()
            except Exception as e:
                CTkMessagebox(title="Error", message=f"No se pudo eliminar la pregunta: {e}", icon="cancel")

    btn_eliminar = CTkButton(frame_del, text="Eliminar", command=confirmar_eliminar)
    btn_eliminar.pack(pady=10)


#menu()
#testVentana(parent=None)
ventanaInicio()




