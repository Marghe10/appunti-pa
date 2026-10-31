class Studente:
    def __init__(self, nome, cognome, eta, matricola, corso, anno):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.corso = corso
        self.anno = anno
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def calcola_media(self):
        if len(self.voti) == 0:
            return 0

        return sum(self.voti) / len(self.voti)

    def __str__(self):
        return (f"Nome: {self.nome}\n", "Cognome: {self.cognome}\n", "Età: {self.eta}\n", "Matricola: {self.matricola}\n",
                f"Corso: {self.corso}\n", "Anno: {self.anno}\n", "Voti: {self.voti}\n", "Media: {self.calcola_media():.2f}")