import subprocess
from time import sleep

# Hier wäre normalerweise der Start/Initialisierung; bei libcamera-still nicht direkt nötig

sleep(2)  # Wartezeit, die Kamera bereit ist

# Führt den Befehl aus, um das Bild aufzunehmen
subprocess.run(["libcamera-still", "-o", "test.jpg"])

print("✅ Bild gespeichert als test.jpg")
