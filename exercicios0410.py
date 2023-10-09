#faça um programa le duas notas parcias obitirads ao longo de um semestre calc media
#media 
#entre 9.0 10.0 = a 7.5 e 9.0 = B
#entre 6.9 e7.5 C entre 4.0 6.0 = D
#ENTRE 4 E ZERO = E

notas=[]
def calc(notas,media):
    if media >= 9 and media <= 10:
        print("Nota A")
    elif media >= 7.5 and media < 9:
       print("Nota B")
    elif media < 7.5 and media > 6:
        print("Nota C")
    elif media <= 6 and media >= 4:
        print("Nota D")
    elif media >= 0 and media < 4:
        print("Nota E")
    else: 
         print("NOTA INVALIDA") 
    notas.append(media)

notaA= int(input("Digite o valor da PRIMEIRA NOTA:"))
notaB= int(input("Digite o valor da SEGUNDA NOTA:"))

media= (notaA+notaB)/2
calc(notas,media)