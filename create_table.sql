CREATE TABLE solicitacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empresa VARCHAR(255),
    cnpj VARCHAR(20),
    endereco VARCHAR(255),
    proprietario VARCHAR(255),
    tipo_licenca VARCHAR(100)
);
