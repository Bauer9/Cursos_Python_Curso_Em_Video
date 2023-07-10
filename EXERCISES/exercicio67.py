# tabuada que para quando digitar um valor negativo


resultado = 0
num = 1

while True :
    print ( '=' * 41)
    num = int (input ('Quer ver a tabuada de qual valor? '))
    print ( '=' * 41 )

    if num < 0 :
        break
    
    for t in range (1, 11) :
        resultado = num * t
        print (f'{num} x {t:2} = {resultado:2}')
       
print ('Acabou')
