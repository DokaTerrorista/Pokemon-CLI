import random
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
                    self.dinheiro += pokemon_inimigo.level * 50
                    print(f"{self.nome} recebeu ${self.dinheiro},00!")
                    break
                pokemon_inimigo.atacar(pokemon)
                if pokemon.vida <= 0:
                    print(f"{pokemon} desmaiou e {pokemon_inimigo} venceu esta batalha!")
                    break
        else:
            print("Essa batalha não pode ocorrer.")

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self.nome} capturou {pokemon}!")

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


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):

        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self.nome} escolheu {pokemon_escolhido}!")
            return pokemon_escolhido
        else:
            print("ERRO: esse jogador não possui nenhum pokemon para ser escolhido.")

player1 = Player("Kelvyn", pokemons=[PokemonEletrico("Pikachu", level=11), PokemonAgua("Squirtle", level=5), PokemonPedra("Aerodactyl", level=50)])
inimigo1 = Inimigo("Gary", pokemons=[PokemonFogo("Charmander", level=7), PokemonAgua("Squirtle", level=35), PokemonPedra("Geodude", level=10)])

player1.batalhar(inimigo1)