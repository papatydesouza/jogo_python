import forca
import adivinhacao

print("ESCOLHA SEU JOGO NO MENU:\n1- Forca\n2- Adivinhação\n**********************************")
jogo = int(input("Qual jogo você quer jogar agora?"))
if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()