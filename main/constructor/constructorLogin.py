from sistemaBancario.views.viewLogin import ViewLogin
from sistemaBancario.controller.controllerLogin import ControllerLogin


def constructorLogin():
    telaLogin = ViewLogin()
    controllerLogin = ControllerLogin(telaLogin)

    return telaLogin
