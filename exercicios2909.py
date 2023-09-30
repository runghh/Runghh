
#arry

#exemplo 1
#pessoa = ["A","B","C","D","E"]
#tel = [1,2,3,4,5]

#for i in range(len(tel)):
# print("Nome:",pessoa[i],"telefone",tel[i])

#exemplo 2 arry/media

#nota = [7,7,7,7]
#soma = 0

#for i in range(len(nota)):

#  soma = soma + nota[i] 

#media = soma/4
#print(media)

#if media >= 7 :
# print("Aprovado")
#else:
# print("Reprovado")

#arry input

#numero = []
#for i in range(5):
#  num = int(input("Digite um numero:"))
#  numero.append(num) 
#for b in range(len(numero)):
#  print(numero[b])

#leia 10 numeros inteiros e amarzene no vetor, 
#crie vetor impar e par e imprima os 3 

#num = []
#par = []
#impar = []

#for i in range(10):
 
# numero = int(input("Digite um numero:"))
# num.append(numero)
# if numero % 2 == 0:
#    par.append(numero)
# else:
#    impar.append(numero)

#print("Numeros Digitado:",num)
#print("Numeros Pares:",par)
#print("Numeros Impares:",impar)

#exercicio 2
 # faça um programa que peça as quatro notas de 5 alunos calcule e armazene num vetor a media de cada aluno,
 # imprima o numero de alunos com media maior ou igual a 7

notas = []
media = []
ap = []
re = []
calc = 0
md = 0


for i in range(1,6):
    print("------------------------------")
    print("Nota Aluno do aluno",i)

    for b in range(1,5):
      
       print("Nota",b)
       nota = int(input("Digite a Nota Do aluno: "))
       calc += nota 

    md = calc/4
    media.append(md)

    if md >= 7:
      ap.append(i)
    else:
      re.append(i)
    calc = 0
    nota = 0

print("Alunos aprovado:",ap)
print("Alunos reprovado:",re)
print("Media de todos os alunos:",media)


