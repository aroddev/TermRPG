import random

class Personagem:
    def __init__(self, nome, hp, ataque, defesa):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.inventario = []

    def mostrar_status(self):
        """Exibe os atributos do personagem"""
        print("\n=== Status ===")
        print(f"Nome: {self.nome}")
        print(f"HP: {self.hp}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")

    def mostrar_inventario(self):
        """Exibe o inventário do personagem"""
        print("\n=== Inventário ===")
        if not self.inventario:
            print("Inventário Vazio!")
        else:
            for i, item in enumerate(self.inventario, start=1):
                print(f"{i}. {item}")

    def explorar(self):
        """Simula a exploração de uma região e adiciona itens ao inventário"""
        print("Explorando a região...")
        achado = random.choice(["Poção", None])
        if achado:
            print(f"Você encontrou: {achado}!")
            self.inventario.append(achado)
        else:
            print("Você não encontrou nada desta vez.")
