import flet as ft
from flet import Checkbox, Column, ElevatedButton, Row, Text, TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    # Configurações da página
    page.title = 'Cadastro'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # Campos de Cadastro
    text_username: TextField = TextField(label='Nome de Usuário', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Senha', text_align=ft.TextAlign.LEFT, width=200, password=True)
    Checkbox_signup: Checkbox = Checkbox(label='Aceitar Termos', value= False)
    button_submit: ElevatedButton = ElevatedButton(text='Cadastrar', width=200, disabled=True)

    # Função para validar preenchimento dos campos
    def validate(e: ControlEvent) -> None: 
        """Valida se todos os campos foram preenchidos corretamente."""
        if all([text_username.value, text_password.value, Checkbox.value]):
            button_submit.disabled = False
        else: 
            button_submit.disabled = True 
        page.update()

    # Função para submeter cadastro
    def submit(e: ControlEvent) -> None:
        """Submete o cadastro e exibe mensagem de boas-vindas."""
        print('Nome de Usuário:', text_username.value)
        print('Senha:', text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Bem-vindo: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # Atribuição de eventos às funções de validação
    Checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit 

    # Adiciona os controles à página
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                    text_password,
                    Checkbox_signup,
                    button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == '__main__':
    # Inicia a aplicação
    ft.app(target=main)
