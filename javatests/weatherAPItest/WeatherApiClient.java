package org.example;

import com.google.gson.Gson;
import com.google.gson.annotations.SerializedName;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class WeatherApiClient {
 public static void main(String[] args) {
 try {
 // URL of the API endpoint
 String apiUrl = "https://api.weatherapi.com/v1/current.json?key=<HEREYOURAPI>&q=London";

 // Create a URL object
 URL url = new URL(apiUrl);

 // Open a connection to the API endpoint
 HttpURLConnection connection = (HttpURLConnection) url.openConnection();
 connection.setRequestMethod("GET");

 // Get the response code
 int responseCode = connection.getResponseCode();

 // Read the response
 BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
 StringBuilder response = new StringBuilder();
 String line;
 while ((line = reader.readLine()) != null) {
 response.append(line);
 }
 reader.close();

 // Check if the request was successful (response code 200)
 if (responseCode == 200) {
 // Parse the response as an object (assuming it is in JSON format)
 WeatherResponse weatherResponse = parseResponse(response.toString());

 // Print some information from the response object
 System.out.println("Location: " + weatherResponse.getLocation().getName());
 System.out.println("Temperature: " + weatherResponse.getCurrent().getTempC() + "°C");
 System.out.println("Condition: " + weatherResponse.getCurrent().getCondition().getText());
 } else {
 System.out.println("Error: " + response.toString());
 }
 } catch (Exception e) {
 e.printStackTrace();
 }
 }

 private static WeatherResponse parseResponse(String jsonResponse) {
 Gson gson = new Gson();
 return gson.fromJson(jsonResponse, WeatherResponse.class);
 }

 public static class WeatherResponse {
 private Location location;
 private CurrentWeather current;

 public Location getLocation() {
 return location;
 }

 public void setLocation(Location location) {
 this.location = location;
 }

 public CurrentWeather getCurrent() {
 return current;
 }

 public void setCurrent(CurrentWeather current) {
 this.current = current;
 }
 }

 public static class Location {
 private String name;

 public String getName() {
 return name;
 }

 public void setName(String name) {
 this.name = name;
 }
 }

 public static class CurrentWeather {
 private float tempC;
 private Condition condition;

 public float getTempC() {
 return tempC;
 }

 public void setTempC(float tempC) {
 this.tempC = tempC;
 }

 public Condition getCondition() {
 return condition;
 }

 public void setCondition(Condition condition) {
 this.condition = condition;
 }
 }

 public static class Condition {
 private String text;

 public String getText() {
 return text;
 }

 public void setText(String text) {
 this.text = text;
 }
 }
}
