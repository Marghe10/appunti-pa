import flet as ft

from UI.view import View
from model.model import DepositoStrumenti


class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value

        self._view.txt_responsabile.value = (
            f"Responsabile: {self._model.responsabile}"
        )

        self._view.update()

    def mostra_strumenti(self, e):
        # Elimina i risultati della visualizzazione precedente.
        self._view.lista_strumenti.controls.clear()

        strumenti = self._model.get_strumenti()

        if strumenti is None:
            self._view.update()
            self._view.show_alert(
                "Errore durante la lettura del database."
            )
            return

        if not strumenti:
            self._view.update()
            self._view.show_alert(
                "Non ci sono strumenti nel database."
            )
            return

        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(
                ft.Text(str(strumento))
            )

        self._view.update()

    def cerca_strumenti(self, e):
        tipo = (
            self._view.input_tipo_strumento.value or ""
        ).strip()

        self._view.lista_strumenti_ricerca.controls.clear()

        if not tipo:
            self._view.update()
            self._view.show_alert(
                "Inserisci il tipo di strumento da cercare."
            )
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        if strumenti is None:
            self._view.update()
            self._view.show_alert(
                "Errore durante la ricerca nel database."
            )
            return

        if not strumenti:
            self._view.update()
            self._view.show_alert(
                f"Nessuno strumento trovato per il tipo '{tipo}'."
            )
            return

        for strumento in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(
                ft.Text(str(strumento))
            )

        self._view.update()