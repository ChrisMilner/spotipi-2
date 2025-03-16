echo "Installing Python dependencies..."
python3 -m pip install -r requirements.txt

echo "Downloading rgb-matrix software setup..."
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh > rgb-matrix.sh

echo "Running rgb-matrix software setup..."
sudo ./rgb-matrix.sh
rm rgb-matrix.sh
