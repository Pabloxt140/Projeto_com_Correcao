from flask import Flask, render_template, request, redirect, url_for, flash, render_template_string
import requests
import pymysql

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para flash messages

@app.route('/')
def listar():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='sistema'
    )
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM solicitacoes")
            dados = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
    html = '''
    <html>
    <head>
        <title>Solicitações</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f8f9fa; margin: 0; padding: 20px; }
            h2 { color: #343a40; }
            table { border-collapse: collapse; width: 100%; background: #fff; }
            th, td { padding: 8px 12px; text-align: left; }
            th { background: #007bff; color: #fff; }
            tr:nth-child(even) { background: #f2f2f2; }
            tr:hover { background: #e9ecef; }
            .btn {
                display: inline-block;
                padding: 8px 16px;
                margin-bottom: 16px;
                font-size: 16px;
                color: #fff;
                background: #28a745;
                border: none;
                border-radius: 4px;
                text-decoration: none;
                transition: background 0.2s;
            }
            .btn:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h2>Solicitações</h2>
        <a href="{{ url_for('nova_solicitacao') }}" class="btn">Nova Solicitação</a>
        <table>
            <tr>
                {% for col in colunas %}
                <th>{{ col }}</th>
                {% endfor %}
            </tr>
            {% for row in dados %}
            <tr>
                {% for item in row %}
                <td>{{ item }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''
    return render_template_string(html, dados=dados, colunas=colunas)

@app.route('/nova', methods=['GET', 'POST'])
def nova_solicitacao():
    if request.method == 'POST':
        dados = {
            'empresa': request.form['empresa'],
            'cnpj': request.form['cnpj'],
            'endereco': request.form['endereco'],
            'proprietario': request.form['proprietario'],
            'tipo_licenca': request.form['tipo_licenca']
        }
        try:
            resp = requests.post('http://localhost:5002/solicitacoes', json=dados)
            if resp.status_code == 201:
                flash('Solicitação criada com sucesso!', 'success')
                return redirect(url_for('listar'))
            else:
                flash('Erro ao criar solicitação.', 'danger')
        except Exception as e:
            flash('Erro ao conectar ao servidor.', 'danger')
    return render_template('nova.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
