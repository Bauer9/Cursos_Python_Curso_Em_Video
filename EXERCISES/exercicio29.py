#
# programa que lê a velocidade de um carro, 
# se ele ultrapassar 80km aparece a mensagem que foi multado
# Calcular a multa que é 7 reais para cada KM acima do limite


vel = int (input('Qual a velocidade do carro? '))



if vel > 80:
    print ('Você foi multado!, Você excedel o limimte de 80 km/h')
    print ('A multa é de 7 reais por km excedido!')
    print ('Você vai pagar uma multa de R$ {:.2f}' .format((vel-80)*7))


print ('Tenha um bom dia, dirija com segurança!')
