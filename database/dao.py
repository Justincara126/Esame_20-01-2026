from database.DB_connect import DBConnect
from model.artist import Artist
from model.connessione import Connessione


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_artists(num):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT a.id, a.name
                FROM artist a,album b
                    where a.id=b.artist_id
                    group by a.id,a.name
                    having count(*)>=%s
                """
        cursor.execute(query,(num,))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        print(result)

        return result
    @staticmethod
    def get_edges(artists):
        conn = DBConnect.get_connection()
        result = []


        cursor = conn.cursor(dictionary=True)
        print(66666666666666666666)
        query='''select a1.artist_id as id1, a2.artist_id as id2, count(*) as peso
        from iTunes.album a1,iTunes.album a2,iTunes.track t1,iTunes.track t2
        where a1.artist_id > a2.artist_id and t1.genre_id = t2.genre_id and t1.album_id=a1.id and t2.album_id=a2.id
        group by a1.artist_id, a2.artist_id,t2.genre_id'''
        cursor.execute(query)
        for row in cursor:
            artist = row['id1']
            artist2 = row['id2']
            peso = row['peso']
            print(artist,artist2,peso)
            result.append(Connessione(row['id1'],row['id2'],peso))
            print(9)
            pass
        cursor.close()
        conn.close()
        return result





        cursor.close()
        conn.close()
        return result

