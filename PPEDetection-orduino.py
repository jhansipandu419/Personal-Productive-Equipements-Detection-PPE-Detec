import pyfirmata
from ultralytics import YOLO
import cv2
import cvzone
import math
import time
from simple_facerec import SimpleFacerec
import pyttsx3
import pandas as pd
from datetime import datetime
from openpyxl.workbook import Workbook
import openpyxl

# Arduino setup
port = "COM5"
board = pyfirmata.Arduino(port)

# LED setup
green_led = board.get_pin("d:13:o")
red_led = board.get_pin("d:12:o")

# Stepper motor control pins (4-wire)
stepper_pins = [8, 9, 10, 11]
steps_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]
for pin in stepper_pins:
    board.digital[pin].mode = pyfirmata.OUTPUT

def rotate_stepper(steps=100, delay=0.01):
    for _ in range(steps):
        for step in steps_sequence:
            for pin, val in zip(stepper_pins, step):
                board.digital[pin].write(val)
            time.sleep(delay)

# Load YOLO model
model = YOLO("ppe.pt")
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']

# Face recognition setup
sfr = SimpleFacerec()
sfr.load_encoding_images("Images/")

# Text-to-speech setup
engine = pyttsx3.init()

# Webcam
cap = cv2.VideoCapture(0)

# Log setup
log_df = pd.DataFrame(columns=["Name", "Time"])

# Initial prompt and motor rotation
engine.say("Please enter first person")
engine.runAndWait()
rotate_stepper(steps=100)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    face_locations, face_names = sfr.detect_known_faces(img)

    if len(face_locations) > 1:
        print("More than one person detected")
        engine.say("Only one person allowed")
        engine.runAndWait()
        red_led.write(1)
        green_led.write(0)
        continue

    if len(face_locations) == 1:
        name = face_names[0]
        print(f"Detected person: {name}")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_log = pd.DataFrame({"Name": [name], "Time": [current_time]})
        log_df = pd.concat([log_df, new_log], ignore_index=True)
        log_df.to_excel("recognition_log.xlsx", index=False)
        z1, o2, z2, o1 = face_locations[0]
        cv2.putText(img, name, (o1, z1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.rectangle(img, (o1, z1), (o2, z2), (255, 255, 0), 4)

    results = model(img, stream=True)
    ppe_ok = {"Hardhat": False, "Mask": False, "Safety Vest": False}

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            print(currentClass)

            if conf > 0.5:
                color = (0, 255, 0) if 'NO-' not in currentClass else (0, 0, 255)
                cvzone.putTextRect(img, f'{currentClass} {conf}', (x1, y1 - 10),
                                   scale=1, thickness=1, colorR=color, colorT=(255, 255, 255),
                                   colorB=color, offset=1)
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

                if currentClass in ppe_ok:
                    ppe_ok[currentClass] = True

    if all(ppe_ok.values()):
        engine.say("Access granted")
        engine.runAndWait()
        red_led.write(0)
        green_led.write(1)
        rotate_stepper(steps=100)
    else:
        red_led.write(1)
        green_led.write(0)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
board.exit()