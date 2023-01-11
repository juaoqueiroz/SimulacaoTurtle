#Importação das bibliotecas para o projeto 
import turtle
import time
import random
from turtle import *
from random import *
from time   import *

"""
Esse programa tem o objetivo de simular um fluxo de peixes em uma empresa de psicultura, 
que possui duas barragens de conteção para recolher os peixes do rio

"""
#Definindo as dimensões da tela
altura = 600 
largura = 800

#Definindo a tela
tela = turtle.Screen()
tela.title("SIMULADOR PARA SISTEMA DE PISCICULTURA ")
tela.bgcolor("blue")
tela.setup(width=largura, height=altura)
tela.tracer(1)

#desenhando os limites da tela
def desenhar_limites():
    limite_tela = turtle.Turtle()
    limite_tela.speed(0)
    limite_tela.penup()
    limite_tela.pensize(15)
    limite_tela.hideturtle()
    limite_tela.goto(-largura/2+15, altura/2-15)
    limite_tela.pendown()
    limite_tela.goto(largura/2-20, altura/2-15)
    limite_tela.goto(largura/2-20, -altura/2+20)
    limite_tela.goto(-largura/2+15, -altura/2+20)
    limite_tela.goto(-largura/2+15, altura/2-15)

#desenhando as barragens 
def desenhar_barragens():
    desenha_barragem = turtle.Turtle()
    desenha_barragem.speed(0)
    desenha_barragem.penup()
    desenha_barragem.pensize(5)
    desenha_barragem.pencolor("ghost white")
    desenha_barragem.hideturtle()
    desenha_barragem.goto(270, 0)
    desenha_barragem.pendown()
    desenha_barragem.fillcolor("lime green")
    desenha_barragem.begin_fill()
    desenha_barragem.goto(270, 260)
    desenha_barragem.goto(350, 260)
    desenha_barragem.goto(350, -260)
    desenha_barragem.goto(270, -260)
    desenha_barragem.goto(270, 0)
    desenha_barragem.end_fill()
    desenha_barragem.goto(350,0)
    escrever_conteudo()

#escrevendo a identificacao das barragens
def escrever_conteudo():
    fonte1 = ("Comic Sans", 10, "italic")
    fonte2 = ("Comic Sans", 50, "normal")
    caneta = turtle.Turtle()
    caneta.speed(0)
    caneta.right(90)
    caneta.hideturtle()
    caneta.penup()
    caneta.goto(310,240)
    caneta.write("Barragem", False, "center", fonte1)
    caneta.goto(310,100)
    caneta.write("A", False, "center", fonte2)
    caneta.goto(310,-20)
    caneta.write("Barragem", False, "center", fonte1)
    caneta.goto(310,-160)
    caneta.write("B", False, "center", fonte2)
    

""" os peixes se movimentam de maneira randomica na tela, com a função randint
para dar a base desse movimento. Que será pra frente com alteração nos angulos
"""
#movimentando peixes
def movimentar_peixes():
    for peixe in peixes1:
        angulo = randint(-30,30)
        x,y = peixe.pos()
        movimenta = randint(15,30)
        peixe.forward(movimenta)
        peixe.setheading(angulo)
        testa_ataque(peixe)
        limitar_tela(peixe,x,y)
        testar_passagem(x,y,peixe)
""" o jacaré segue um padrão de movimento com alteração no quanto ele vai pra frente atraves do randint
    quando o jacaré chega ao fim da tela ele volta para o início em uma outra posição
"""
#movimentando o jacare
def movimentar_jacare(jacare):
    jacare.shape("jacare.gif")
    movimenta = randint(25,60)
    x,y = jacare.pos()
    jacare.forward(movimenta)
    posicao = randint(-250, 250)
    if x >= 230:
        jacare.hideturtle()
        jacare.setpos(-300, posicao)
        jacare.showturtle()

"""
se a distância do peixe para o jacaré for menor que 50 pixels, o peixe é atacado 
e o turtle removido. há uma mudança no .shape do jacaré para destacar o ataque
"""


#testando a distancia do peixe para o jacare para ver se houve um ataque
peixes_atacados = 0 #essa variável armazena o número de peixes que forma atacados
def testa_ataque(peixe):
    global peixes_atacados
    distancia = peixe.distance(jacare)
    if distancia < 50:
        jacare.shape("jacare2.gif")
        peixe.hideturtle()
        peixes1.remove(peixe)
        n1 = len(peixes1)
        peixes_atacados+=1
     
"""
as barragens são limite para os peixes, caso eles passem por uma delas é contada a passagem e o peixe
é removido da tela
"""  

#testando se o peixe passou pela barragem 
contador_a = 0 #essa variável armazena a quantidade de peixes que passaram pela barragem A
contador_b = 0 #essa variável armazena a quantidade de peixes que passaram pela barragem B
def testar_passagem(x,y,peixe):
    global contador_a, contador_b
    if x > 270 and 0<y<=260:
        peixe.hideturtle()
        peixes1.remove(peixe)
        n1 = len(peixes1)
        contador_a +=1
    if x > 270 and -260<y<0:
        peixe.hideturtle()
        peixes1.remove(peixe)
        n1 = len(peixes1)
        contador_b +=1
        

#limitando para que os peixes não ultrapassem os limites superiores e inferiores da tela
def limitar_tela(peixe,x,y):
    if y >  altura/2-40:
        peixe.setheading(-40)
        peixe.forward(20)
    if y < -altura/2+40:
        peixe.setheading(40)
        peixe.forward(20)

"""
na tela aparecerão os contadores de quantos peixes passaram em cada barragem e a quantidade 
de peixes que foram atacados
"""
#escrevendos as informações que aparecerão na tela
def escrever_info(contador):
    fonte1 = ("Comic Sans", 10, "italic")
    contador.clear()
    contador.write("PASSARAM POR A: {}   PASSARAM POR B: {}   PEIXES ATACADOS: {}".format(contador_a, contador_b, peixes_atacados ), False, "center", fonte1)

  


#Definindo os objetos da simulação, que nesse caso vão ser peixes e um jacaré
register_shape("peixe.gif")
register_shape("jacare.gif")
register_shape("jacare2.gif")
jacare = turtle.Turtle()
jacare.shape("jacare.gif")
jacare.penup()
jacare.goto(-300, 250)


peixes1 = [] #essa lista armazena o turtle de cada peixe da simulação

#chamando as funções que irão desenhar o ambiente da simulação
desenhar_limites()
desenhar_barragens()

#definindo o objeto contador que será responsável por escrever e atualizar as informações na tela
contador = turtle.Turtle()
contador.hideturtle()
contador.pencolor("white")
contador.penup()
contador.goto(-50,-250)
contador.pendown()

"""
esse é o loop principal do código em que as funções que precisam de recorrencia serão chamadas,
nesse loop também é criada um novo objeto para os peixes sempre algum deles é removido e adiciona
esse objeto à lista 
"""

limite_peixes = 15 #essa variável armazena a quantidade limite de peixes na tela ao mesmo tempo
#loop principal
while True:
    tela.update()
    n1 = len(peixes1) #essa variável armazena o tamanho da lista de peixes
    if n1<limite_peixes:
        peixe = turtle.Turtle()
        peixe.hideturtle()
        peixe.shape("peixe.gif")
        peixe.penup()
        peixe.goto(-350,randint(-280,280))
        peixe.showturtle()
        peixes1.append(peixe)
    movimentar_peixes()
    movimentar_jacare(jacare)
    escrever_info(contador)
    






