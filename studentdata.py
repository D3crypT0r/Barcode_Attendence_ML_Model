import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime
import pandas as pd

def load_dataset():
    dataset_path = 'data.csv'
    # Load dataset with tab delimiter
    return pd.read_csv(dataset_path)

def decode_qr(frame, dataset):
    decoded_objs = decode(frame)
    for obj in decoded_objs:
        # Decode the QR code or barcode
        membership_id = obj.data.decode('utf-8').strip()  
        print("Detected ID:", membership_id)

        # Match membership ID with dataset
        match = dataset[dataset['ID'] == membership_id]
        if not match.empty:
            full_name = match.iloc[0]['Name']
            roll_no = match.iloc[0]['Roll No']  
            print("Attendance Marked for:", full_name, "Roll No:", roll_no)
            mark_attendance(full_name, roll_no)
        else:
            print("Student not found in dataset. ID:", membership_id)

def mark_attendance(full_name, roll_no):
    # Get current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with open('attendance.csv', 'a') as f:
        f.write(f"{full_name},{roll_no},{date_str},{time_str}\n")

def main():
    try:
        dataset = load_dataset()
    except FileNotFoundError:
        print("Student dataset file not found.")
        return

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        decode_qr(frame, dataset)

        cv2.imshow('Attendance System', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
