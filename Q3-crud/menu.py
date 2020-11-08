import psycopg2
from connection import Connection

def meu_nome():
    nome = input("Digite o nome: ")
    return nome
    
def meu_cpf():
    cpf = input("Digite o CPF: ")
    return cpf

def meu_email():
    email = input("Digite o email: ")
    return email

def valid_cpf(cpf_val):

    if cpf_val.isdigit() == True and len(cpf_val) == 11:
        return 1

    else:
        return 0

def valid_nome (nome_val):

    if len(nome_val) <= 150:
        return 1

    else:
        return 0

def validate_email(email_val):

    if len(email_val) <= 400:
        return 1
    else:
        return 0

def menu():
    opcao= int(input(("Bem-vindo ao nosso Sistema."
                      "Escolha uma opção: \n"
                      "1- Inserir dados\n"
                      "2- Selecionar\n"
                      "3- Alterar dados\n"
                      "4- Excluir\n"
                      "0- Sair\n\n"
                      "DIGITE: ")))
    realizar_operacao(opcao)


def realizar_operacao (opcao):
    if opcao == 1:

        cpf=meu_cpf()
        cpf_valido = valid_cpf(cpf)

        if cpf_valido == 1:

            nome = meu_nome()
            nome_valido = valid_nome(nome)

            email = meu_email()
            email_valido = validate_email(email)

            if nome_valido == 1 and email_valido == 1:
                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute ("insert into pessoa (nome, cpf, email, logado) values ('{0}','{1}','{2}','1')".format(nome, cpf, email))

                conn.commit()
                conn.close()

                menu()

            else:
                menu()

        else:
            menu()


    elif opcao == 2:

        acao_select = int(input("O que gostaria de fazer?\n1- Ver tudo\n2- Consultar por CPF\n3- Consultar por email\n4- Sair\n\nDIGITE: "))

        if acao_select == 1:
            conn = Connection().getConnection()
            cur = conn.cursor()
            cur.execute("select * from pessoa where logado = '1'")

            rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])
                conn.close()
                menu()


        elif acao_select == 2:

            cpf=meu_cpf()
            cpf_valido = valid_cpf(cpf)

            if cpf_valido == 1:

                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute("select * from pessoa where logado = '1' and cpf = '{0}'".format(cpf))
                rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])

                conn.close()
                menu()
            
            else:
                menu()


        elif acao_select == 3:

            email = meu_email()
            email_valido = validate_email(email)

            if email_valido == 1:
                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute("select * from pessoa where logado = '1' and email = '{0}'".format(email))

                rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])

                conn.close()
                menu()

            else:
                print("Email não encontrado.")
                menu()


        elif acao_select == 4:
            print("Adeus.")
            menu()


        else:
            print ("Opção inválida. Tente novamente.")
            menu()



    elif opcao == 3:

        acao_select = int(input("O que gostaria de fazer?\n1- Atualizar nome\n2- Atualizar email\n3- Sair\n\nDIGITE: "))
        
        if acao_select == 1:

            cpf = meu_cpf()
            cpf_valido = valid_cpf(cpf)

            nome = meu_nome()
            nome_valido = valid_nome(nome)

            if nome_valido == 1:
                conn = Connection().getConnection()

                cur = conn.cursor()
                cur.execute("update pessoa set nome = '{0}' where cpf = '{1}'".format(nome,cpf))
                conn.commit()
                conn.close()

            else:
                print ("Nome inválido. Tente novamente.")


        elif acao_select == 2:

            cpf = meu_cpf()
            cpf_valido=valid_cpf(cpf)

            email = meu_email()
            email_valido = validate_email(email)

            if email_valido == 1:

                conn = Connection().getConnection()

                cur = conn.cursor()
                cur.execute("Update pessoa set email = '{0}'".format(email))
                conn.commit()
                conn.close()

            else:
                print ("Email inválido. Tente novamente.")
                menu()


        elif acao_select == 3:
            menu()

        else:
            print ("Opção inválida. Tente novamente.")
            menu()


    elif opcao == 4:

        cpf=meu_cpf()
        cpf_valido = valid_cpf(cpf)

        if cpf_valido == 1:

            conn = Connect().getConnection()
                
            cur = conn.cursor()
            cur.execute("update pessoa set logado = 0 where cpf = '{0}'".format(cpf))
            conn.commit()

            conn.close()
            menu()
        
        else:
            print ("CPF inválido. Tente novamente.")


    elif opcao == 0:
        print("Exit.")
        exit()

    
    else:
        print ("Comando inválido. Tente novamente.")
        menu()