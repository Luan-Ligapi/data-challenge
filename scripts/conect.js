const mysql = require('mysql2');

// Criação da conexão com os mesmos parâmetros do DBeaver
const connection = mysql.createConnection({
  host: '35.199.115.174',        // Endereço IP do servidor MySQL
  port: 3306,                    // Porta do MySQL (padrão 3306)
  user: 'looqbox-challenge',      // Usuário MySQL
  password: 'looq-challenge',     // Senha MySQL
  database: '',                   // Deixe vazio ou especifique o banco de dados se necessário
  ssl: {
    rejectUnauthorized: false     // Você pode ajustar SSL caso seja necessário
  }
});

// Tenta conectar ao MySQL
connection.connect(function(err) {
  if (err) {
    console.error('Erro ao conectar ao MySQL:', err.stack);
    return;
  }
  console.log('Conectado ao MySQL como id ' + connection.threadId);
  
  // Testando uma query simples (ajuste conforme o banco de dados que deseja consultar)
  connection.query('SHOW DATABASES', function (error, results, fields) {
    if (error) throw error;
    console.log(results);
  });

  // Fecha a conexão
  connection.end();
});
