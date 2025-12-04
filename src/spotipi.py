import os
import time
from io import BytesIO
import configparser
import logging

import requests
from PIL import Image

from led_matrix import LEDMatrix
from spotify_service import SpotifyService


class Spotipi:
    def __init__(self, config):
        self.config = config
        self.matrix = LEDMatrix(config)
        self.spotify = SpotifyService(config)
        
        self.curr_cover_art_url = None
    
    def update_matrix(self):
        new_cover_art_url = self.spotify.get_current_cover_art_url()

        if new_cover_art_url != self.curr_cover_art_url:
            self.curr_cover_art_url = new_cover_art_url

            if self.curr_cover_art_url is not None:
                image = self.fetch_image(self.curr_cover_art_url)
                self.matrix.display_image(image)
            else:
                self.matrix.clear()
        
        # If we're not displaying the album cover, display the clock
        if new_cover_art_url is None:
            self.show_binary_clock()

    def fetch_image(self, url):
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        dimensions = (int(self.config["MATRIX"]["Width"]), int(self.config["MATRIX"]["Height"]))
        image.thumbnail(dimensions, Image.Resampling.LANCZOS)

        return image.convert("RGB")


    def show_binary_clock(self):
        frame = self.matrix.create_blank_frame()

        frame.SetPixel(0,0, 255, 255, 255)

        self.matrix.display_frame(frame)


def main(config):
    spotipi = Spotipi(config)

    while True:
        try:
            spotipi.update_matrix()
        except Exception as e:
            logging.exception(e)
        finally:
            time.sleep(int(config["GENERAL"]["DelaySeconds"]))


def parse_config():
    config_file = os.path.join(os.path.dirname(__file__), '../config.ini')

    config = configparser.ConfigParser()
    config.read(config_file)

    return config


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    main(parse_config())
