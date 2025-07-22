from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()
sleep(2)  # Zeit geben, bis Kamera bereit ist

picam2.capture_file("test.jpg")
print("✅ Bild gespeichert als test.jpg")
