# Spotipi 2
> Display Spotify cover art on your Raspberry Pi connected LED matrix display

This project is inspired by, and based upon [ryanwa18/spotipi](https://github.com/ryanwa18/spotipi) :pray:

It aims to simplify the original project, and make the setup process easier.

## Setup

### Spotify API

In order to run Spotipi you need to have an Application set up in the [Developer Dashboard](https://developer.spotify.com/dashboard/applications).

1. Navigate to the link above and click "Create app"
2. Give your app a name and description, and add a redirect URI: `http://127.0.0.1/callback` (or anything you want - it shouldn't matter)
3. Agree to the T&C and click "Save"  

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
