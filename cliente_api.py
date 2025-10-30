print("Script iniciado")  # Adicionado para depuração

from flask import Flask, request, jsonify, render_template_string, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'chave_secreta_cliente'  # Necessário para flash messages

def get_conn():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='sistema',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/', methods=['GET', 'POST'])
def formulario_cliente():
    if request.method == 'POST':
        dados = {
            'empresa': request.form['empresa'],
            'cnpj': request.form['cnpj'],
            'endereco': request.form['endereco'],
            'proprietario': request.form['proprietario'],
            'tipo_licenca': request.form['tipo_licenca']
        }
        try:
            conn = get_conn()
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO solicitacoes (empresa, cnpj, endereco, proprietario, tipo_licenca) VALUES (%s, %s, %s, %s, %s)',
                (dados['empresa'], dados['cnpj'], dados['endereco'], dados['proprietario'], dados['tipo_licenca'])
            )
            conn.commit()
            conn.close()
            flash('Solicitação enviada com sucesso!', 'success')
            return redirect(url_for('formulario_cliente'))
        except Exception as e:
            flash('Erro ao enviar solicitação: ' + str(e), 'danger')
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Nova Solicitação</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f6fb; margin: 0; padding: 0; }
            .container { background: #fff; max-width: 500px; margin: 40px auto; padding: 30px 40px; border-radius: 8px; box-shadow: 0 2px 8px rgba(44,62,80,0.1);}
            h2 { color: #2a5298; text-align: center; margin-bottom: 30px;}
            label { display: block; margin-bottom: 8px; color: #2a5298;}
            input, select { width: 100%; padding: 10px; margin-bottom: 18px; border: 1px solid #bfc9d9; border-radius: 4px; font-size: 15px;}
            button { background: #2a5298; color: #fff; border: none; padding: 12px 28px; border-radius: 5px; font-size: 16px; cursor: pointer; width: 100%; transition: background 0.2s;}
            button:hover { background: #1e3c72;}
            .msg-success { background:#d4edda;color:#155724;padding:10px;border-radius:5px;margin-bottom:10px;}
            .msg-danger { background:#f8d7da;color:#721c24;padding:10px;border-radius:5px;margin-bottom:10px;}
            .link-listar { display: block; text-align: center; margin-top: 18px; color: #2a5298; text-decoration: none;}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Nova Solicitação</h2>
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                {% for category, message in messages %}
                  <div class="msg-{{category}}">{{ message }}</div>
                {% endfor %}
              {% endif %}
            {% endwith %}
            <form method="post">
                <label for="empresa">Empresa</label>
                <input type="text" id="empresa" name="empresa" required>
                <label for="cnpj">CNPJ</label>
                <input type="text" id="cnpj" name="cnpj" required>
                <label for="endereco">Endereço</label>
                <input type="text" id="endereco" name="endereco" required>
                <label for="proprietario">Proprietário</label>
                <input type="text" id="proprietario" name="proprietario" required>
                <label for="tipo_licenca">Tipo de Licença</label>
                <select id="tipo_licenca" name="tipo_licenca" required>
                    <option value="">Selecione...</option>
                    <option value="Licença de Prévia">Licença de Prévia</option>
                    <option value="Licença de Instalação">Licença de Instalação</option>
                    <option value="Licença de Operação">Licença de Operação</option>
                </select>
                <button type="submit">Enviar Solicitação</button>
            </form>
            <a class="link-listar" href="/listar">Ver Solicitações</a>
        </div>
    </body>
    </html>
    """)

@app.route('/listar')
def listar():
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM solicitacoes')
        solicitacoes = cursor.fetchall()
        conn.close()
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Solicitações</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f4f6fb; margin: 0; padding: 0; }
                h1 { background: #2a5298; color: #fff; margin: 0; padding: 20px 0; text-align: center; letter-spacing: 2px;}
                table { margin: 40px auto; border-collapse: collapse; width: 90%; background: #fff; box-shadow: 0 2px 8px rgba(44,62,80,0.1);}
                th, td { padding: 12px 16px; text-align: left;}
                th { background: #2a5298; color: #fff;}
                tr:nth-child(even) { background: #eaf0fb;}
                tr:hover { background: #d0e2ff;}
                .message { width: 90%; margin: 20px auto; padding: 10px; border-radius: 5px; margin-bottom: 10px;}
                .success { background: #d4edda; color: #155724;}
                .danger { background: #f8d7da; color: #721c24;}
                .link-nova { display: block; text-align: center; margin-bottom: 30px; }
                .btn-nova { background: #2a5298; color: #fff; border: none; padding: 12px 28px; border-radius: 5px; font-size: 16px; cursor: pointer; transition: background 0.2s;}
                .btn-nova:hover { background: #1e3c72;}
            </style>
        </head>
        <body>
            <h1>Solicitações</h1>
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                <div style="width:90%;margin:20px auto;">
                  {% for category, message in messages %}
                    <div class="message {{ category }}">
                      {{ message }}
                    </div>
                  {% endfor %}
                </div>
              {% endif %}
            {% endwith %}
            <div class="link-nova">
                <a href="/"><button class="btn-nova">Nova Solicitação</button></a>
            </div>
            {% if solicitacoes and solicitacoes|length > 0 %}
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Empresa</th>
                    <th>CNPJ</th>
                    <th>Endereço</th>
                    <th>Proprietário</th>
                    <th>Tipo Licença</th>
                </tr>
                {% for s in solicitacoes %}
                <tr>
                    <td>{{ s.id }}</td>
                    <td>{{ s.empresa }}</td>
                    <td>{{ s.cnpj }}</td>
                    <td>{{ s.endereco }}</td>
                    <td>{{ s.proprietario }}</td>
                    <td>{{ s.tipo_licenca }}</td>
                </tr>
                {% endfor %}
            </table>
            {% else %}
            <p style="text-align:center;">Nenhuma solicitação cadastrada.</p>
            {% endif %}
        </body>
        </html>
        """, solicitacoes=solicitacoes)
    except Exception as e:
        flash('Erro ao buscar solicitações: ' + str(e), 'danger')
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Solicitações</title>
        </head>
        <body>
            <h1>Solicitações</h1>
            <div class="message danger">{{ get_flashed_messages()[0] }}</div>
            <a href="/">Voltar</a>
        </body>
        </html>
        """, solicitacoes=[])

@app.route('/solicitacoes', methods=['POST'])
def criar_solicitacao():
    try:
        data = request.json
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO solicitacoes (empresa, cnpj, endereco, proprietario, tipo_licenca) VALUES (%s, %s, %s, %s, %s)',
            (data['empresa'], data['cnpj'], data['endereco'], data['proprietario'], data['tipo_licenca'])
        )
        conn.commit()
        conn.close()
        return jsonify({'mensagem': 'Solicitação criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/solicitacoes', methods=['GET'])
def info_solicitacoes():
    return jsonify({'mensagem': 'Use POST para criar uma solicitação.'})

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    print("Iniciando cliente_api.py")
    app.run(port=5002, debug=True)