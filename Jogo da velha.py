#Jogo do galo
#===================================================================================Menu============================================================================================================
#tela pedindo a você se você deseja jogar ou sair do jogo, se você digitar que ‘Não’ o jogo irá parar de rodar e você terá que abrir ele novamente para jogar, mas se você digitou que ‘Sim’,
#você deseja jogar, logo em seguida pedira para escolher seu marcador (X ou O), assim que você terminar de usar o menu aparecera o tabuleiro do jogo da velha e o jogo começara o jogo
#===================================================================================================================================================================================================
import sys

entrar_sair =input ('Voce deseja jogar o Jogo da Velha?{S/N}:').upper()

if entrar_sair == 'N':
    print ('Encerrando sessao'), sys.exit()

elif entrar_sair == 'S':
    print ('Jogo iniciando...')

elif entrar_sair != 's' or 'n':
    print ('Voce nao escolheu nenhuma das opçoes o sistema vai se desativar'), sys.exit()

menu = input ('Digite que marcador voce deseja {X/O}').upper()

if menu == 'X':
    print ('Voce escolheu X seu oponente ira ficar com O')
    
    
elif menu == 'O':
    print ('Voce escolheu O seu oponente ira ficar com X')

elif menu != 'X' or 'O':
    print ('Voce nao escolheu nenhuma das opçoes o sistema vai se desativar'), sys.exit()

#===================================================================================Fim do menu=====================================================================================================

#===================================================================================Tabuleiro=======================================================================================================
#Fizemos essa parte do programa para definir as casas onde o Jogador iria posicionar o “X” ou “O”, fizemos e deixamos o tabuleiro como uma variável e o menu bem básico só pedindo se
#você quer jogar e se você quer jogar com ‘X’ ou ‘O’ e fizemos com que o tabuleiro aparecesse 1,2,3,4... ao invés se b1,b2,b3,b4... assim para ficar mais fácil o entendimento dos jogador(es).
#===================================================================================================================================================================================================

x_o = 'X'
uraraka_san = 0 
b1 = ('1')
b2 = ('2')
b3 = ('3')
b4 = ('4')
b5 = ('5')
b6 = ('6')
b7 = ('7')
b8 = ('8')
b9 = ('9')
def tabu():
    print(b1 ,"  |  ", b2  ,"  |  ", b3)
    print(b4 ,"  |  ", b5  ,"  |  ", b6)
    print(b7 ,"  |  ", b8  ,"  |  ", b9)

#=================================================================================Fim do tabuleiro==================================================================================================

print('-' *100)
print('Bem vindo ao jogo da velha desenvolvido por Marina e Vitor Kruger')
print('-' *100)

#==============================================================================Interpretaçao de comandos=============================================================================================
#Aqui nós usamos um esquema para que só o ‘X’ começasse e fizemos também um sistema para interpretar os comandos quando o jogador enviasse um comando de que casa que ele gostaria de jogar
#que seria 1,2,3,4... o sistema interpretaria como se fosse nas variáveis b1,b2,b3,b4... e marcando-as.
#===================================================================================================================================================================================================

tabu()
while True:
    if uraraka_san % 2 == 0: x_o ='X'
    else: x_o = 'O'

    print(x_o ,' está jogando')
    jogada = int(input())
    
    if uraraka_san % 2 == 0: x_o ='X'
    else: x_o = 'O'
  
    
    if jogada == 1 and b1 == '1' :
        b1 = x_o

    elif jogada == 2 and b2 == '2' :
        b2 = x_o

    elif jogada == 3 and b3 == '3' :
        b3 = x_o

    elif jogada == 4 and b4 == '4' :
        b4 = x_o

    elif jogada == 5 and b5 == '5' :
        b5 = x_o

    elif jogada == 6 and b6 == '6' :
        b6 = x_o

    elif jogada == 7 and b7 == '7' :
        b7 = x_o

    elif jogada == 8 and b8 == '8' :
        b8 = x_o

    elif jogada == 9 and b9 == '9' :
        b9 = x_o


#=================================================================================Fim da interpretaçao de comandos==================================================================================


#==========================================================================Etapa de vitoria derrota ou VELHA de 'O' ou 'X'==========================================================================
#Bom nessa última parte usamos esse código ‘ uraraka_san = (uraraka_san + 1) ’ para fazer com que o sistema soubesse quando seria a vez de ‘O’ ou ‘X’ marcar no tabuleiro,
#e o resto do código e para saber quando ‘X’ ou ‘O’ fosse ganhar, fizemos todas as formas de como os jogadores poderiam ganhar tanto faz se fosse em horizontal,
#vertical ou diagonal ira sempre sinalizar quem foi o vencedor e quando fosse empatar nós usamos apenas um ‘else’
#que a leitura seria feita assim ‘se não for em horizontal, vertical ou diagonal ira printar ‘Deu Velha’’ poupando o nosso trabalho.
#===================================================================================================================================================================================================

    uraraka_san = (uraraka_san + 1)
    tabu()
    
    if b1 == 'X' and b2 == 'X' and b3 == 'X':
        print ('O X GANHOU')
        break
    if b4 == 'X' and b5 == 'X' and b6 == 'X':
        print ('O X GANHOU')
        break
    if b7 == 'X' and b8 == 'X' and b9 == 'X':
        print ('O X GANHOU')
        break
    if b1 == 'X' and b4 == 'X' and b7 == 'X':
        print ('O X GANHOU')
        break
    if b2 == 'X' and b5 == 'X' and b8 == 'X':
        print ('O X GANHOU')
        break
    if b3 == 'X' and b6 == 'X' and b9 == 'X':
        print ('O X GANHOU')
        break
    if b1 == 'X' and b5 == 'X' and b9 == 'X':
        print ('O X GANHOU')
        break
    if b3 == 'X' and b5 == 'X' and b7 == 'X':
        print ('O "X" GANHOU')
        break

    if b1 == 'O' and b2 == 'O' and b3 == 'O':
        print ('O "O" GANHOU')
        break
    if b4 == 'O' and b5 == 'O' and b6 == 'O':
        print ('O "O" GANHOU')
        break
    if b7 == 'O' and b8 == 'O' and b9 == 'O':
        print ('O "O" GANHOU')
        break
    if b1 == 'O' and b4 == 'O' and b7 == 'O':
        print ('O "O" GANHOU')
        break
    if b2 == 'O' and b5 == 'O' and b8 == 'O':
        print ('O "O" GANHOU')
        break
    if b3 == 'O' and b6 == 'O' and b9 == 'O':
        print ('O "O" GANHOU')
        break
    if b1 == 'O' and b5 == 'O' and b9 == 'O':
        print ('O "O" GANHOU')
        break
    if b3 == 'O' and b5 == 'O' and b7 == 'O':
        print ('O "O" GANHOU')
        break


    if uraraka_san == 9:
        print('Deu velha')
        break

#====================================================================================Fim da etapa de vitoria/derrota=================================================================================
   


