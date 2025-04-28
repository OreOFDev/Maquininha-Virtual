# Printei a mensagem de boas vindas
print("Bem Vindo A Maquinha De Loja!")

# Criei A Variavel Menu Que Tem As Opcoes De Pagamento
menu = """
1 - Debito
2 - Credito
3 - Pix
4 - Alimentacao Ou Refeicao
0 - Cancelar
"""
# Printei O Menu
print(menu)

# Criei A Variavel Opcao Que A Pessoa Escolhe A Opcao De Pagamento
opcao = input("Qual a opcao desejada? \n")

# Criei A Variavel Valor Que A Pessoa Escolhe O Valor Da Operacao
valor = input("Qual o valor da operacao? \n")

# Se O Valor for um digito
if valor.isdigit():

    # transformo em float
    valor = float(valor)

    # Se A Opcao for um digito
    if opcao.isdigit():

        # transformo em int
        opcao = int(opcao)

        # Se A Opcao for 1 (Debito)
        if opcao == 1: 

            # Printei A Mensagem De Debito
            print("Debito Selecionado")

            # Criei A Variavel AprOuIns Que A Pessoa Escolhe A Opcao De Aproximar Ou Inserir
            AprOuIns = input("Digite Qual Aproximar Ou Inserir (APR/INS) \n").upper()

            # Se A Opcao For Aproximar
            if AprOuIns == "APR":
                
                # Printei A Mensagem De Aproximar
                print("Aproximar Selecionado")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

            # Se A Opcao For Inserir
            elif AprOuIns == "INS":

                # Printei A Mensagem De Inserir
                print("Inserir Selecionado")

                # Criei A Variavel Senha Que A Pessoa Digita A Senha
                senha = input("Digite a Senha \n")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

        # Se A Opcao For 2 (Credito)
        elif opcao == 2:

            # Printei A Mensagem De Credito
            print("Credito Selecionado")

            # Criei A Variavel AprOuIns Que A Pessoa Escolhe A Opcao De Aproximar Ou Inserir
            AprOuIns = input("Digite Qual Aproximar Ou Inserir (APR/INS) \n").upper()

            # Se A Opcao For Aproximar
            if AprOuIns == "APR":
                
                # printei A Mensagem De Aproximar
                print("Aproximar Selecionado")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

            # Se A Opcao For Inserir
            elif AprOuIns == "INS":
                
                # Printei A Mensagem De Inserir
                print("Inserir Selecionado")

                # Criei A Variavel Senha Que A Pessoa Digita A Senha
                senha = input("Digite a Senha \n")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

        # Se A Opcao For 3 (Pix)
        elif opcao == 3:
            
            # Printei A Mensagem De Pix
            print("Pix Selecionado")

            # Criei A Variavel QrOuChave Que A Pessoa Escolhe QRCode Ou ChavePix
            QrOuChave = input("QRCode Ou ChavePix (QR/CHAVE) \n")

            # Se A Opcao For QRCode
            if QrOuChave == "QR":

                # Printei A Mensagem De QRCode
                print("QRCode Selecionado")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

            # Se A Opcao For ChavePix
            elif QrOuChave == "CHAVE":
                
                # Printei A Mensagem De ChavePix
                print("ChavePix Selecionado")

                # Criei A Variavel Chave Que E A Chave Pix
                chave = "lojalegal@gmail.com"

                # Printei A Mensagem Da Chave
                print(f"A Chave E {chave}")

                # Printei A Mensagem De Operacao Realizada Com Sucesso!
                print("Operacao Realizada Com Sucesso!")

        # Se A Opcao For 4 (Alimentacao Ou Refeicao)
        elif opcao == 4:

            # Printei A Mensagem De Alimentacao Ou Refeicao
            print("Alimentacao Ou Refeicao Selecionado")

            # Criei A Variavel AliOuRef Que A Pessoa Escolhe Alimentacao Ou Refeicao
            aliOuRef = input("Digite Qual Alimentacao Ou Refeicao (ALI/REF) \n").upper()

            # Se A Opcao For Alimentacao
            if aliOuRef == "ALI": 

                # Printei A Mensagem De Alimentacao
                print("Alimentacao Selecionada")

                # Criei A Variavel AprOuIns Que A Pessoa Escolhe A Opcao De Aproximar Ou Inserir
                AprOuIns = input("Digite Qual Aproximar Ou Inserir (APR/INS) \n").upper()

                # Se A Opcao For Aproximar
                if AprOuIns == "APR":
                    
                    # Printei A Mensagem De Aproximar
                    print("Aproximar Selecionado")

                    # Printei A Mensagem De Operacao Realizada Com Sucesso!
                    print("Operacao Realizada Com Sucesso!")

                # Se A Opcao For Inserir
                elif AprOuIns == "INS":
                    
                    # Printei A Mensagem De Inserir
                    print("Inserir Selecionado")

                    # Criei A Variavel Senha Que A Pessoa Digita A Senha
                    senha = input("Digite a Senha \n")

                    # Printei A Mensagem De Operacao Realizada Com Sucesso!
                    print("Operacao Realizada Com Sucesso!")


            # Se A Opcao For Refeicao
            elif aliOuRef == "REF":

                # Printei A Mensagem De Refeicao
                print("Refeicao Selecionada")

                # Criei A Variavel AprOuIns Que A Pessoa Escolhe A Opcao De Aproximar Ou Inserir
                AprOuIns = input("Digite Qual Aproximar Ou Inserir (APR/INS) \n").upper()

                # Se A Opcao For Aproximar
                if AprOuIns == "APR":
                    
                    # Printei A Mensagem De Aproximar
                    print("Aproximar Selecionado")

                    # Printei A Mensagem De Operacao Realizada Com Sucesso!
                    print("Operacao Realizada Com Sucesso!")

                # Se A Opcao For Inserir
                elif AprOuIns == "INS":
                    
                    # Printei A Mensagem De Inserir
                    print("Inserir Selecionado")

                    # Criei A Variavel Senha Que A Pessoa Digita A Senha
                    senha = input("Digite a Senha \n")

                    # Printei A Mensagem De Operacao Realizada Com Sucesso!
                    print("Operacao Realizada Com Sucesso!")

            # Se A Opcao Nao For Alimentacao Ou Refeicao
            else:

                # Printei A Mensagem De Erro
                print("Erro: Opcao Invalida")

        # Se A Opcao For 0 (Cancelar)
        elif opcao == 0:

            # Printei A Mensagem De Operacao Cancelada
            print("Operacao Cancelada")

# Se A Opcao Nao For Debito, Credito, Pix, Alimentacao Ou Refeicao
else:

    # Printei A Mensagem De Erro
    print("Erro: Opcao Invalida")
