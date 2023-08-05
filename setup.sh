sudo raspi-config
sudo reboot
lsmod | grep spi
# spi_bcm2835 must be enabled else
# sudo nano /boot/config.txt
# dtparam=spi=on uncomment
sudo apt update
sudo apt upgrade
sudo apt install python3-dev python3-pip
sudo pip3 install spidev
sudo pip3 install mfrc522
