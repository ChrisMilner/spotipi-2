# Spotipi 2
> Display Spotify cover art on your Raspberry Pi connected LED matrix display

This project is inspired by, and based upon [ryanwa18/spotipi](https://github.com/ryanwa18/spotipi) :pray:

It aims to simplify the original project, and make the setup process easier.

## Setup

### Spotify API

In order to run Spotipi you need to have an Application set up in the [Developer Dashboard](https://developer.spotify.com/dashboard/applications).

1. Navigate to the link above and click "Create app"
2. Give your app a name and description, and add a redirect URI: `http://127.0.0.1/callback` (or anything you want - it shouldn't matter)
3. Agree to the T&Cs and click "Save"  

### Pi Setup

```shell
git clone https://github.com/ChrisMilner/spotipi-2.git
cd spotipi-2

./setup.sh
```

You'll be prompted for some information about your LED Matrix setup, and then will need to restart.

```shell
cp config-template.ini config.ini
```

Now you need to edit `config.ini` to include the missing Spotipy variables which you can get from the app you created above.

```shell
sudo python3 src/spotipi.py
```

You will be given a link, open it and login through Spotify (if you are not already logged in).

You will then be redirected to a new URL, copy this new URL and paste it into the terminal.

:tada: Spotipi should now be running :tada:
 * If you're not currently playing a song on Spotify you should see `No song playing`
 * If you are then the cover art should be displayed on your LED matrix

## Installing as a service

If you've completed the above steps then Spotipi should be running, however, if you restart the Pi it will stop.
If you want the Pi to run Spotipi constantly in the background then you should install it as a service.

```shell
sudo ./install_service.sh
```

## Troubleshooting

### "I installed the service but it's not working"

Firstly, make sure that you've run Spotipi via the Python command successfully at least once.
This is required as you need to manually authenticate with Spotify. 

If you've done that, then you can view the service's logs by running:

```shell
journalctl -u spotipi2 -n 50
```

This will show you the `50` most recent log lines output by the Spotipi2 service.

### "How do I stop the service?"

You can stop/start the service with:

```shell
systemctl stop/start spotipi2
```

### "The service shows an error about `input`/`raw_input`"

This occurs when it can't read the Spotipy token cache file.
Either because it doesn't exist or it doesn't have permission.
Check that there is a file `spotipi-2/src/.cache` and that it is not empty
* If it doesn't exist or is empty, then you need to manually run the `sudo python3 src/spotipi.py` to set the token.
* If it does exist then most likely the service is unable to read it. You should check the permissions on that file.

I have tested this on my own Pi 2 Model B, but not on any other configurations.
Feel free to raise issues or PRs if you find bugs/improvements.
