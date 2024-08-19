from sistemaBancario.views.viewCadastro import ViewCadastro
from sistemaBancario.controller.controllerCadastrar import ControllerCasdasrtrar

def constructorCadastrar():
    telaCadastrar = ViewCadastro()
    controllerCadastrar = ControllerCasdasrtrar(telaCadastrar)

    return telaCadastrar
