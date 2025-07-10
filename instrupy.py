import serial
import matplotlib.pyplot as plt
import time
import csv

# --- CONFIGURACIÓN SERIAL ---
arduino_port = "COM5"      # Cambia esto al puerto que use tu Arduino
baud_rate = 9600           # Asegúrate que coincida con el baud rate del Arduino
execution_time = 60        # Tiempo de ejecución en segundos

# --- CONEXIÓN SERIAL ---
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Esperar que el Arduino reinicie

# --- VARIABLES PARA DATOS ---
times = []
weights = []
start_time = time.time()

# --- INICIO DE LECTURA Y GRAFICADO ---
try:
    print("Recibiendo datos del Arduino... (Duración: 1 minuto)")
    plt.ion()
    fig, ax = plt.subplots()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > execution_time:
            print("Tiempo límite alcanzado. Finalizando...")
            break

        line = ser.readline().decode().strip()
        try:
            t, w = map(float, line.split(","))
            times.append(t)
            weights.append(w)

            ax.clear()
            ax.plot(times, weights, label="Peso estimado (kg)", color="blue")
            ax.set_title("Peso estimado vs Tiempo")
            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Peso (kg)")
            ax.legend()
            plt.pause(0.1)
        except ValueError:
            pass  # Ignorar líneas mal formateadas
except KeyboardInterrupt:
    print("Lectura interrumpida por el usuario.")
finally:
    ser.close()
    plt.ioff()
    plt.show()

    # Guardar datos en CSV
    with open("datos_fuerza_vs_tiempo.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tiempo (s)", "Peso (kg)"])
        writer.writerows(zip(times, weights))

    print("Datos guardados en datos_fuerza_vs_tiempo.csv")