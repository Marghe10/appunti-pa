import mysql.connector

from database.DB_connect import get_connection
from model.strumento import Strumento


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
        Restituisce tutti gli strumenti.
        Restituisce None in caso di errore del database.
        """
        connessione = get_connection()
        cursore = None

        try:
            cursore = connessione.cursor(dictionary=True)

            query = """
                SELECT codice, tipo, marca, anno_acquisto,
                       valore, disponibile
                FROM strumento
                ORDER BY codice
            """

            cursore.execute(query)
            righe = cursore.fetchall()

            strumenti = []

            for riga in righe:
                strumento = Strumento(
                    codice=riga["codice"],
                    tipo=riga["tipo"],
                    marca=riga["marca"],
                    anno_acquisto=riga["anno_acquisto"],
                    valore=riga["valore"],
                    disponibile=bool(riga["disponibile"])
                )

                strumenti.append(strumento)

            return strumenti

        except mysql.connector.Error as errore:
            print(f"Errore durante la lettura degli strumenti: {errore}")
            return None

        finally:
            try:
                if cursore is not None:
                    cursore.close()
            finally:
                connessione.close()

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
        Restituisce tutti gli strumenti del tipo indicato.
        Restituisce None in caso di errore del database.
        """
        connessione = get_connection()

        if connessione is None:
            return None

        cursore = None

        try:
            cursore = connessione.cursor(dictionary=True)

            query = """
                SELECT codice, tipo, marca, anno_acquisto,
                       valore, disponibile
                FROM strumento
                WHERE tipo = %s
                ORDER BY codice
            """

            cursore.execute(query, (tipo,))
            righe = cursore.fetchall()

            strumenti = []

            for riga in righe:
                strumento = Strumento(
                    codice=riga["codice"],
                    tipo=riga["tipo"],
                    marca=riga["marca"],
                    anno_acquisto=riga["anno_acquisto"],
                    valore=riga["valore"],
                    disponibile=bool(riga["disponibile"])
                )

                strumenti.append(strumento)

            return strumenti

        except mysql.connector.Error as errore:
            print(f"Errore durante la ricerca degli strumenti: {errore}")
            return None

        finally:
            try:
                if cursore is not None:
                    cursore.close()
            finally:
                connessione.close()