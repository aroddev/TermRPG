from classes import Personagem

def menu_principal(personagem):
    """Exibe o menu principal do jogo"""
    while True:
        print("\n=== Menu Principal ===")
        print("\033[31m1.\033[m Status do Personagem")  # Cores ANSI
        print("\033[31m2.\033[m Inventário")
        print("\033[31m3.\033[m Explorar Região")
        print("\033[31m4.\033[m Sair")

        try:
            escolha = int(input("Escolha uma das opções [1-4]: "))
        except ValueError:
            print("Por favor, insira um número válido!")
            continue

        if escolha == 1:
            personagem.mostrar_status()
        elif escolha == 2:
            personagem.mostrar_inventario()
        elif escolha == 3:
            personagem.explorar()
        elif escolha == 4:
            print("Saindo do jogo! Obrigado por jogar o TermRPG!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
   escolhaNome = str(input('Qual vai ser o nome do personagem? '))
   personagem = Personagem(nome=f"{escolhaNome}", hp=100, ataque=20, defesa=15)
   menu_principal(personagem)
