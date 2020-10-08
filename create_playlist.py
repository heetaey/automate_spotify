import json
import requests

from secrets import spotify_userid, spotify_token


class CreatePlaylist:
    def __init__(self):
        self.userid = spotify_userid
        self.spotify_token = spotify_token

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube liked Videos",
            "description": "All Liked Youtube videos",
            "public": False
        })

        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            self.userid)
        response = requests.post(
            query,
            data = request_body,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        return response_json["id"]

    def get_spotify_url(self):
        pass

    def add_song_to_playlist(self):
        pass