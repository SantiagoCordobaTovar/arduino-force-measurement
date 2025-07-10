#include "HX711.h"

// Pines del módulo HX711
#define DT_PIN 3  // Pin DT del HX711 al pin digital 3 del Arduino
#define SCK_PIN 2 // Pin SCK del HX711 al pin digital 2 del Arduino

HX711 scale;

// Factor de calibración inicial (ajústalo según tus pruebas)
float calibration_factor = 0.00001200;

unsigned long start_time = 0; // Tiempo inicial

void setup() {
  Serial.begin(9600);
  Serial.println("Iniciando...");
  scale.begin(DT_PIN, SCK_PIN);
  scale.tare(); // Ajusta el peso a cero sin carga
  Serial.println("Coloca un peso conocido para calibrar.");
  delay(2000); // Espera para colocar el peso
  start_time = millis(); // Tiempo inicial
}

void loop() {
  if (scale.is_ready()) {
    // Lectura de peso
    long raw_reading = scale.get_units(1); // Promedio de 1 lectura
    float weight = -1 * raw_reading * calibration_factor; // Calcular peso
    unsigned long current_time = (millis() - start_time) / 1000; // Tiempo en segundos

    // Enviar datos al puerto serial
    Serial.print(current_time);
    Serial.print(",");
    Serial.println(weight);
  } else {
    Serial.println("HX711 no está listo");
  }

  delay(1000); // Actualiza cada segundo
}
