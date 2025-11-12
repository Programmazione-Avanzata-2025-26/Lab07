import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    def popola_dropdown_musei(self):
        """Popola il menu a tendina dei musei."""
        self._view.dropdown_museo.options.clear()
        self._view.dropdown_museo.options.append(ft.dropdown.Option(None, "Nessun Filtro"))

        musei = self._model.get_musei()

        if musei:
            for museo in musei:
                self._view.dropdown_museo.options.append(ft.dropdown.Option(museo.nome))
        else:
            self._view.show_alert("Errore nel caricamento dei musei.")

        self._view.update()

    def popola_dropdown_epoche(self):
        """Popola il menu a tendina con TUTTE le epoche disponibili nel DB."""
        self._view.dropdown_epoca.options.clear()
        self._view.dropdown_epoca.options.append(ft.dropdown.Option(None, "Nessun Filtro"))

        epoche = self._model.get_epoche()

        if epoche:
            for epoca in epoche:
                self._view.dropdown_epoca.options.append(ft.dropdown.Option(epoca))
        else:
            self._view.show_alert("Errore nel caricamento delle epoche.")

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_museo_change(self, e):
        """Aggiorna il museo selezionato e salva il valore."""
        valore = e.control.value
        self.museo_selezionato = None if valore == "Nessun Filtro" else valore

    def on_epoca_change(self, e):
        """Aggiorna l'epoca selezionata e salva il valore."""
        valore = e.control.value
        self.epoca_selezionata = None if valore == "Nessun Filtro" else valore

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e):
        """Mostra gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        self._view.lista_artefatti.controls.clear()
        lista_artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if lista_artefatti is None:
            self._view.show_alert("Errore di connessione al database.")
        elif len(lista_artefatti) == 0:
            self._view.show_alert("Nessun artefatto trovato per i criteri selezionati")
        else:
            for artefatto in lista_artefatti:
                self._view.lista_artefatti.controls.append(ft.Text(f"{artefatto}"))

        self._view.update()
