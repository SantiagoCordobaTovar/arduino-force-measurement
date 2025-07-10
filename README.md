# Real-Time Compression Force Measurement with Arduino and Python
This project measures the force applied to a surface (e.g., chest compressions for CPR training) using an Arduino with a load cell and HX711 amplifier. The data is sent via serial communication and visualized in real-time using a Python script. The system also saves the data to a CSV file for later analysis.

## 🛠️ Components
- Arduino UNO (or compatible board)
- Load cell
- HX711 load cell amplifier
- Jumper wires
- Computer with Python 3
- 
## 📦 Repository Structure
arduino-force-measurement/
│
├── instrupy.py # Python script: reads serial data, plots it, and saves to CSV
├── MEDICION_FRECUENCIA_COMPRESIONES.ino # Arduino sketch: reads weight from HX711 and sends via serial
├── README.md # This file
└── datos_fuerza_vs_tiempo.csv # Output data file (generated after script execution)

## 🚀 How It Works
## Arduino
The Arduino sketch reads data from the load cell using the HX711 amplifier, converts it into weight (kg), and sends the data in the format:
at a fixed interval (e.g., every 100ms).
time_in_seconds,weight_in_kg

### Python Script
The `instrupy.py` script:
1. Connects to the Arduino via serial (adjust `COM5` as needed).
2. Reads incoming data for 60 seconds.
3. Plots the weight vs time in real time using Matplotlib.
4. Saves the collected data to `datos_fuerza_vs_tiempo.csv`.
## ▶️ How to Run
### 1. Upload the Arduino Sketch
Open `MEDICION_FRECUENCIA_COMPRESIONES.ino` in the Arduino IDE and upload it to your board.
### 2. Install Python Dependencies
Make sure Python 3 is installed, then run:
```bash
pip install matplotlib pyserial
