from flet import (UserControl, Image, TextField,
                  ElevatedButton, ResponsiveRow, Column,
                  MainAxisAlignment, Text, FontWeight, Row,
                  icons, ButtonStyle, MaterialState, RoundedRectangleBorder)
from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewCadastro(UserControl):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()

        self.img_cadastro = Image(src='img_login.png')
        self.titulo = Text("Cadastrar", size=30, weight=FontWeight.BOLD, color=self.cores.corPrimaria)
        self.t_field_login = TextField(label='Login', icon=icons.LOGIN)
        self.t_field_senha = TextField(label='Senha', password=True, icon=icons.PASSWORD_ROUNDED)
        self.t_field_email = TextField(label='Email', icon=icons.EMAIL_OUTLINED)
        self.t_field_telefone = TextField(label='Telefone', icon=icons.PHONE_IPHONE)
        self.t_field_saldo = TextField(label='Saldo', prefix_text='R$', icon=icons.ATTACH_MONEY)
        self.btn_cadastrar = ElevatedButton(text='CADASTRAR',
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                }, shape=RoundedRectangleBorder(radius=5)
                                            ), width=300, height=45)


    def build(self):
        linha1 = ResponsiveRow(controls=[
            Column(col={'sm': 8, 'md': 2}, controls=[self.img_cadastro])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 1
        linhaTitulo = Row(
            controls=[self.titulo],
            alignment=MainAxisAlignment.CENTER
        )  # final da linha titulo
        linha2 = ResponsiveRow(controls=[
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 5}, controls=[self.t_field_login]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 5}, controls=[self.t_field_senha]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 2}, controls=[self.t_field_saldo]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 5}, controls=[self.t_field_email]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 4}, controls=[self.t_field_telefone]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 3}, controls=[self.btn_cadastrar])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 2

        return Column(controls=[
            linha1, linhaTitulo, linha2
        ])
