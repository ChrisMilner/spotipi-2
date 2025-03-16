set -e

echo "Removing spotipi2 service if it exists..."
systemctl stop spotipi2
rm -rf /etc/systemd/system/spotipi2.*
systemctl daemon-reload

echo "Creating spotipi2 service..."
cp service/spotipi2.service /etc/systemd/system/
install_path=$(pwd)
sed -i -e 's/install_path/$install_path/g'
systemctl daemon-reload
systemctl start spotipi2
systemctl enable spotipi2
