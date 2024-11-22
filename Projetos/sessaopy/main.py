from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para a sessão

# Usuário fictício para demonstração (em uma aplicação real, e para fazer o select para buscar no banco de dados)
USUARIO_EXEMPLO = {
    "email": "usuario@gmail.com",
    "senha_hash": bcrypt.generate_password_hash("123").decode('utf-8')  # Senha criptografada
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se os valores do formulario é igual ao USUARIO_EXEMPLO
        if email == USUARIO_EXEMPLO['email'] and bcrypt.check_password_hash(USUARIO_EXEMPLO['senha_hash'], senha):
            session['usuario_id'] = email  # Armazena o usuário na sessão
            return redirect(url_for('dashboard'))
        else:
            return "Email ou senha incorretos", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)  # Remove o usuário da sessão
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))  # Redireciona para login se não autenticado
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)