import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.dao=DAO()
        self.peso_massimo=0
        self.percorso_migliore=[]


    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        pass
    def get_num_nodi(self):
        print(list(self.g.nodes()))

        return len(list(self.g.nodes()))
    def get_num_archi(self):
        return self.g.number_of_edges()

    def build_graph(self,n_albums):
        self.g = nx.Graph()
        lista_artists = self.dao.get_artists(n_albums)
        self._graph.clear()
        self.dizionario={}
        for artist in lista_artists:
            self.g.add_node(artist)
            self.dizionario[artist.id] = artist
        connection=self.dao.get_edges(self.dizionario)
        for connessione in connection:
            if connessione.id1 in self.dizionario and connessione.id2 in self.dizionario:
                print('aggiunto arco')
                self.g.add_edge(self.dizionario[connessione.id1],self.dizionario[connessione.id2],weight=connessione.peso)
            else:
                print('aggiunto non existente')
        for u,v,data in self.g.edges(data=True):
            print(u,v,data)
    def getSortedNeighbors(self, id):
        nodo=self.dizionario[id]
        vicini = self.g.neighbors(nodo)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append((v, self.g[nodo][v]["weight"]))
            viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple


    def percorso_migliore(self,n_art,d_min,artista_1):
        id_artisti=self.dao.get_artisti_minuti(d_min)
        lista_artisti=[]
        for id in id_artisti:
            lista_artisti.append(self.dizionario[id])
        self.ricorsione(n_art,[artista_1],lista_artisti,peso=0)
        return self.percorso_migliore,self.peso_massimo
    def ricorsione(self,lunghezza,parziale,lista_artisti,peso):
        if len(parziale) ==lunghezza:
            if self.peso_massimo<peso:
                self.peso_massimo=peso
                self.percorso_migliore=parziale.copy()
        ultimo_nodo=parziale[-1]
        for v in self.g.neighbors(ultimo_nodo):
            if v  in parziale:
                pass
            elif v not in lista_artisti:
                pass
            else:
                parziale.append(v)
                self.ricorsione(lunghezza,parziale,lista_artisti,peso+self.g[ultimo_nodo][v]["weight"])
                parziale.pop()





