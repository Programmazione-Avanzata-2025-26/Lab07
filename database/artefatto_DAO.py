from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def get_artefatti_filtrati(museo: str, epoca: str) -> list[Artefatto] | None:
        """
        Restituisce tutti gli artefatti appartenenti a un dato museo.
        :return: lista di oggetti Artefatto oppure None
        """
        cnx = ConnessioneDB.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_artefatti_filtrati).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT a.*
                FROM artefatto a, museo m 
                WHERE m.nome = COALESCE(%s,m.nome) and a.epoca = COALESCE(%s,a.epoca) and a.id_museo = m.id
                """
        try:
            cursor.execute(query, (museo, epoca,))
            for row in cursor:
                artefatto = Artefatto(
                    id=row["id"],
                    nome=row["nome"],
                    tipologia=row["tipologia"],
                    epoca=row["epoca"],
                    id_museo=row["id_museo"],
                )
                result.append(artefatto)
        except Exception as e:
            print(f"Errore durante la query get_artefatti_filtrati: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_epoche() -> list[str] | None:
        """
        Restituisce tutte le epoche presenti nel database.
        :return: lista di epoche (stringhe) oppure None
        """
        cnx = ConnessioneDB.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database (get_epoche).")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT DISTINCT epoca
                FROM artefatto
                """
        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["epoca"])

        except Exception as e:
            print(f"Errore durante la query get_epoche: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result