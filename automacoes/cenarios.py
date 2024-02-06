
class Cenarios:

    def __init__(self) -> None:
        self.cenarios = {
            "inputUsuario":"page.goto('https://github.com')"  
        }
page.locator("text=Sign in").click()