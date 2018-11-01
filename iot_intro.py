from time import sleep
from iot_gh.IoTGreenhouseService import IoTGreenhouseService

print("IoT Greenhouse.\n")
#Make up a name for your house and enter below
name = "your house name here"

ghs = IoTGreenhouseService()
ghs.greenhouse.name = name
number = ghs.greenhouse.house_number

print("House Number: " + number)

tempF = ghs.temperature.get_inside_temp_F()
print("House temperature is " + str(tempF))
state = ghs.servo.get_status()
print("House state is " + state)

ghs.web_service.post_greenhouse()
