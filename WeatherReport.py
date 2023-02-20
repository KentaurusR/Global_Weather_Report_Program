import requests # We need the requests module to connect to the API and request data from it
import json

# In this code, you will see 'f' in front of strings, these are called f-strings, or 'formatted string literals'
# These allow you to incorporate curly braces containing expressions that can be replaced with values

def weather_report():
    # API endpoint URL and API request parameters
    lat = 47.6062
    lon = -122.3321
    api_key = "<Insert API Key Here>"
    target_location = "Seattle, Washington"
    print("The default latitude and longitude is set to (47.6062, -122.3321).\nThese are the coordinates for Seattle, Washington.")
    change_coordinates = input("Would you like to change the coordinates? Yes or No?: ").lower()
    while True:
        if change_coordinates == "yes":
            print("Please enter the new coordinates you would like to use.")
            # We need to validate the latitude and longitude inputs, to make sure they are valid real-world coordinates
            # Valid latitude values are between -90 and 90
            # Valid longitude values are between -180 and 180
            while True:
                lat = input("Latitude: ")
                try:
                    lat = float(lat)
                    if -90 <= lat <= 90:
                        break
                    else:
                        print("Please enter a valid latitude between -90 and 90.")
                except ValueError:
                    print("Please enter a valid number for latitude.")

            while True:
                lon = input("Longitude: ")
                try:
                    lon = float(lon)
                    if -180 <= lon <= 180:
                        break
                    else:
                        print("Please enter a valid longitude between -180 and 180.")
                except ValueError:
                    print("Please enter a valid number for longitude.")
            # We need to check to see if the API has data for the provided coordinates, so we don't cause an error
            # In other words, we need to check if the provided coordinates
            try:
                check_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
                check_response = requests.get(check_url)
                check_data = check_response.json()
                # The code continues inside this try block if the API has data, if the API does not have data, it will ask for new coordinates
                if not len(check_data) == 0 or check_data[0]["name"] == "":
                    # Now, we check if the response code is 200, which is what we want if we are going to connect to the API
                    # We use the reverse_geocode_url so we can determine what the location the coordinate pair matches with
                    # Since most people don't have a lot of coordinates memorized, this allows the program to be used for more fun weather/geography purposes
                    if check_response.status_code == 200:
                        reverse_geocode_url = f"https://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid={api_key}"
                        georesponse = requests.get(reverse_geocode_url)
                        if georesponse.status_code == 200:
                            geo_data = georesponse.json()
                            location_name = geo_data[0]["name"]
                            print(f"The provided coordinates ({lat},{lon}) are in {location_name}.")
                        else:
                            # It is uncommon, but there may be cases where there is valid data, but no location name
                            print(f"We failed to get a location name for the ({lat},{lon}), but we will still check the weather for this location.")
                            target_location = f"({lat},{lon})"
                        target_location = location_name
                        break
                    else:
                        print(
                            f"The API does not have data for the coordinates ({lat},{lon}), please provide new coordinates.")
                else:
                    print(
                        f"The API does not have data for the coordinates ({lat},{lon}), please provide new coordinates.")
            except:
                print(f"The API does not have data for the coordinates ({lat},{lon}), please provide new coordinates.")




        elif change_coordinates == "no":
            break
        else:
            change_coordinates = input("Please enter 'yes' or 'no': ").lower()

    endpoint_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    # Now, we need to send our API request
    response = requests.get(endpoint_url)

    # Now, we check the response status code, if the response status code is 200, it means our API request it successful
    if response.status_code == 200:
        data = response.json()
        # If the response is okay, we will be able to retrieve the JSON data

        # Now, we want to retrieve the weather information from the JSON data
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2) # We need to convert the data from Open Weather API to Celsius, and we round it to the second decimal
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print the weather information
        print("\n")
        print(f"The weather in " + target_location + f" is currently {weather}.")
        print(f"The temperature is {temperature}°C.")
        print(f"The humidity is {humidity}%.")
        print(f"The wind speed is {wind_speed} m/s.")

        print("\n")
        while True:
            repeat = input("Would you like to look at current weather data from a different location? Yes or No?: ").lower()
            if repeat == "yes":
                print("\n")
                weather_report()
            elif repeat == "no":
                print("Thank you for using this program, have a nice day!")
                exit()
            else:
                print("Please enter 'yes' or 'no'.")

    else:
        print("The API request failed. Please check your API Key or your internet connection.")

while True:
    print("Welcome to my Weather Report Program!")
    print("This program uses the Open Weather Map API.\nYou can enter latitude and longitude coordinates to find current weather data across the world.")
    print("The data is presented using the imperial system.\n")
    weather_report()


