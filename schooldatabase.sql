CREATE TABLE tb_professor (
  idtb_professor INTEGER   NOT NULL ,
  professor_nome VARCHAR(30)    ,
  professor_senha VARCHAR(25)      ,
PRIMARY KEY(idtb_professor));




CREATE TABLE tb_aluno (
  idtb_aluno INTEGER   NOT NULL ,
  tb_professor_idtb_professor INTEGER   NOT NULL ,
  nome_aluno VARCHAR(30)    ,
  senha_aluno VARCHAR(25)      ,
PRIMARY KEY(idtb_aluno)  ,
  FOREIGN KEY(tb_professor_idtb_professor)
    REFERENCES tb_professor(idtb_professor));


CREATE INDEX tb_aluno_FKIndex1 ON tb_aluno (tb_professor_idtb_professor);


CREATE INDEX IFK_Rel_01 ON tb_aluno (tb_professor_idtb_professor);


CREATE TABLE tb_presenca (
  idtb_presenca INTEGER   NOT NULL ,
  tb_aluno_idtb_aluno INTEGER   NOT NULL ,
  presenca_status BOOL    ,
  presenca_imagem VARCHAR(255)    ,
  presenca_data DATETIME      ,
PRIMARY KEY(idtb_presenca, tb_aluno_idtb_aluno)  ,
  FOREIGN KEY(tb_aluno_idtb_aluno)
    REFERENCES tb_aluno(idtb_aluno));


CREATE INDEX tb_presenca_FKIndex1 ON tb_presenca (tb_aluno_idtb_aluno);


CREATE INDEX IFK_Rel_02 ON tb_presenca (tb_aluno_idtb_aluno);


CREATE TABLE tb_treino (
  idtb_treino INTEGER   NOT NULL ,
  tb_aluno_idtb_aluno INTEGER   NOT NULL ,
  treino_foto VARCHAR(255)      ,
PRIMARY KEY(idtb_treino)  ,
  FOREIGN KEY(tb_aluno_idtb_aluno)
    REFERENCES tb_aluno(idtb_aluno));


CREATE INDEX tb_treino_FKIndex1 ON tb_treino (tb_aluno_idtb_aluno);


CREATE INDEX IFK_Rel_03 ON tb_treino (tb_aluno_idtb_aluno);



