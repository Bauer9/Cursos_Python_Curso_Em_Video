# converter metros em centimetros e milimetros
n1 = float (input('Digite o número em metros'))

cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000

print ('A medida de {} \nEm centímetros é {:.0f}cm \nEm milímetros é: {:.0f}mm'.format(n1, cm, mm))

print('A medida {} \nEm km é {}km'.format(n1, km))






