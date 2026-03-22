import flet as ft
import scripts.dados as Dados
import UI

def main(page: ft.Page):
    # Window config
    page.title = 'Calculadora'
    page.window.full_screen = False
    page.window.width = 400
    page.window.height = 580

    # Util
    label = ft.Text('Olá!', size=42, weight=ft.FontWeight.BOLD)
    dados = Dados.Pilha()

    # Numeric bottons
    bt1 = UI.BotaoNumerico(page, label, 1)
    bt2 = UI.BotaoNumerico(page, label, 2)
    bt3 = UI.BotaoNumerico(page, label, 3)
    bt4 = UI.BotaoNumerico(page, label, 4)
    bt5 = UI.BotaoNumerico(page, label, 5)
    bt6 = UI.BotaoNumerico(page, label, 6)
    bt7 = UI.BotaoNumerico(page, label, 7)
    bt8 = UI.BotaoNumerico(page, label, 8)
    bt9 = UI.BotaoNumerico(page, label, 9)
    bt0 = UI.BotaoNumerico(page, label, 0)

    # Special bottons
    btDL = UI.BotaoDelete(page, label)
    btP = UI.BotaoNumerico(page, label, '.')
    btC = UI.BotaoClear(page, label)
    btR = UI.BotaoResult(page, label, dados)
    btA = UI.BotaoOperador(page, label, '+', dados)
    btMP = UI.BotaoOperador(page, label, '*', dados)
    btM = UI.BotaoOperador(page, label, '-', dados)
    btDV = UI.BotaoOperador(page, label, '/', dados)
    btRT = UI.BotaoOperador(page, label, '%', dados)
    btPT = UI.BotaoOperador(page, label, 'x²', dados)

    # Base style
    visu = ft.Container(
        content=label,
        padding=10,
        width=float('inf'),
        height=100,
        alignment=ft.Alignment.BOTTOM_RIGHT,
        border=ft.Border.all(2, ft.Colors.BLUE),
        border_radius=ft.BorderRadius.all(8)
    )

    grid = ft.GridView(
        width=float('inf'),
        runs_count=4,
        spacing=8,
        controls=[
            bt1,
            bt2,
            bt3,
            btMP, # Multi
            bt4,
            bt5,
            bt6,
            btM, # Menos
            bt7,
            bt8,
            bt9,
            btA, # Adicao
            btP, # Ponto
            bt0,
            btC, # Clear
            btR # Result
        ]
    )

    gridBar = ft.ResponsiveRow(
        width=float('inf'),
        controls=[
            btPT,
            btRT,
            btDV,
            btDL
        ]
    )

    mainColumn = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            visu,
            gridBar,
            grid
        ]
    )

    #page.add(visu)
    #page.add(gridBar)
    page.add(mainColumn)

    page.update()

ft.run(main)