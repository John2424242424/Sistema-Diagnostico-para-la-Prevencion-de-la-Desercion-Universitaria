# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from conexion import firebase

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Necesaria para las sesiones

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]  # En producción, usa hashing
        
        try:
            # Verificar usuario (esto es un ejemplo, en producción usa Firebase Client SDK)
            user = firebase.get_auth().get_user_by_email(email)
            
            # Guardar en sesión (simulado)
            session["user"] = {
                "uid": user.uid,
                "email": user.email
            }
            return redirect(url_for("perfil"))
            
        except Exception as e:
            error = f"Error: {str(e)}"
            return render_template("login.html", error=error)
    
    return render_template("login.html")

@app.route("/perfil")
def perfil():
    if not session.get("user"):
        return redirect(url_for("login"))
    
    # Obtener datos adicionales de Firestore usando tu conexión
    user_ref = firebase.db.collection("usuarios").document(session["user"]["uid"])
    user_data = user_ref.get().to_dict()
    
    return render_template("perfil.html", user=session["user"], datos=user_data)

if __name__ == "__main__":
    app.run(debug=True)