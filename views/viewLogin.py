from flet import (UserControl, Text, Image, TextField, ElevatedButton, ButtonStyle,
                  MaterialState, RoundedRectangleBorder, ResponsiveRow, Column, MainAxisAlignment,
                  alignment, Row)
from sistemaBancario.utils.paletaCores import CoresAplicacao

class ViewLogin(UserControl):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.titulo = Text('Login', size=30, color=self.cores.corPrimaria)
        self.img_login = Image('img_login.png')
        self.t_field_login = TextField(label='Login')
        self.t_field_senha = TextField(label='Senha', password=True, can_reveal_password=True)
        self.btn_enter = ElevatedButton('Entrar', expand=True, style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                }, shape=RoundedRectangleBorder(radius=5)
                                            ), width=300, height=45)

    def build(self):
        linhaBtnEntrar = Row(col={'xs': 6, 'sm': 2, 'md': 3},
                             controls=[self.btn_enter])
        layout = ResponsiveRow(
            controls=[
                Column(col={'xs': 10, 'sm': 8, 'md': 6, 'lg': 5, 'xl': 3},
                       controls=[
                        Column(col={'xs': 6, 'sm': 2, 'md': 1, 'lg': 2, 'xl': 1},
                               controls=[self.img_login],
                               alignment=alignment.center),
                        Column(col={'sm': 12, 'md': 8},
                               controls=[self.titulo,
                                         self.t_field_login,
                                         self.t_field_senha,
                                         linhaBtnEntrar
                                         ])  # fim da coluna do campo de entrada em botoes
                    ], alignment=MainAxisAlignment.CENTER
                )  # fim da minha coluna principal
            ], alignment=MainAxisAlignment.CENTER
        )  # fim da minha linha responsiva

        return layout
