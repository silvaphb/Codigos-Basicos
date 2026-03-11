# Calcular IMC e verificar o mesmo

peso: float 
altura: float
imc: float
status: str

print("*** CALCULADORA DE IMC ***\n")
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira agora sua altura: '))
imc = peso / (altura * 2)
if (imc < 18.5):
    status = 'Muito Magro!'
elif (imc > 18.5) and (imc < 24.9):
    status = 'Normal'
elif (imc > 25.0) and (imc < 29.9):
    status = 'Sobrepeso'
elif (imc > 30.0) and (imc < 34.9):
    status = 'Obeso grau I'
elif (imc > 35.0) and (imc < 39.9):
    status = 'Obeso grau II'
elif (imc > 40):
    status = 'Obeso grau III / Morbido'

print(f'Seu IMC: {int(imc)}')
print(f'Status: {status}')

#||||||||||||||||||||||||||||||||||||||||||||||
#||                                          ||
#||             JEFFERSON SILVA              ||
#||                                          ||
#||||||||||||||||||||||||||||||||||||||||||||||