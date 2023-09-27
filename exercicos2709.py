#exercicos01 calcular taxas acima de 50 quilos, 1 quilo = 4 reais.

quilos = int(input("Quantos quilos do peixe: "))
if quilos>50 :
 resto = quilos - 50
 print("Você vai receber:",resto*4,"R$ de taxa.")
else: 
 print("Não tem taxa") 