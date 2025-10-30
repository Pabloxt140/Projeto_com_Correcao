import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='sistema'
    )
    with conn:
        with conn.cursor() as cursor:
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS solicitacoes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                empresa VARCHAR(255),
                cnpj VARCHAR(20),
                endereco VARCHAR(255),
                proprietario VARCHAR(255),
                tipo_licenca VARCHAR(100)
            )
            ''')
            # Exemplo: inserir apenas se não existir
            cursor.execute('''
            SELECT COUNT(*) FROM solicitacoes WHERE cnpj=%s
            ''', ('12345678000199',))
            if cursor.fetchone()[0] == 0:
                cursor.execute('''
                INSERT INTO solicitacoes (empresa, cnpj, endereco, proprietario, tipo_licenca)
                VALUES (%s, %s, %s, %s, %s)
                ''', ('Empresa Exemplo', '12345678000199', 'Rua Exemplo, 123', 'João da Silva', 'Ambiental'))
        conn.commit()
except Exception as e:
    print(f"Erro ao criar banco ou inserir dados: {e}")