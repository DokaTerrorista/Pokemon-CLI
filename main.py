import time
import os
import pickle
from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    print(f"Você poderá escolher o Pokemon que irá lhe acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui três escolhas: ")
    print("1 - Pikachu")
    print("2 - Charmander")
    print("3 - Squirtle")

    while True:
        escolha = str(input("Escolha seu pokemon: "))

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha válida!")

def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
    except Exception as error:
        print("Erro ao salvar jogo")
        print(error)

def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading feito com sucesso")
            return player
    except:
        print("")

if __name__ == "__main__":
    print("-----------------------------------------")
    print("Bem-vindo ao Pokémon Game RPG de terminal")
    print("-----------------------------------------")

    player = carregar_jogo()

    if not player:
        nome = str(input("Olá, qual é o seu nome: "))
        player = Player(nome)
        print(f"Olá {player.nome}, esse é um mundo habitado por Pokémons. A partir de agora, sua missão é se tornar um mestre Pokémon.")
        time.sleep(2)
        print("Capture o máximo de Pokémon que conseguir e lute contra seus inimigos!")
        time.sleep(2)
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns Pokémon.")
            player.mostrar_pokemon()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Vi que você não tem Pokémon algum, portanto, precisa escolher um.")
            time.sleep(1)
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você já possui um Pokémon, enfrente seu arqui-rival desde o jardim de infância, Gary!")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        time.sleep(2)
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print("-----------------------------------------")
        print(f"O que deseja fazer, {player.nome}")
        print("1 - Explorar o mundo")
        print("2 - Lutar contra um inimigo")
        print("3 - Ver PokéAgenda")
        print("0 - Sair do jogo")

        escolha = str(input("Sua escolha: "))

        if escolha == "0":
            print("Encerrando o jogo...")
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemon()
        else:
            print("Escolha inválida")
