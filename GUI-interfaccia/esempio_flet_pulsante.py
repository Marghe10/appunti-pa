import flet as ft

def main(page: ft.Page):
    myText = ft.Text("Hello in red", size=24, color="red")

    def button_handler():
        print("button pressed")
        myText.color = "blue"
        myText.update()

    myButton = ft.Button(content="cambia colore", on_click=button_handler)

    page.controls.append(myText)
    page.controls.append(myButton)
    # page.update()   in questo caso non serve perchè alla fine della main viene chiamato page.update automaticamente

ft.run(main)