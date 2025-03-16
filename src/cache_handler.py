import os
import json

from spotipy import CacheHandler


class CustomCacheHandler(CacheHandler):
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "../cache/")

        if not os.path.exists(path):
            os.makedirs(path)

        os.chmod(path, 0o666)  # rw-rw-rw-

        self.cache_file = path + "cache.txt"

    def get_cached_token(self):
        with open(self.cache_file, "r") as f:
            return json.loads(f.read())

    def save_token_to_cache(self, token_info):
        with open(self.cache_file, "w") as f:
            f.write(json.dumps(token_info))
