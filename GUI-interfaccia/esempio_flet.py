import flet as ft

def main(page:ft.Page):
    il_mio_testo = ft.Text("questo è il mio primo testo!!!", size=24, color="blue")
    page.controls.append(il_mio_testo)

    il_mio_testo.value="ciao"
    page.update()


ft.run(main)