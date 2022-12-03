from time import sleep as s
from random import randint as r
print('pedra, papel, tesoura')
print('=-'*12)
sair=True
pontu=0
pontpc=0
empad=0
itens=(("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""),
("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""),
("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
)
while sair:
    if pontu == 5:
        input("parabéns!, você está com 5 pontos")
    if pontpc == 5:
        input("você tá perdendo! de 5 à {}, dá a volta por cima miga".format(pontu))
    elif pontu == 8:
        input('Perdi as contas de quantos pontos você fez, mas o pc não. Você está com 8 pontos')
    elif pontpc == 8:
        input('Você está perdendo de 8 à {}, vamo lá, coraje'.format(pontu))
    print("""Escolha uma dessas:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    [3] Ver Pontuação
    [Digite um número maior que 3 para sair] """)
    print('=-'*12)
    esc=int(input('Qual você quer? '))
    if esc>= 4:
        input('Tchau! ')
        break
    while esc == 3:
        print('=-'*12)
        print('A sua pontuação atual é de {}'.format(pontu))
        print('A pontuação do pc é de {}'.format(pontpc))
        print('E deu empate {} vez'.format(empad))
        if empad > 1:
            print('E deu empate {} vezes'.format(empad))
        print('=-'*12)
        esc=int(input("""Escolha uma dessas:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    [3] Ver Pontuação
    [Digite um número maior que 3 para sair] """))
        if esc>= 4:
            input('Tchau! ')
            break
    pc=r(0,2)
    if esc >= 4:
        break
    if esc <= 3:
        print('ja')
        s(1)
        print('quem')
        s(1)
        print("pô")
        print('O computador jogou {} '.format(itens[pc]))
        print('Você jogou {} '.format(itens[esc]))
        if pc == 0:
            if esc==1:
                print('Papel embrulha Pedra')
                input("Você venceu! ")
                pontu+=1
            elif esc==2:
                print('Pedra quebra Tesoura')
                input('você perdeu! ')
                pontpc+=1
            elif esc==0:
                print('Pedra com Pedra dá em nada')
                input('Empate! ')
                empad+=1
        if pc == 1:
            if esc==1:
                print('Papel com Papel dá em nada')
                input('Empate! ')
                empad+=1
            if esc == 0:
                print('Papel embrulha Pedra')
                input('Você perdeu! ')
                pontpc+=1
            if esc == 2:
                print('Tesoura corta Papel')
                input('Você ganhou! ')
                pontu+=1
        if pc == 2:
            if esc == 0:
                print('Pedra quebra Tesoura')
                input('Você ganhou! ')
                pontu+=1
            if esc == 1: 
                print('Tesoura corta Papel')
                input('Você perdeu! ')
                pontpc+=1
            if esc == 2:
                print('Tesoura com Tesoura dá em nada')
                input('Empate! ')
                empad+=1
            print('=-'*12)
       
        
    
    
