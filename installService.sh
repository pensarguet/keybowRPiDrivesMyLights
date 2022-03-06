chmod +x app.py
sudo cp keybowRPiDrivesMyLights.service /etc/systemd/system
sudo systemctl enable keybowRPiDrivesMyLights
sudo systemctl start keybowRPiDrivesMyLights
