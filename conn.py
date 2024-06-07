import mysql.connector

class Connection:
    @staticmethod
    def conectar():
        # Configurar a conexão com o banco de dados MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='school_facial_recognition'
        )
        return conn

    def carregar_professores(self, professor_combobox):
        # Conectar ao banco de dados
        db_conn = self.conectar()
        c = db_conn.cursor()

        # Consultar os professores
        c.execute("SELECT idtb_professor, professor_nome FROM tb_professor")
        professores = c.fetchall()

        # Preencher o combobox com os nomes dos professores e associar o ID do professor a cada nome
        professor_combobox['values'] = [prof[1] for prof in professores]
        professor_combobox.professores_ids = {prof[1]: prof[0] for prof in professores}

        # Fechar a conexão
        db_conn.close()

    def inserir_aluno(self, ra, professor_id, nome, senha):
        # Conectar ao banco de dados
        db_conn = self.conectar()
        c = db_conn.cursor()

        c.execute("INSERT INTO tb_aluno (idtb_aluno, tb_professor_idtb_professor, nome_aluno, senha_aluno) VALUES (%s, %s, %s, %s)", (ra, professor_id, nome, senha))
        db_conn.commit()  # Confirmar a transação

        # Fechar a conexão e o cursor
        c.close()
        db_conn.close()

    def inserir_chamada(self, aluno_id, presenca_status, presenca_data):
        # Conectar ao banco de dados
        db_conn = self.conectar()
        c = db_conn.cursor()

        # Inserir dados na tabela tb_presenca
        c.execute("INSERT INTO tb_presenca (tb_aluno_idtb_aluno, presenca_status, presenca_data) VALUES (%s, %s, %s)", (aluno_id, presenca_status, presenca_data))
        db_conn.commit()  # Confirmar a transação

        # Fechar a conexão e o cursor
        c.close()
        db_conn.close()

    def listar_presencas(self):
        # Conectar ao banco de dados
        db_conn = self.conectar()
        c = db_conn.cursor()

        # Consultar os dados de presença
        c.execute("select a.nome_aluno, p.presenca_data, p.presenca_status from tb_presenca p join tb_aluno a on a.idtb_aluno = p.tb_aluno_idtb_aluno;")
        presencas = c.fetchall()

        # Fechar a conexão e o cursor
        c.close()
        db_conn.close()

        return presencas

   
 