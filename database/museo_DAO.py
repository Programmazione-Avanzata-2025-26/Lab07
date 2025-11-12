from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_musei(self) -> list[Museo] | None:
        """
        Restituisce tutti i musei nel database.
        :return: lista di oggetti Museo oppure None
        """
        cnx = ConnessioneDB.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_musei).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM  museo """

        try:
            cursor.execute(query)
            for row in cursor:
                museo = Museo(
                    id=row["id"],
                    nome=row["nome"],
                    tipologia=row["tipologia"]
                )
                result.append(museo)
        except Exception as e:
            print(f"Errore durante la query get_musei: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

