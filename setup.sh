set -e

echo "Installing Python dependencies..."
sudo python3 -m pip install -r requirements.txt --break-system-packages

echo "Downloading rgb-matrix software setup..."
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh > rgb-matrix.sh
chmod u+x rgb-matrix.sh

echo "Running rgb-matrix software setup..."
sudo ./rgb-matrix.sh
