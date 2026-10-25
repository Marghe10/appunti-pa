import flet as ft

def main(page: ft.Page):
    myText = ft.Text("Hello in red", size=24, color="red")

    myButton = ft.Button(content="cambia colore")

    page.controls.append(myText)
    page.controls.append(myButton)

    page.update()

ft.run(main)