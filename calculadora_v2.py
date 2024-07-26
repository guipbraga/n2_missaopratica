saida = ''
def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
        if a == 0 or b == 0:
            return'Não foi possível realizar a divisão por 0'
        else:
            return a / b        
def calculadora(operacao, num1, num2):
    if operacao == '+':
        resultado = adicao(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"   
    return resultado

while saida.lower() != 'n':
        operacao = input('Escolha uma operação (+, -, *, /): ')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = calculadora(operacao,num1,num2)
        print('Resultado da operação: ',resultado)
        print('Você deseja continuar executando o programa?')
        saida = input('Digite S para SIM e N para NÃO: ')        
print('Você saiu do programa.')










    

