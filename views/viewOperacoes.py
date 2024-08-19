from flet import (UserControl, Image,
                  ElevatedButton, ResponsiveRow, Column,
                  MainAxisAlignment, Text,
                  ButtonStyle, MaterialState, RoundedRectangleBorder,
                  DataTable, DataColumn, icons)
from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewOperacoes(UserControl):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()

        self.img_cadastro = Image(src='img_login.png')
        self.btn_depositar = ElevatedButton(text='DEPOSITAR',
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                }, shape=RoundedRectangleBorder(radius=5)
                                            ), width=300, height=45, icon=icons.ARROW_CIRCLE_DOWN)
        self.btn_sacar = ElevatedButton(text='SACAR',
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                    MaterialState.DEFAULT: self.cores.corDefault,
                                                    MaterialState.HOVERED: self.cores.corHover
                                                }, shape=RoundedRectangleBorder(radius=5)
                                            ), width=300, height=45, icon=icons.ARROW_CIRCLE_UP)

        self.table_operacoes = DataTable(
            width=800,
            columns=[
                DataColumn(Text('LOGIN')),
                DataColumn(Text('EMAIL')),
                DataColumn(Text('TELEFONE')),
                DataColumn(Text('OPERACAO')),
                DataColumn(Text('SALDO'))
            ]
        )


    def build(self):
        linha1 = ResponsiveRow(controls=[
            Column(col={'sm': 8, 'md': 2}, controls=[self.img_cadastro])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 1
        linha2 = ResponsiveRow(controls=[
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 3}, controls=[self.btn_depositar]),
            Column(col={'xs': 12, 'sm': 10, 'md': 4, 'lg': 3}, controls=[self.btn_sacar])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 2
        linha3 = ResponsiveRow(controls=[
            Column(col={'xs': 12, 'sm': 10, 'md': 8, 'lg': 8}, controls=[self.table_operacoes])
        ], alignment=MainAxisAlignment.CENTER)  # final da linha 3

        return Column(controls=[
            linha1, linha2, linha3
        ])
