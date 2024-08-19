from flet import app, WEB_BROWSER
from sistemaBancario.main.handle_process import start

app(start, assets_dir='assets', view=WEB_BROWSER)
