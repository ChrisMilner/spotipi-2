import logging

import spotipy

from cache_handler import CustomCacheHandler

SCOPE = "user-read-currently-playing"


class SpotifyService:
    def __init__(self, config):
        self.logger = logging.getLogger(self.__class__.__name__)

        cache_handler = CustomCacheHandler()

        auth_manager = spotipy.SpotifyOAuth(
            username=config["SPOTIPY"]["Username"],
            scope=SCOPE,
            client_id=config["SPOTIPY"]["ClientId"],
            client_secret=config["SPOTIPY"]["ClientSecret"],
            redirect_uri=config["SPOTIPY"]["RedirectURI"],
            cache_handler=cache_handler,
            open_browser=False
        )

        self.spotify = spotipy.Spotify(auth_manager=auth_manager)

    def get_current_cover_art_url(self):
        result = self.spotify.current_user_playing_track()

        if result is None:
            self.logger.info("No song playing")
            return None
        else:
            return result["item"]["album"]["images"][0]["url"]
