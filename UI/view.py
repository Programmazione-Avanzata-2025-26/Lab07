import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # Dropdown musei
        self.dropdown_museo = ft.Dropdown(
            label="Museo",
            width=400,
            options=[ft.dropdown.Option(key="None", text="Nessun Filtro")],
            on_change=self.controller.on_museo_change  # Callback collegata
        )
        self.controller.popola_dropdown_musei()

        # Dropdown epoca
        self.dropdown_epoca = ft.Dropdown(
            label="Epoca",
            width=220,
            options=[ft.dropdown.Option(key="None", text="Nessun Filtro")],
            on_change=self.controller.on_epoca_change  # Callback collegata
        )
        self.controller.popola_dropdown_epoche()

        # Sezione 3: Artefatti
        pulsante_mostra_artefatti = ft.ElevatedButton(
            "Mostra Artefatti",
            on_click=self.controller.mostra_artefatti
        )
        self.lista_artefatti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
                spacing=20,
                controls=[self.dropdown_museo, self.dropdown_epoca],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Divider(),

            # Sezione 3: Artefatti
            ft.Row(
                spacing=200,
                controls=[pulsante_mostra_artefatti],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Container(
                content=self.lista_artefatti,
                height=250,
                border=ft.border.all(1, ft.Colors.BLACK),
                padding=5,
            ),
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
