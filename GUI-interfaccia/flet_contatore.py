import flet as ft

def main(page: ft.Page):
    contatore = ft.TextField(value="0", read_only=True, width=50, text_align=ft.TextAlign.CENTER, )

    def incrementa_contatore():
        contatore.value = str(int(contatore.value) + 1)  # trasforma il numero dentro contatore in un intero, ci aggiunge uno e poi lo ritrasforma in una stringa

    def decrementa_contatore():
#        if int(contatore.value) > 0: si scrive così se voglio che il contatore non possa scendere nei numeri negativi
#            contatore.value = str(int(contatore.value) - 1)
        contatore.value = str(int(contatore.value) - 1)



    bottone_meno=ft.IconButton(icon=ft.Icons.REMOVE, on_click=decrementa_contatore)
    bottone_piu = ft.IconButton(icon=ft.Icons.ADD, on_click=incrementa_contatore)

    row = ft.Row([bottone_meno, contatore, bottone_piu])

    page.controls.append(row)

ft.run(main)