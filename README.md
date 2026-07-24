# 😴 Sleep Alarm Detector

A real-time AI-based drowsiness detection system that monitors eye movements using a webcam. When the user's eyes remain closed for a specified duration, the system triggers an alarm to alert the user and help prevent accidents caused by drowsiness.

## 🚀 Features

- Real-time face and eye detection
- AI-based drowsiness detection
- Eye Aspect Ratio (EAR) based monitoring
- Automatic alarm alert when drowsiness is detected
- Works with any webcam
- Fast and lightweight performance
- Real-time video processing

## 🧠 How It Works

The system captures live video through a webcam and detects facial landmarks using MediaPipe. Eye landmarks are tracked and the Eye Aspect Ratio (EAR) is calculated. If the eyes remain closed for a certain period, the alarm is automatically triggered.

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Pygame / Playsound

## 📂 Project Structure
Sleep-Alarm-Detector/
│
├── main.py
├── eye_utils.py
├── alarm.wav
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

## ⚙️ Installation & Run Project

Copy and paste the command below in your terminal:

```bash
git clone https://github.com/your-username/Sleep-Alarm-Detector.git && cd Sleep-Alarm-Detector && pip install -r requirements.txt && python main.py

📦 Dependencies

The project requires:

opencv-python
mediapipe
numpy
pygame
playsound
