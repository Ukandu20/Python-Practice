import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

def get_most_played_song(username):
    # Replace 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET', and 'YOUR_REDIRECT_URI' with your actual Spotify API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth
                        (client_id= os.getenv('CLIENT_ID'),
                        client_secret=  os.getenv('CLIENT_SECRET'),
                        redirect_uri= os.getenv('REDIRECT_URI'),
                        scope='os.getuser-top-read'))
                        
    # Get the user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=1, time_range='long_term')

    if top_tracks['items']:
        most_played_track = top_tracks['items'][0]
        track_name = most_played_track['name']
        artist_name = most_played_track['artists'][0]['name']
        play_count = most_played_track['popularity']  # The popularity score can be considered as play count
        print(f"The most played song for user {username} is '{track_name}' by {artist_name} with a popularity score of {play_count}.")
    else:
        print("No top tracks found for the user.")

    
    # Get the users top artists
    top_artists = sp.current_user_top_artists(limit=1, time_range='long_term')

    if top_artists ['items']:
        most_played_artist = top_artists['items'][0]
        artist_name = most_played_artist['name']
        artist_genre = most_played_artist['genres']
        artist_popularity = most_played_artist['popularity']
        print(f"The most played artist for user {username} is '{artist_name}' with a popularity score of {artist_popularity}.")
    else:
        print("No top artists found for the user.")

    # Get the user's top 10 tracks of all time
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='long_term')

    if top_tracks['items']:
        print(f"The top 10 tracks of all time for user {username} are:")
        for i, track in enumerate(top_tracks['items']):
            print(f"{i+1}. {track['name']} by {track['artists'][0]['name']} with a popularity score of {track['popularity']}.")
    else:
        print("No top tracks found for the user.")

    

# Replace 'YOUR_USERNAME' with the Spotify username of the user you want to get the most played song for
get_most_played_song('cartierkuti')
    
