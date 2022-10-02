from pokemon import *
from pessoa import *

player = str(input("Escolha seu nome: "))
player = Player(player)
def escolher_pokemon_inicial(player):
    print(f"Olá {player.nome}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!")

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