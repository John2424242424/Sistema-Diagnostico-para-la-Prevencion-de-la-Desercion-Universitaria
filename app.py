from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    print("¡La función login se está ejecutando!")  # Verifica en consola
    return render_template('login.html')

if __name__ == '__main__':
    # Verifica que la carpeta templates existe
    if not os.path.exists('templates'):
        os.makedirs('templates')
        with open('templates/login.html', 'w') as f:
            f.write('<h1>Login funciona!</h1>')
    
    app.run(debug=True, port=5000)