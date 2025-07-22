# camera/capture.py
import cv2

def take_picture(filename="capture.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Kamera konnte nicht geöffnet werden.")
    
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Bildaufnahme fehlgeschlagen.")
    
    cv2.imwrite(filename, frame)
    cap.release()
    return filename
