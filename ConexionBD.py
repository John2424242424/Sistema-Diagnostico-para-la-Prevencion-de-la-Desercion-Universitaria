import pymysql

def ConnexionBD():
    bd = pymysql.connect(
        host="localhost",
       user="root",
        password="",
        db="sistema_experto"
    )
    return bd


##import sqlite3
##con = sqlite3.connect("archivos/sistema_experto.db")
##cur = con.cursor()

##def tablaExiste(nombreTabla):
    ##cur.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))
    ##if cur.fetchone()[0] == 1:
        ##return True
    ##else:
        ##cur.execute("""
        ##CREATE TABLE usuario(
           ## id INTEGER PRIMARY KEY AUTOINCREMENT, 
           ## nombre TEXT, 
           ## apellido TEXT, 
           ## correo TEXT, 
           ## contraseña TEXT, 
           ## direccion TEXT, 
           ## estrato INTEGER, 
           ## celular TEXT
##        )
  ##  """)
       ## return False

##res = cur.execute("SELECT name FROM sqlite_master")
##res.fetchone()
##tablaExiste('sistema_experto')
