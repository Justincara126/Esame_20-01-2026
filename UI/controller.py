import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb=int(self._view.txtNumAlbumMin.value)
            print(n_alb)
            if n_alb<=0:
                return self._view.show_alert('usare un numero maggiore di 0')
            self._model.build_graph(n_alb)
            artisti=self._model.g.nodes()
            self._view.ddArtist.options.clear()
            self._view.btnArtistsConnected.disabled=False
            self._view.btnSearchArtists.disabled=False


            for artist in artisti:
                self._view.ddArtist.options.append(ft.dropdown.Option(key=artist.id, text=artist.name))



            nodi=self._model.get_num_nodi()
            archi=self._model.get_num_archi()
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f'Il grafo ha {nodi} nodi e {archi} archi'))
            self._view.update_page()

        except ValueError:
            return self._view.show_alert('errore')

    def handle_connected_artists(self, e):
        try:
            nodo=int(self._view.ddArtist.value)
            vicini=self._model.getSortedNeighbors(nodo)
            self._view.txt_result.controls.clear()
            for vicino in vicini:
                self._view.txt_result.controls.append(ft.Text(vicino.name))
        except ValueError:
            return self._view.show_alert('errore')
    def handle(self,e):
        try:
            num_album=int(self._view.txtNumAlbumMin.value)
            print(num_album)
            if num_album<=0:
                return self._view.show_alert('usare un numero maggiore di 0')
            lunghezza=int(self._view.txtMaxArtists.value)
            percorso,peso=self._model.getSortedNeighbors(lunghezza,num_album,self._view.ddArtist.value)
        except ValueError:
            print(1)

#grafo
