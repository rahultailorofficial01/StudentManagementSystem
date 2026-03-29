import random
import time
import playsound
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
import matplotlib.pyplot as plt
import os

file_path = r'C:\Users\rtail\OneDrive\Documents\python programs\Intrusion-Detection-System\beep.mp3'

if os.path.exists(file_path):
    print("File found, playing sound...")
    playsound.playsound(file_path)
else:
    print("File not found!")


# Area boundary coordinates
AREA_BOUNDARY = {
    'lat_min': 25.0,
    'lat_max': 26.0,
    'lon_min': 75.0,
    'lon_max': 76.0
}

def generate_fake_coordinates():
    latitude = random.uniform(24.5, 26.5)
    longitude = random.uniform(74.5, 76.5)
    return latitude, longitude

def is_intruder_detected(lat, lon):
    if AREA_BOUNDARY['lat_min'] <= lat <= AREA_BOUNDARY['lat_max'] and AREA_BOUNDARY['lon_min'] <= lon <= AREA_BOUNDARY['lon_max']:
        return False
    else:
        return True

def log_intrusion(lat, lon):
    """Intrusion details ko file mein save karna."""
    with open("intrusion_log.txt", "a") as file:
        file.write(f"Intrusion detected at {lat:.4f}, {lon:.4f} on {time.ctime()}\n")

def send_email_alert(lat, lon):
    """Email bhejna jab intruder detect ho."""
    sender_email = "rahulonline.work02@gmail.com"
    receiver_email = "rahultailorofficial@gmail.com"
    password = "your_email_password"  # App Password ka use karna agar 2FA enabled ho
    msg = MIMEText(f"Intruder detected at Latitude={lat:.4f}, Longitude={lon:.4f}")
    msg['Subject'] = '🚨 Intruder Alert! 🚨'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

def update_gui(lat, lon, alert_status):
    window = tk.Tk()
    window.title("Intrusion Detection")
    label1 = tk.Label(window, text=f"Latitude: {lat:.4f}")
    label1.pack()
    label2 = tk.Label(window, text=f"Longitude: {lon:.4f}")
    label2.pack()
    alert_text = "🚨 Intruder Detected! 🚨" if alert_status else "✅ No Intrusion Detected."
    label3 = tk.Label(window, text=alert_text, fg="red" if alert_status else "green")
    label3.pack()
    window.mainloop()

def plot_coordinates(lat, lon):
    plt.scatter(lat, lon, color='red')
    plt.title("Live GPS Coordinates")
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.pause(0.1)

def simulate_intrusion_detection():
    plt.ion()  # Interactive mode
    while True:
        lat, lon = generate_fake_coordinates()
        print(f"Sensor Triggered! Location: Latitude={lat:.4f}, Longitude={lon:.4f}")
        
        if is_intruder_detected(lat, lon):
            print("🚨 ALERT: Intruder detected! 🚨")
            playsound.playsound (r'C:\Users\rtail\OneDrive\Documents\python programs\Intrusion-Detection-System\beep.mp3')  # Absolute path
              # Simple relative path# Play sound
            log_intrusion(lat, lon)  # Log intrusion
            send_email_alert(lat, lon)  # Send email
            alert_status = True
        else:
            print("✅ No intrusion detected.")
            alert_status = False
        
        update_gui(lat, lon, alert_status)  # Update GUI
        plot_coordinates(lat, lon)  # Plot graph
        time.sleep(2)  # 2 seconds delay for each iteration

if __name__ == "__main__":
    simulate_intrusion_detection()
