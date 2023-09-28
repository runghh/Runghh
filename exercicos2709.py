#exercicos01 calcular taxas acima de 50 quilos, 1 quilo = 4 reais.
#quilos = int(input("Quantos quilos do peixe: "))
#if quilos>50 :
# resto = quilos - 50
# print("Você vai receber:",resto*4,"R$ de taxa.")
# print("Peso informado",quilos)
#else: 
# print("Não tem taxa")

#exercicios02 
#calcular salario ganho de horas * horas trabalhadas por mes,
#descontado 11% de imposto de renda 8% de INSS e 5% para o sindicato


#receber = int(input("Quantos voce recebe por hora? "))
#horas = int(input("Quantos horas voce trabalha por mes? "))

#salario= receber*horas
#ir=salario*(8/100)
#inss=salario*(11/100)
#sindicato=salario*(5/100)

#print("Salario bruto: ",salario,"R$")
#print("Imposto de Imposto de renda:",ir,"R$")
#print("Imposto de INSS: ",inss,"R$")
#print("Imposto de sindicato:",sindicato,"R$")
#print("Salario liquido:",salario-inss-ir-sindicato,"R$")

#Exerciso03 
#tamanho do arquivo para downloado em MB e a velocidade de um link de internet em Mbps
#calcule e informe o tempo aproximado de download do arquivo usando este link em minutos

#mb = int(input("Quantos MB seu arquivo tem? "))
#mbps = int(input("Qual a sua velocidade em internet em Mbps? "))

#trans = mb * 8
#seg = trans/mbps
#print(seg,"minutos.")

#Exercicios04
#distancia em km/h

distancia = float(input("Digite a distância em quilômetros: "))
vm = float(input("Digite a velocidade média em km/h: "))


tempo = distancia / vm
horas = int(tempo)

restominutos = (tempo - horas)
minutos = restominutos * 60
minutos = int(minutos)

restosegundo = (60*(minutos-(60*restominutos)))
restosegundo = int(restosegundo)


print(tempo)
print("Tempo estimado de viagem:",horas," horas",minutos," minutos",restosegundo,"segundos.")

#inverso em tempo de distancia