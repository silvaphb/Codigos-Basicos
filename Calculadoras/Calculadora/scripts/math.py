

class Math():
    def __init__(self):
        pass

    def calcular(self, calculo: str):
        if '+' in calculo:
            data = calculo.split('+')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            n2 = float(data[1]) if '.' in data[1] else int(data[1])
            return n1 + n2
        elif '-' in calculo:
            data = calculo.split('-')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            n2 = float(data[1]) if '.' in data[1] else int(data[1])
            return n1 - n2
        elif '*' in calculo:
            data = calculo.split('*')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            n2 = float(data[1]) if '.' in data[1] else int(data[1])
            return n1 * n2
        elif '/' in calculo:
            data = calculo.split('/')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            n2 = float(data[1]) if '.' in data[1] else int(data[1])
            return n1 / n2
        elif '%' in calculo:
            data = calculo.split('%')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            n2 = float(data[1]) if '.' in data[1] else int(data[1])
            return n1 % n2
        elif 'x²' in calculo:
            data = calculo.split('x²')
            n1 = float(data[0]) if '.' in data[0] else int(data[0])
            return n1 * n1
        else:
            return print('Operador invalido!')
        