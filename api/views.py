import requests
import spotipy
from django.shortcuts import render
from spotipy.oauth2 import SpotifyOAuth

# Configurazione dell'autenticazione (senza refreshing automatico del token)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fe9c1a7abbfb4598a012734fc8c8ff6e",
                                               client_secret="ba088183e57d405d874fb1239741a02d",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=["user-library-read"],
                                               cache_path=".cache"))

# Ottenere informazioni su un brano specifico
'''track = sp.track('spotify_track_id')
print(track)
album = sp.album('spotify_album_id')
print(album)'''
def test_spotify(request):
    results = sp.current_user_saved_tracks()
    risultati = {

    }
    lista_canzoni = []
    img = []
    for idx, item in enumerate(results['items']):
        track_name = item['track']['name']
        track = item['track']
        img.append(item['track']['album']['images'][0]['url'])
        lista_canzoni.append(track_name)
        #print(f"{track['name']} - {track['artists'][0]['name']}")
    context = {
        "results": lista_canzoni,
        "track": track,
        "img": img,
        
    }    
    return render(request, 'spotify.html', context)

def todos_view(request):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()
            messaggio_errore = None
        else:
            lista_todos = []
            messaggio_errore = "Errore nel recupero dei dati. Codice di stato: "+str(response.status_code)
    except Exception as e:
        lista_todos = []
        messaggio_errore = "Errore nella connessione all'API: "+ str(e)

    return render(request, 'todos.html', {
        'todos': lista_todos,
        'errore': messaggio_errore,
    })

