#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

/* WiFi Credentials */
const char* ssid = "Shravni";
const char* password = "Shravni@8046";

/* MQTT Broker */
const char* mqtt_server = "broker.hivemq.com";

/* MQTT Topics */
const char* temp_topic = "home/esp32/temperature";
const char* hum_topic  = "home/esp32/humidity";

/* DHT Configuration */
#define DHTPIN 4
#define DHTTYPE DHT11

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup_wifi() {
  delay(10);
  Serial.print("Connecting to WiFi");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected");
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_DHT_Publisher")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor");
    delay(2000);
    return;
  }

  char tempStr[8];
  char humStr[8];

  dtostrf(temperature, 1, 2, tempStr);
  dtostrf(humidity, 1, 2, humStr);

  client.publish(temp_topic, tempStr);
  client.publish(hum_topic, humStr);

  Serial.print("Temperature: ");
  Serial.print(tempStr);
  Serial.print(" °C | Humidity: ");
  Serial.print(humStr);
  Serial.println(" %");

  delay(5000);   // Publish every 5 seconds
}