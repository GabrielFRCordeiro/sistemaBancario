from flet import (AppBar, IconButton, icons, PopupMenuItem,
                  Image, PopupMenuButton)
from sistemaBancario.utils.paletaCores import CoresAplicacao


class ViewBar(AppBar):
    def __init__(self):
        super().__init__()
        self.cores = CoresAplicacao()
        self.logo = Image(src='logofi.png')
        self.btnCadastrar = PopupMenuItem(icon=icons.ASSIGNMENT_IND, text='Cadastrar')
        self.btnOperacoes = PopupMenuItem(icon=icons.CURRENCY_EXCHANGE, text='Operações')
        self.btnRelatorio = PopupMenuItem(icon=icons.AREA_CHART_OUTLINED, text='Relatório')
        self.menu = PopupMenuButton(
            items=[
                self.btnOperacoes,
                self.btnCadastrar,
                self.btnRelatorio
            ]
        )
        self.btnVoltar = IconButton(icon=icons.LOGOUT, icon_color=self.cores.corPrimaria)
        self.leading = self.btnVoltar
        self.title = self.logo
        self.actions = [self.menu]
        self.center_title = True
