from mysql.connector import errorcode
import mysql.connector

def main():
    print("sto funzionando")
    try:
        # STABILISCO LA CONNESSIONE CON IL DATABASE
        cnx = mysql.connector.connect(user='root', password='', host='localhost', port="3306",
                                      database='products_suppliers')

        print("se vedi questo messaggio mi sono collegato al database\n\n")

        #MI FACCIO DARE DALLA CONNESSIONE IN CURSORE, SCRIVO LA QUERY, LA ESEGUO

        cursore_dizionario = cnx.cursor(dictionary=True)
        query = """select `S#`, `SNAME` from S
                    where CITY="Paris" """

        cursore_dizionario.execute(query)

        for riga in cursore_dizionario:
            print(riga["SNAME"])




    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERRORE: Qualcosa è andato storto con username o password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERRORE: Il Database non esiste")
        else:
            print(err)
    else:
        cnx.close()



main()