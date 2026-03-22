import flet as ft
import scripts.dados as Dados
import scripts.math as Calculadora

class BotaoNumerico(ft.ElevatedButton):
    def __init__(self, page: ft.Page, label: ft.Text, numero):
        super().__init__()
        self.label: ft.Text = label
        self.numero = numero

        self.bgcolor = ft.Colors.GREY_700
        self.on_click = self.on_clicker
        #self.style = ft.ButtonStyle(
            #shape=ft.RoundedRectangleBorder(10),
            #padding=10
        #)
        #self.text = str(numero)
        self.content = ft.Text(
            str(numero),
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
    
    def on_clicker(self, e :ft.ControlEvent):
        if type(self.label.value) is int:
            self.label.value = str(self.numero)
        else:
            self.label.value += str(self.numero)
        e.page.update()

class BotaoResult(ft.ElevatedButton):
    def __init__(self, page: ft.Page, label: ft.Text, dados: Dados.Pilha):
        super().__init__()
        self.label: ft.Text = label
        self.dados: Dados.Pilha = dados

        self.bgcolor = ft.Colors.GREEN
        self.on_click = self.on_clicker
        #self.text = '='
        self.content = ft.Text(
            '=',
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
    
    def on_clicker(self, e :ft.ControlEvent):
        calculadora = Calculadora.Math()
        result = calculadora.calcular(self.label.value)
        self.label.value = result
        print(self.dados.dados, result)
        e.page.update()

class BotaoClear(ft.ElevatedButton):
    def __init__(self, page: ft.Page, label: ft.Text):
        super().__init__()
        self.label: ft.Text = label

        self.bgcolor = ft.Colors.GREY_900
        self.on_click = self.on_clicker
        #self.text = 'CE'
        self.content = ft.Text(
            'CE',
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
    
    def on_clicker(self, e :ft.ControlEvent):
        self.label.value = ''
        e.page.update()

class BotaoOperador(ft.ElevatedButton):
    def __init__(self, page: ft.Page, label: ft.Text, operador, dados: Dados.Pilha):
        super().__init__()
        self.label: ft.Text = label
        self.operador = operador
        self.dados: Dados.Pilha = dados

        self.bgcolor = ft.Colors.GREY_900
        self.on_click = self.on_clicker
        self.col = {
            ft.ResponsiveRowBreakpoint.XS: 3,
            ft.ResponsiveRowBreakpoint.MD: 6,
            ft.ResponsiveRowBreakpoint.LG: 3
        }
        #self.text = 'X'
        self.content = ft.Text(
            str(self.operador),
            size=16,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        )
    
    def on_clicker(self, e: ft.ControlEvent):
        if type(self.label.value) is int:
            #self.dados.addDado(int(self.label.value))
            #self.dados.addDado(str(self.operador))
            self.label.value = str(self.label.value) + str(self.operador)
        else:
            self.label.value += str(self.operador)
        e.page.update()

class BotaoDelete(ft.ElevatedButton):
    def __init__(self, page: ft.Page, label: ft.Text):
        super().__init__()
        self.label: ft.Text = label

        self.bgcolor = ft.Colors.GREY_900
        self.on_click = self.on_clicker
        self.col = {
            ft.ResponsiveRowBreakpoint.XS: 3,
            ft.ResponsiveRowBreakpoint.MD: 6,
            ft.ResponsiveRowBreakpoint.LG: 3
        }
        #self.text = 'AAA'
        self.content = ft.Icon(
            icon=ft.Icons.BACKSPACE
        )
    
    def on_clicker(self, e :ft.ControlEvent):
        self.label.value = str(self.label.value)[:-1]
        
        e.page.update()