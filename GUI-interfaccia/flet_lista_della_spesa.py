import flet as ft

def main(page: ft.Page):
    myText = ft.TextField(label="aggiungi elemento:")
    myListView = ft.ListView(expand=True)

    def gestione_bottone():
        checkbox=ft.Checkbox(myText.value) # value è il modo in cui si chiama il contenuto della casella di testo, label è solo l'etichetta che vedi prima di scrivere
        myListView.controls.append(checkbox)
        page.update()

    myAddButton = ft.CupertinoButton(content="aggiungi", on_click=gestione_bottone)

    row1=ft.Row([myText, myAddButton], alignment=ft.MainAxisAlignment.CENTER)

    page.controls.append(row1)
    page.controls.append(myListView)


ft.run(main)