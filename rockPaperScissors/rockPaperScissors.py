import time
from random import randint
option = int(input("\n\nVamos jogar Pedra, Papel, Tesoura?\n\nPor favor escolha um modo:\n1-Honesto\n2-Sempre Ganha\n3-Sempre Perde\n"))
if option == 1:    
    opOut = ''
    maq=hum=emp=0
    while opOut in ('Ss'):
        opM = randint(1,3)
        opH = int(input("Digite sua opção:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
        if opH == 1:
            human = 'Pedra'
        elif opH == 2:
            human = 'Papel'
        elif opH == 3:
            human = 'Tesoura'            
        if opM == 1:
            machine = 'Pedra'
        elif opM == 2:
            machine = 'Papel'
        elif opM == 3:
            machine = 'Tesoura'        
        if machine == human:
            print(f'Máquina {machine}--Humano {human}-->Empatou\n')
            emp=emp+1
        elif machine == 'Pedra':
            if human == 'Papel':
                print(f'Máquina {machine}--Humano {human}-->Humano Ganhou\n')
                hum=hum+1
            elif human == 'Tesoura':
                print(f'Máquina {machine}--Humano {human}-->Máquina Ganhou\n')
                maq=maq+1
        elif machine == 'Papel':
            if human == 'Pedra':
                print(f'Máquina {machine}--Humano {human}-->Máquina Ganhou\n')
                maq=maq+1
            elif human == 'Tesoura':
                print(f'Máquina {machine}--Humano {human}-->Humano Ganhou\n')
                hum=hum+1
        elif machine == 'Tesoura':
            if human == 'Pedra':
                print(f'Máquina {machine}--Humano {human}-->Humano Ganhou\n')
                hum=hum+1
            elif human == 'Papel':
                print(f'Máquina {machine}--Humano {human}-->Máquina Ganhou\n')
                maq=maq+1
        opOut = input('Continuar?[S/N]')
        if opOut in 'Nn':
            break
elif option == 2:    
    opOut = ''
    maq=hum=emp=0
    while opOut in ('Ss'):
        opH = int(input("Digite sua opção:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
        if opH == 1:
            human = 'Pedra'
            machine = 'Tesoura'            
        elif opH == 2:
            human = 'Papel'
            machine = 'Pedra'
        elif opH == 3:
            human = 'Tesoura'
            machine = 'Papel'   
        print(f'Máquina {machine}--Humano {human}-->Humano Ganhou\n') 
        hum=hum+1        
        opOut = input('Continuar?[S/N]')
        if opOut in 'Nn':
            break
elif option == 3:    
    opOut = ''
    maq=hum=emp=0
    while opOut in ('Ss'):
        opH = int(input("Digite sua opção:\n1-Pedra\n2-Papel\n3-Tesoura\n"))
        if opH == 1:
            human = 'Pedra'
            machine = 'Papel'            
        elif opH == 2:
            human = 'Papel'
            machine = 'Tesoura'
        elif opH == 3:
            human = 'Tesoura'
            machine = 'Pedra'   
        print(f'Máquina {machine}--Humano {human}-->Máquina Ganhou\n') 
        maq=maq+1        
        opOut = input('Continuar?[S/N]')
        if opOut in 'Nn':
            break
print('=*'*20) 
titulo = 'Fim do Jogo - PLACAR'
print(titulo.center(40,'*'))
print(f'Empates = {emp}\nVitórias = {hum}\nDerrotas = {maq}')   
print('=*'*20)
