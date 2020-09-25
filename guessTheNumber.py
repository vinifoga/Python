import random, time

print("\n\nVamos Jogar?\n\nEu vou escolher um número inteiro entre 1 e 20 e você tem que adivinhar qual é beleza? ")
for x in range(3):
    print("Pensando...")
    time.sleep(1)
n = random.randint(1,20)
chute = int(input("Beleza, vamos ver se você adivinha, que número eu escolhi? "))
while n != chute:
    if n < chute:
        chute = ''
        chute = int(input("Quase, vamos tentar denovo, o número é menor "))
    elif n > chute:
        chute = ''
        chute = int(input("Quase, vamos tentar denovo, o número é maior "))
if n == chute:
        print("Parabéns, você acertou!")
        print("O número era",n)
    