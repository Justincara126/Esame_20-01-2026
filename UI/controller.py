import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb=int(self._view.txtNumAlbumMin)
        except ValueError:
            return self.

    def handle_connected_artists(self, e):
        pass


