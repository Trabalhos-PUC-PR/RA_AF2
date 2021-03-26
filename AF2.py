import numpy as np
escolha = int(input("Digite o N° do Exercício: "))

#Elabore um algoritmo e a app para ler dois valores inteiros, somar e imprimir o resultado.
if(escolha == 1):
    numeroum = int(input("Digite um Número Inteiro: "))
    numerodois = int(input("Digite outro Número inteiro: "))
    soma = numeroum + numerodois
    print("A soma é",soma)

#Elaborar um algoritmo a app para ler dois valores reais e multiplicar um pelo outro, imprimindo o resultado.
if(escolha == 2):
    numeroum = float(input("Digite um Número: "))
    numerodois = float(input("Digite outro Número: "))
    produto = numeroum * numerodois
    print("O produto é",produto)

#Elaborar um algoritmo a app que leia um valor inteiro e positivo, imprimindo o quadrado desse número.
if(escolha == 3):
    numeroum = int(input("Digite um Número Inteiro Positivo: "))
    while(numeroum<0):
        numeroum = int(input("Digite um Número Inteiro *Positivo* Novamente: "))
    quadrado = numeroum ** 2
    print("O quadrado do" ,numeroum, "é" ,quadrado)

#Elaborar um algoritmo a app para calcular e imprimir a raiz quadrada de um número inteiro e positivo lido. 
if(escolha == 4):
    numeroum = int(input("Digite um Número Inteiro positivo: "))
    while(numeroum<0):
        numeroum = int(input("Digite um Número Inteiro *Positivo* Novamente: "))
    raiz = np.sqrt(numeroum) 
    print("A raiz do" ,numeroum, "é" ,raiz)

#Elaborar um algoritmo a app para ler duas cadeias de carecteres e imprimir a concatenação de ambas.
if(escolha == 5):
    stringum = input("Digite qualquer coisa: ")
    stringdois = input("Digite outra qualquer coisa: ")
    print(stringum,stringdois)

#Elaborar um algoritmo a app que leia um número inteiro de quatro dígitos e imprima, separadamente, a unidade, a dezena, a centena e a milhar.
if(escolha == 6):
    numeroum = int(input("Digite um Número Inteiro de 4 digitos: "))
    numerodois = numeroum/1000 #ele divide aqui pra ver se tem 4 digitos ou mais, se tiver 3 ou menos o resultado é menor que 1
    if(numerodois>=1):
        print ("O digito dos milhares é: ", (numeroum//1000)%10) #não importa o quão grande o valor seja, dividindo por 1000 leva a casa do milhar pra unidade, a unica que não é divisivel por 10
        print ("O digito das centenas é: ", (numeroum//100)%10) #digamos 1234, 1234/100 = 12.34, pegando só o inteiro, 12, dividindo por 10 e pegando o resto, 2
        print ("O digito das dezenas é: ", (numeroum//10)%10) #digamos 1234, 1234/10 = 123.4, pegando só o inteiro, 123, dividindo por 10 e pegando o resto, 3
        print ("O digito das unidades é: ",(numeroum//1)%10) #a mesma coisa ali de cima, só que aqui em baixo

        #achei interessante comentar aqui por que as vezes pode ficar meio confuso :D

#Elaborar um algoritmo a app para calcular e imprimir o volume de uma esfera, sendo que o raio da esfera deve ser lido. 
if(escolha == 7):
    raio = int(input("Digite um raio para a esfera: "))
    volume = (4 * np.pi * raio ** 3) / 3
    print(volume ,"alguma coisa, não tem unidade de medida espeficicada...")