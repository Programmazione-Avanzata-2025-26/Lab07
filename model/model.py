from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
import roman as r

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        return self._artefatto_dao.get_artefatti_filtrati(museo, epoca)

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        return self._ordina_epoche(self._artefatto_dao.get_epoche()) # con metodo-chiave

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        return self._museo_dao.get_musei()

    # --- ALTRO ---
    @staticmethod
    def _ordina_epoche(lista_epoche):
        """Restituisce la lista di tutte le epoche ordinata"""
        def chiave(epoca):
            elements = epoca.split(" ")
            secolo = r.fromRoman(elements[0])
            # Le epoche d.C. non hanno la locuzione esplicitata quindi elements[] avrà solo due elementi
            locuzione = 0 if len(elements) == 3 else 1  # Mappo a.C.-->0 , d.C.-->1

            if locuzione == 0:
                return -secolo
            else:
                return secolo

        return sorted(lista_epoche, key=chiave)
