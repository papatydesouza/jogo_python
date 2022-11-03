import random

def jogar():
    print ("*****************\nBEM VINDO AO JOGO\n*****************")

    numero_secreto = random.randint(0, 100)
    pontos = 1000

    nivel_str = input("Qual nível de dificuldade voce quer?\n1-fácil \n2-médio \n3-difícil\n")
    nivel = int(nivel_str)

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 4

    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite um número inteiro de 0 a 100: ")
        print(chute_str)
        chute = int(chute_str)

        if (chute < 0 or chute > 100):
            print("Você precisa digitar um valor entre 0 e 100!")
            continue
        else:
            maior_que = chute > numero_secreto
            menor_que = chute < numero_secreto

            correto = numero_secreto == chute

        if (correto):
            print("Voce acertou o número")
            print("Sua pontuação foi de: ",pontos)
            break
        else:
            if (maior_que):
                print("Voce errou o número! Seu chute foi maior do que o número secreto")
                pontos = pontos - 100
                print("Sua pontuação foi: ", pontos)
            elif (menor_que):
                print("Voce errou o número! Seu chute foi menor do que o número secreto")
                pontos = pontos - 100
                print("Sua pontuação foi: ", pontos)

    print("O número secreto é: ",numero_secreto)
    print("************\nFIM DO JOGO!\n************")

if(__name__ == "__main__"):
    jogar()
