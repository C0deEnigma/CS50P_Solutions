#Voice-Based Weather and Time Assistant
##Video URL - https://youtu.be/HtZxKEi970c

##INTRODUCTION

###The Voice-Based Weather and Time Assistant is a Python-powered application that provides the current date, time, and weather information aloud.
This project is developed with accessibility in mind, focusing on visually impaired individuals as well as those seeking hands-free experience for daily updates.
This assistant incorporates APIs for location and weather retrieval and utilizes text-to-speech technology for natural, spoken output. Its design is based on usability, dynamic functionality, and accessibility.

###File Descriptions

####1. project.py

This file contains the core functionality of the project, which includes:

1-main(): This is the entry point that orchestrates the functions of the assistant. It retrieves the current date, time, and weather and uses the pyttsx3 library to read them aloud.
2-date(): Builds the current date in human-readable format by replacing the numerical parts with the ordinal words, like "Eighth of December."
3-time(): Returns the current time in user-friendly format and adds the relevant time of day, either "AM" or "PM."
4-get_city(): Using the http://ipinfo.io API, it can find out the city the user is coming from.
5-weather(): Retrieves real-time weather information for the city identified by using the OpenWeather API, such as temperature, humidity, wind speed, and a short description of the weather.

###2. test_project.py

This file contains unit tests to ensure that each function in the application is correct. Important aspects of this file include:
1-Testing date(): Ensures that the function formats the date correctly.
2-Testing time(): Ensures that the formatted time output is correct.
3-Testing get_city() and weather(): This utilizes unittest.mock to simulate API responses and tests the functionality without needing an internet connection.
 
###3. requirements.txt
 
It contains a list of the Python libraries required for running this project. The main dependencies are:
1-pyttsx3: It is used for the purpose of text-to-speech.
2-requests: It is used to call APIs for retrieving the weather and geolocation information.
3-num2words: It is used for converting numbers into words so that the spoken output will sound more natural.
2-Live Updates: The application fetches real-time weather data and formats it with location detection.
3-Human Readable Formatting: Ordinal formatting for dates and natural spoken language output ensures clarity and usability.

##Design Decisions

1. Why IP-Based Geolocation?
We decided to fetch the user's location using the http://ipinfo.io API so that the application is dynamic and user-friendly without having to manually input.
This approach simplifies the user experience but could be improved with manual location input as a fallback.
3. API Selection
The OpenWeather API was chosen for its robust, free-tier services that include comprehensive weather information.
However, this API requires an API key for use, adding an initial setup step for users.
4. Text-to-Speech Library
pyttsx3 has been chosen because it is user friendly and offline so that the assistant can keep talking even without internet for the speech synthesis.

##Applications of the Project

1-Assistive Technology for People who are Blind: Suggests blind people audio speech of date, time and weather, thus essential information is not out of one's reach.
2-Easy Information for Users with Busy Schedules: Easy access to information with out looking at the display can be achieved by this assistive technology for general users, while working, commuting, etc.
3-Development Tool: A project for the developers to know how to integrate the APIs, like OpenWeather and IP geolocation, using Python, along with features like text-to-speech.

##Possible Enhancements

1-User Adaptability: Make it a user adaptable where users may choose certain details they desire (like time or just weather).
2-Better Error Handling: Handle errors more gracefully due to networking problems or even API error. This may be providing a default message.
