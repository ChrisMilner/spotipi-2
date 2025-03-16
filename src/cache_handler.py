import logging
import os
import json
import getpass

from spotipy import CacheHandler


class CustomCacheHandler(CacheHandler):
    def __init__(self):
        print("Constructor: " + getpass.getuser())
        self.logger = logging.getLogger(self.__class__.__name__)

        path = os.path.join(os.path.dirname(__file__), "../cache/")

        if not os.path.exists(path):
            os.makedirs(path)

        os.chmod(path, 0o766)  # rw-rw-rw-

        self.cache_file = path + "cache.txt"

        if not os.path.exists(self.cache_file):
            os.mknod(self.cache_file)

        print(self.cache_file)
        print("Exists?: " + str(os.path.exists(self.cache_file)))

    def get_cached_token(self):
        print("Getter: " + getpass.getuser())
        print(self.cache_file)
        print("Exists?: " + str(os.path.exists(self.cache_file)))

        if not os.path.exists(self.cache_file):
            self.logger.warning("Cache file doesn't exist")
            self.logger.info("Creating cache file...")
            os.mknod(self.cache_file)
            return

        with open(self.cache_file, "r") as f:
            return json.loads(f.read())

    def save_token_to_cache(self, token_info):
        with open(self.cache_file, "w") as f:
            f.write(json.dumps(token_info))
