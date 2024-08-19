from sistemaBancario.views.viewBar import ViewBar

class ControllerBarMenu:
    def __init__(self, viewBar: ViewBar) -> None:
        self.barraMenu = viewBar
        self.voltar = viewBar.btnVoltar
        self.btnOperacoes = viewBar.menu.items[0]
        self.btnCadastrar = viewBar.btnCadastrar
        self.btnRelatorio = viewBar.btnRelatorio
        self.btnOperacoes.on_click = self.trocarDePagina_operacoes
        self.btnCadastrar.on_click = self.trocarDePagina_cadastrar
        self.btnRelatorio.on_click = self.trocarDePagina_relatorio

    def trocarDePagina_operacoes(self, e):
        self.barraMenu.page.go('/operacoes')

    def trocarDePagina_cadastrar(self, e):
        self.barraMenu.page.go('/cadastrar')

    def trocarDePagina_relatorio(self, e):
        self.barraMenu.page.go('/relatorio')
