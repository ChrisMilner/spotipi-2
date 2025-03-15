import time
from io import BytesIO
import configparser
import logging

import requests
from PIL import Image

from src.spotify_service import SpotifyService


def fetch_image(url, config):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    dimensions = (int(config["MATRIX"]["Width"]), int(config["MATRIX"]["Height"]))
    image.thumbnail(dimensions, Image.Resampling.LANCZOS)

    return image.convert("RGB")


def display_image(image):
    image.show()


def main(config):
    spotify = SpotifyService(config)
    curr_cover_art_url = None

    while True:
        try:
            new_cover_art_url = spotify.get_current_cover_art_url()

            if new_cover_art_url != curr_cover_art_url:
                curr_cover_art_url = new_cover_art_url

                image = fetch_image(curr_cover_art_url, config)
                display_image(image)
        except Exception as e:
            logging.exception(e)
        finally:
            time.sleep(int(config["GENERAL"]["DelaySeconds"]))


def parse_config():
    config = configparser.ConfigParser()
    config.read("../config.ini")

    return config


if __name__ == "__main__":
    main(parse_config())
