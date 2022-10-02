import random

class Pokemon:
    def __init__(self, especie=None, nome=None, level=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return f"{self.nome}({self.level})"

    def atacar(self, pokemon, ataque_efetivo=None):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        print(f"{pokemon} perdeu {ataque_efetivo} pontos de vida!")

class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print(f"{self} lançou chamas em {pokemon}!")
        super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        if pokemon.especie == "Fogo" or pokemon.especie == "Pedra":
            ataque_efetivo = int(self.ataque * random.random() * 2.0)
            super().atacar(pokemon, ataque_efetivo)
            print(f"{self} lançou um jato d'água em {pokemon}!")
        else:
            print(f"{self} lançou um jato d'água em {pokemon}!")
            super().atacar(pokemon)

class PokemonEletrico(Pokemon):
    tipo = "Elétrico"

    def atacar(self, pokemon):
        if pokemon.especie == "Água":
            ataque_efetivo = int(self.ataque * random.random() * 2.0)
            super().atacar(pokemon, ataque_efetivo)
            print(f"{self} lançou um raio de trovão em {pokemon}!")
        else:
            print(f"{self} lançou um raio de trovão em {pokemon}!")
            super().atacar(pokemon)

class PokemonPedra(Pokemon):
    tipo = "Pedra"

    def atacar(self, pokemon):
        if pokemon.especie == "Fogo":
            ataque_efetivo = int(self.ataque * random.random() * 2.0)
            super().atacar(pokemon, ataque_efetivo)
            print(f"{self} lançou pedregulhos na cabeça de {pokemon}!")
        else:
            print(f"{self} lançou pedregulhos na cabeça de {pokemon}!")
            super().atacar(pokemon)

