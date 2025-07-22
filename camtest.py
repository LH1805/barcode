import cv2

print("Starte Kamera...")
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if not ret:
    print("❌ Fehler: Kein Bild erhalten")
else:
    print("✅ Bild erfasst, speichere als test.jpg")
    cv2.imwrite("test.jpg", frame)

cap.release()
print("Fertig.")
