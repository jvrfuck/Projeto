from conexcao import criar_conexao, fechar_conexao


def insere_empresa(con, NOME, CATEGORIA, CNPJ, TELEFONE, EMAIL, SENHA):
    cursor = con.cursor()
    sql = "INSERT INTO EMPRESA(NOME, CATEGORIA, CNPJ, TELEFONE, EMAIL, SENHA) VALUES(%s, %s, %s, %s, %s, %s)"
    valores = (NOME, CATEGORIA, CNPJ, TELEFONE, EMAIL, SENHA)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()


def select_empresa(con):
    cursor = con.cursor()
    sql = "SELECT ID_EMPRESA, NOME, CATEGORIA, CNPJ, TELEFONE, EMAIL, SENHA FROM EMPRESA"
    cursor.execute(sql)


def main():
    con = criar_conexao("localhost", "root", "doug", "projeto_entra21_db")

    insere_empresa(con, "Douglas", "Jiu-Jitsu", "19.877.249/0001-08",
                   "douglasbitencourtadm@gmail.com", "1234")

    fechar_conexao(con)


if __name__ == '__main__':
    main()
