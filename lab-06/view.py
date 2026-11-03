self.page.add(
    self.toggle_cambia_tema,

    # Sezione 1
    self.txt_titolo,
    self.txt_responsabile,
    ft.Divider(),

    # Sezione 2
    ft.Text("Modifica Informazioni", size=20),

    ft.Row(
        spacing=200,
        controls=[
            self.input_responsabile,
            pulsante_conferma_responsabile
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),

    ft.Divider(),

    # Sezione 3
    ft.Text("Strumenti", size=20),

    pulsante_mostra,

    self.lista_strumenti,

    ft.Divider(),

    # Sezione 4
    ft.Text("Cerca Strumento per Tipo", size=20),

    ft.Row(
        controls=[
            self.input_tipo_strumento,
            pulsante_cerca
        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),

    self.lista_strumenti_ricerca
)