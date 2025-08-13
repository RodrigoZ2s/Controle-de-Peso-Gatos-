import os

lista_de_gatos = [
    {"nome": "Mimikyu", "peso": "" },
    {"nome": "fumaça", "peso": "" },
    {"nome": "Macumba", "peso": "",},
    {"nome": "puera", "peso": "",},
]

def registrar_gatos(): # Finalizado
    while True:
        nome_digitado = input("Digite o nome do gato: ")
        nome_verificado = False

        for nome in lista_de_gatos:
            if nome_digitado.lower() == nome["nome"].lower():
                nome_verificado = True
                peso_atual = input("Digite o peso atual do gato (Em gramas): ")
                if peso_atual.isdigit() == False:
                    print("Número inválido")
                else:
                    nome["peso"] = peso_atual
                    print("Gato registrado com sucesso!")
        if nome_verificado == False:
            print("Nome não encontrado!")

        registrar_outro = input("deseja continuar? digite [S]im ou [N]ao]")
        if registrar_outro.lower() in ["sim", "s"]:
            continue
        break


def monitor_peso(): # Finalizado

    excelente = 30
    muito_bom = 20
    bom = 15
    baixo = 10
    
    gato_digitado = input("Nome do gato: ")
    for gatos in lista_de_gatos:
        if gato_digitado.lower() in gatos["nome"]:
            peso_atual = input("Peso atual do gato: ")

            if peso_atual.isdigit() == False:
                return "Você não digitou um número válido"  
            ganho = int(peso_atual) - int(gatos["peso"])
            gatos["peso"] = peso_atual

            if ganho < bom:
                print("❌ Ruim!: Ganho de peso igual ou abaixo de 14g.")
            elif ganho >= 15 and ganho < muito_bom:
                print("✅ Bom!: Ganho de peso entre 15g e 19g.")
            elif ganho >= muito_bom and ganho < excelente:
                print("✅ Muito bom!: Ganho de peso entre 20g e 29g.")
            elif ganho >= excelente:
                print(
                f"✅ Excelente!: Ganho de peso de 30g ou mais. \n" 
                f"Atenção!: Ganho de peso excessivo! procure um veterinário se notar mudanças no comportamento de {gato_digitado}"
            )

    return "Gato não encontrado"

def info_gatos(): # Finalizado
    for gato in lista_de_gatos:
        print(f"Gato: {gato["nome"]} | Peso: {gato["peso"]}")
   

def menu_gatos(): # Finalizado
    while True:
        print("========================")
        print("   Pesagem dos gatos    ")
        print("========================")
        print("Escolha as opções abaixo")
        print("1 - Registrar peso atual")
        print("2 - Monitor de Peso")
        print("3 - Informações mais recentes")
        print("0 - Sair")
        escolha_usuario = input("R: ")

        if escolha_usuario == "1":
            os.system("cls")
            registrar_gatos()
        elif escolha_usuario == "2":
            os.system("cls")
            monitor_peso()
        elif escolha_usuario == "3":
            os.system("cls")
            info_gatos()
            input("Pressione Enter para continuar")
        elif escolha_usuario == "0":
            continue
        else:
            os.system("cls")
            print("Você não escolheu uma opção válida!")
            continue

menu_gatos()