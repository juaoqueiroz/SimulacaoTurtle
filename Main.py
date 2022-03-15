#Importação das bibliotecas para o projeto 
import turtle
import time
import random
from turtle import *
from random import *
from time   import *

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
    desenha_barragem.hideturtle()
    desenha_barragem.goto(270, 0)
    desenha_barragem.pendown()
    desenha_barragem.fillcolor("green")
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
    

#movimentando os peixes 
def movimentar_peixes():
    for peixe in peixes1:
        angulo = randint(-30,30)
        x,y = peixe.pos()
        movimenta = randint(15,30)
        peixe.forward(movimenta)
        peixe.setheading(angulo)
        limitar_tela(peixe,x,y)
        testar_passagem(x,y,peixe)
       
contador_a = 0
contador_b = 0
#testando se o peixe passou pela barragem 
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
        

#limitando para que os peixes não ultrapassem a tela
def limitar_tela(peixe,x,y):
    if y >  altura/2-40:
        peixe.setheading(-40)
        peixe.forward(20)
    if y < -altura/2+40:
        peixe.setheading(40)
        peixe.forward(20)

#escrevendos as informações que aparecerão na tela
def escrever_info(contador):
    fonte1 = ("Comic Sans", 10, "italic")
    contador.clear()
    contador.write("PASSARAM POR A: {}   PASSARAM POR B: {}".format(contador_a,contador_b), False, "center", fonte1)

    
       




#Definindo os objetos da simulação, que nesse caso vão ser peixes
register_shape("peixe.gif")

peixes1 = []
desenhar_limites()
desenhar_barragens()

contador = turtle.Turtle()
contador.hideturtle()
contador.penup()
contador.goto(120,-250)
contador.pendown()


while True:
    tela.update()
    n1 = len(peixes1) #numero de peixes do tipo 1 ativos na tela
    if n1<5:
        peixe = turtle.Turtle()
        peixe.hideturtle()
        peixe.shape("peixe.gif")
        peixe.penup()
        peixe.goto(-350,randint(-280,280))
        peixe.showturtle()
        peixes1.append(peixe)
    movimentar_peixes()
    escrever_info(contador)
    






