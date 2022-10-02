import random
import time
from pokemon import *

NOMES = [
        "João", "Isabela", "Lorena", "Francisco", "Ricardo", "Diego",
        "Patrícia", "Marcelo", "Gustavo", "Gerônimo", "Gary"
]

POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp")
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def mostrar_pokemon(self):
        if self.pokemons:
            print(f"Pókemons de {self.nome}:")
            for indice, pokemon in enumerate(self.pokemons):
                print(f"{indice} - {pokemon}")
        else:
            print(f"{self.nome} não tem pókemons em sua mochila.")

    def dinheiro_de_batalha(self, pokemon):
        if pokemon.vida <= 0:
            quantidade = pokemon.level * 50
            self.dinheiro += quantidade
            print(f"{self.nome} recebeu ${quantidade}!")
        else:
            quantidade = pokemon.level * 5
            self.dinheiro -= quantidade
            if self.dinheiro <= 0:
                self.dinheiro = 0
            print(f"{self.nome} perdeu ${quantidade}!")

    def mostrar_dinheiro(self):
        print(f"Sua carteira: ${self.dinheiro}")

    def escolher_pokemon(self):
        if self.pokemons:
            self.mostrar_pokemon()
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self.nome} escolheu {pokemon_escolhido}!")
            return pokemon_escolhido
        else:
            print("ERRO: esse jogador não possui nenhum pokemon para ser escolhido.")

    def batalhar(self, pessoa):
        print(f"{self.nome} inicou uma batalha com {pessoa.nome}")

        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                pokemon.atacar(pokemon_inimigo)
                if pokemon_inimigo.vida <= 0:
                    print(f"{pokemon_inimigo} desmaiou e {pokemon} venceu esta batalha!")
                    self.dinheiro_de_batalha(pokemon_inimigo)
                    self.mostrar_dinheiro()
                    break
                pokemon_inimigo.atacar(pokemon)
                if pokemon.vida <= 0:
                    print(f"{pokemon} desmaiou e {pokemon_inimigo} venceu esta batalha!")
                    self.dinheiro_de_batalha(pokemon_inimigo)
                    self.mostrar_dinheiro()
                    break
        else:
            print("Essa batalha não pode ocorrer.")

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome} capturou {pokemon}!")

    def captura_de_exploracao(self, pokemon):
        escolha = str(input(f"Deseja capturar {pokemon}? (s/n): "))

        if escolha == "s":
            if pokemon.level >= 50 and random.random() >= 0.6:
                self.capturar(pokemon)
            elif pokemon.level >= 100 and random.random() >= 0.7:
                self.capturar(pokemon)
            elif pokemon.level <= 50 and random.random() >= 0.5:
                self.capturar(pokemon)
            else:
                print(f"{pokemon} fugiu!")
        else:
            print("Okay, até mais!")

    def escolher_pokemon(self):
        if self.pokemons:
            self.mostrar_pokemon()
            while True:
                try:
                    escolha = int(input("Escolha seu Pokemon: "))

                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido}, eu escolho você!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha inválida!")
        else:
            print("ERRO: esse jogador não possui nenhum pokemon para ser escolhido.")

    def explorar(self):
        if random.random() <= 0.4:
            pokemon_selvagem = random.choice(POKEMONS)
            print(f"Um Pokémon selvagem apareceu: {pokemon_selvagem}")
            self.captura_de_exploracao(pokemon_selvagem)
        else:
            print("Nenhum Pokémon encontrado.")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):

        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            self.mostrar_pokemon()
            print(f"{self.nome} escolheu {pokemon_escolhido}!")
            return pokemon_escolhido
        else:
            print("ERRO: esse jogador não possui nenhum pokemon para ser escolhido.")
