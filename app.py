from flask import Flask, render_template_string, jsonify
import pymysql

app = Flask(__name__)

# Rota para adicionar uma nova empresa
@app.route('/adicionar_empresa', methods=['POST'])
def adicionar_empresa():
    from flask import request
    data = request.json
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sistema',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO solicitacoes (empresa, cnpj, endereco, proprietario, tipo_licenca) VALUES (%s, %s, %s, %s, %s)',
            (data['empresa'], data['cnpj'], data['endereco'], data['proprietario'], data['tipo_licenca'])
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return jsonify({'id': new_id}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Rota para retornar os dados em JSON
@app.route('/empresas_json')
def listar_empresas_json():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sistema',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        cursor.execute('SELECT id, empresa, cnpj, endereco, proprietario, tipo_licenca FROM solicitacoes')
        empresas = cursor.fetchall()
        print("Dados retornados do banco:", empresas)  # Debug: veja no terminal
        conn.close()
        return jsonify(empresas)
    except Exception as e:
        print("Erro ao acessar o banco:", e)
        return jsonify({'erro': str(e)}), 500

# Rota para aceitar uma solicitação
@app.route('/aceitar_solicitacao/<int:id>', methods=['POST'])
def aceitar_solicitacao(id):
    try:
        # Não faz update de status, apenas retorna sucesso
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Rota para excluir uma solicitação
@app.route('/excluir_solicitacao/<int:id>', methods=['DELETE'])
def excluir_solicitacao(id):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='sistema',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        cursor.execute('DELETE FROM solicitacoes WHERE id=%s', (id,))
        conn.commit()
        conn.close()
        return jsonify({'ok': True})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Rota para exibir o frontend HTML
@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Solicitar Licença Ambiental</title>
        <style>
            body {
                background: #e8f5e9;
                color: #1b5e20;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            header {
                background: linear-gradient(90deg, #43a047 60%, #a5d6a7 100%);
                color: #fff;
                padding: 30px 0 20px 0;
                text-align: center;
                box-shadow: 0 2px 8px #c8e6c9;
            }
            header .icon {
                font-size: 48px;
                vertical-align: middle;
                margin-right: 10px;
            }
            h1 {
                margin: 0;
                font-size: 2.2em;
                letter-spacing: 2px;
            }
            .subtitle {
                font-size: 1.1em;
                color: #e0f2f1;
                margin-top: 8px;
            }
            .form-container {
                background: #fff;
                margin: 40px auto 0 auto;
                padding: 18px 24px;
                border-radius: 8px;
                box-shadow: 0 2px 8px #c8e6c9;
                width: 90%;
                max-width: 900px;
                text-align: center;
            }
            .form-container input, .form-container select {
                margin: 6px 8px 12px 0;
                padding: 6px 10px;
                border: 1px solid #a5d6a7;
                border-radius: 4px;
                font-size: 1em;
            }
            .form-container button {
                background: #43a047;
                color: #fff;
                border: none;
                padding: 8px 18px;
                border-radius: 4px;
                font-size: 1em;
                cursor: pointer;
                margin-top: 10px;
            }
            .form-container button:hover {
                background: #388e3c;
            }
            .list-btn {
                display: inline-block;
                margin-top: 24px;
                background: #388e3c;
                color: #fff;
                padding: 10px 22px;
                border-radius: 4px;
                text-decoration: none;
                font-size: 1.1em;
                transition: background 0.2s;
            }
            .list-btn:hover {
                background: #2e7031;
            }
            footer {
                text-align: center;
                padding: 18px 0 10px 0;
                background: #a5d6a7;
                color: #1b5e20;
                font-size: 1em;
                margin-top: 40px;
                letter-spacing: 1px;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    </head>
    <body>
        <header>
            <span class="icon"><i class="fas fa-leaf"></i></span>
            <h1>Solicitar Licença Ambiental</h1>
            <div class="subtitle">Preencha o formulário para solicitar uma licença ambiental</div>
        </header>
        <div class="form-container">
            <form id="empresaForm" autocomplete="off">
                <input type="text" name="empresa" placeholder="Empresa" required>
                <input type="text" name="cnpj" placeholder="CNPJ" required>
                <input type="text" name="endereco" placeholder="Endereço" required>
                <input type="text" name="proprietario" placeholder="Proprietário" required>
                <input type="text" name="tipo_licenca" placeholder="Tipo Licença" required>
                <br>
                <button type="submit"><i class="fas fa-plus"></i> Solicita Licença</button>
            </form>
            <a class="list-btn" href="/listar"><i class="fas fa-list"></i> Listar Solicitações</a>
        </div>
        <footer>
            <i class="fas fa-seedling"></i> Sistema Verde &copy; 2025 - Projeto de Empresas Sustentáveis
        </footer>
        <script>
            document.getElementById('empresaForm').addEventListener('submit', function(event) {
                event.preventDefault();
                const form = event.target;
                const dados = {
                    empresa: form.empresa.value,
                    cnpj: form.cnpj.value,
                    endereco: form.endereco.value,
                    proprietario: form.proprietario.value,
                    tipo_licenca: form.tipo_licenca.value
                };
                fetch('/adicionar_empresa', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(dados)
                })
                .then(resp => resp.json())
                .then(res => {
                    if (res.id) {
                        alert('Solicitação enviada com sucesso!');
                        form.reset();
                    } else {
                        alert('Erro ao solicitar licença: ' + (res.erro || 'Erro desconhecido'));
                    }
                })
                .catch(() => alert('Erro ao conectar ao servidor.'));
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/listar')
def listar():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lista de Solicitações de Licença</title>
        <style>
            body {
                background: #e8f5e9;
                color: #1b5e20;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            header {
                background: linear-gradient(90deg, #43a047 60%, #a5d6a7 100%);
                color: #fff;
                padding: 30px 0 20px 0;
                text-align: center;
                box-shadow: 0 2px 8px #c8e6c9;
            }
            header .icon {
                font-size: 48px;
                vertical-align: middle;
                margin-right: 10px;
            }
            h1 {
                margin: 0;
                font-size: 2.2em;
                letter-spacing: 2px;
            }
            .subtitle {
                font-size: 1.1em;
                color: #e0f2f1;
                margin-top: 8px;
            }
            table {
                margin: 40px auto;
                border-collapse: collapse;
                width: 90%;
                background: #fff;
                box-shadow: 0 2px 8px #c8e6c9;
            }
            th, td {
                border: 1px solid #a5d6a7;
                padding: 12px 8px;
                text-align: center;
            }
            th {
                background: #388e3c;
                color: #fff;
                font-size: 1.1em;
            }
            tr:nth-child(even) {
                background: #f1f8e9;
            }
            tr:hover {
                background: #c8e6c9;
            }
            .leaf {
                color: #43a047;
                font-size: 1.2em;
                margin-right: 4px;
            }
            .back-btn {
                display: inline-block;
                margin: 24px 0 0 5%;
                background: #388e3c;
                color: #fff;
                padding: 10px 22px;
                border-radius: 4px;
                text-decoration: none;
                font-size: 1.1em;
                transition: background 0.2s;
            }
            .back-btn:hover {
                background: #2e7031;
            }
            .action-btn {
                padding: 6px 12px;
                border: none;
                border-radius: 4px;
                font-size: 1em;
                cursor: pointer;
                margin: 0 2px;
            }
            .accept-btn {
                background: #388e3c;
                color: #fff;
            }
            .accept-btn:hover {
                background: #256029;
            }
            .delete-btn {
                background: #c62828;
                color: #fff;
            }
            .delete-btn:hover {
                background: #8e0000;
            }
            footer {
                text-align: center;
                padding: 18px 0 10px 0;
                background: #a5d6a7;
                color: #1b5e20;
                font-size: 1em;
                margin-top: 40px;
                letter-spacing: 1px;
            }
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    </head>
    <body>
        <header>
            <span class="icon"><i class="fas fa-leaf"></i></span>
            <h1>Lista de Solicitações de Licença</h1>
            <div class="subtitle">Empresas que solicitaram licença ambiental</div>
        </header>
        <a class="back-btn" href="/"><i class="fas fa-arrow-left"></i> Solicitar Licença</a>
        <table id="empresas">
            <thead>
                <tr>
                    <th><span class="leaf"><i class="fas fa-tree"></i></span>ID</th>
                    <th><span class="leaf"><i class="fas fa-building"></i></span>Empresa</th>
                    <th><span class="leaf"><i class="fas fa-id-card"></i></span>CNPJ</th>
                    <th><span class="leaf"><i class="fas fa-map-marker-alt"></i></span>Endereço</th>
                    <th><span class="leaf"><i class="fas fa-user"></i></span>Proprietário</th>
                    <th><span class="leaf"><i class="fas fa-certificate"></i></span>Tipo Licença</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        </table>
        <footer>
            <i class="fas fa-seedling"></i> Sistema Verde &copy; 2025 - Projeto de Empresas Sustentáveis
        </footer>
        <script>
            function removerLinha(btn) {
                btn.closest('tr').remove();
            }
            function atualizarStatusLinha(tr) {
                tr.style.background = "#c8e6c9";
            }
            fetch('/empresas_json')
                .then(response => response.json())
                .then(data => {
                    const tbody = document.querySelector('#empresas tbody');
                    data.forEach(e => {
                        const tr = document.createElement('tr');
                        tr.innerHTML = `<td>${e.id}</td>
                            <td>${e.empresa}</td>
                            <td>${e.cnpj}</td>
                            <td>${e.endereco}</td>
                            <td>${e.proprietario}</td>
                            <td>${e.tipo_licenca}</td>
                            <td>
                                <button class="action-btn accept-btn" onclick="aceitarSolicitacao(${e.id}, this)"><i class="fas fa-check"></i> Aceitar</button>
                                <button class="action-btn delete-btn" onclick="excluirSolicitacao(${e.id}, this)"><i class="fas fa-trash"></i> Excluir</button>
                            </td>`;
                        tbody.appendChild(tr);
                    });
                });

            function aceitarSolicitacao(id, btn) {
                fetch('/aceitar_solicitacao/' + id, {method: 'POST'})
                    .then(resp => resp.json())
                    .then(res => {
                        if (res.ok) {
                            const tr = btn.closest('tr');
                            atualizarStatusLinha(tr);
                            btn.disabled = true;
                            // Remove o botão de excluir ao aceitar
                            const deleteBtn = tr.querySelector('.delete-btn');
                            if (deleteBtn) {
                                deleteBtn.style.display = 'none';
                            }
                            alert('Solicitação aceita com sucesso!');
                        } else {
                            alert('Erro ao aceitar: ' + (res.erro || 'Erro desconhecido'));
                        }
                    })
                    .catch(() => alert('Erro ao conectar ao servidor.'));
            }
            function excluirSolicitacao(id, btn) {
                if (!confirm('Tem certeza que deseja excluir esta solicitação?')) return;
                fetch('/excluir_solicitacao/' + id, {method: 'DELETE'})
                    .then(resp => resp.json())
                    .then(res => {
                        if (res.ok) {
                            removerLinha(btn); // Só remove da tela se o backend confirmou a exclusão
                        } else {
                            alert('Erro ao excluir: ' + (res.erro || 'Erro desconhecido'));
                        }
                    })
                    .catch(() => alert('Erro ao conectar ao servidor.'));
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
