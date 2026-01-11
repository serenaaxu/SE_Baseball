import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._selected_team = None
        self._view = view
        self._model = model

    def populate_dd(self):
        years = self._model.get_years()
        self._view.dd_anno.options = [ft.dropdown.Option(str(y)) for y in years]
        self._view.update()

    def handle_year_selected(self, year):
        year = self._view.dd_anno.value
        if not year:
            return
        teams = self._model.get_teams_by_year(int(year))

        self._view.txt_out_squadre.controls.clear()
        for t in teams:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{t.name} {t.team_code}"))

        self._view.dd_squadra.options = [
            ft.dropdown.Option(key=str(t.id), text = t.name)
            for t in teams
        ]
        self._view.update()

    def handle_squadra_selected(self, e):
        if self._view.dd_squadra.value is None:
            return

        team_id = int(self._view.dd_squadra.value)
        self._selected_team = self._model.get_team_by_id(team_id)

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        year = self._view.dd_anno.value

        if not year:
            self._view.show_alert("Selezionare l'anno!")
            return

        self._model.build_graph(year)

        n_nodes, n_edges = self._model.get_graph_details()

        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(
            ft.Text(f"Grafo creato.\nNodi: {n_nodes}\nArchi: {n_edges}")
        )
        self._view.update()


    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        if self._selected_team is None:
            self._view.show_alert("Selezionare team")
            return

        n_nodes, _ = self._model.get_graph_details()
        if n_nodes == 0:
            self._view.show_alert("Creare prima il grafo")
            return

        neighbors = self._model.get_sorted_neighbors(self._selected_team)

        self._view.txt_risultato.controls.clear()
        for team_vicino, peso, in neighbors:
            self._view.txt_risultato.controls.append(
                ft.Text(f"{team_vicino} {peso}")
            )

        self._view.update()


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

