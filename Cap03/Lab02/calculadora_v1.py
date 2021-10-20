# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
oper = int(input("Informe 1 - Soma 2 - Subtracao 3 - multiplicacao 3 - divisao 5 potencia 6 - modulo"))
n1 = float(input("Informe o primeiro número "))
n2 = float(input("Informe o segundo número "))
def calc(n1,n2):
  sinal = 0 
  if (oper==1):
    sinal = '+'
   elsif (oper==2):
    sinal = '-'
  if (oper==3):
    sinal = '*'
  if (oper==4):
    sinal = '/'
  if (oper==5):
    sinal = '^'
  if (oper==6):
    sinal = '%'
  calc = n1 + " " + sinal + " " + n2  
 retrn(calc) 
    
     
     
   
     
        


