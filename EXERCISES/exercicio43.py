"""
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida

"""

peso = float (input ('Qual o seu peso? (kg) '))
altura = float (input ('Qual a sua altura? (m) '))

imc = peso /  (altura ** 2) # ou  (altura * altura)

if imc < 18.5 :
    print ('Seu IMC é {:.1f}, Abaixo do Peso' .format(imc))
elif 18.5 <= imc < 25 :  # METODO MELHOR PARA ESCREVER, MAIS SIMPLIFICADO ESSE MAIOR ERA O MEU # imc >= 18.5  and imc < 25 :
    print ('Seu IMC é {:.1f}, Peso Ideal' .format(imc))
elif 25 <= imc < 30 :
    print ('Seu IMC é {:.1f}, Sobrepeso' .format(imc))
elif 30 <= imc < 40 :
    print ('Seu IMC é {:.1f}, Obesidade' .format(imc))
elif imc >= 40 :
    print ('Seu IMC é {:.1f}, Obesidade Mórbida' .format(imc))


