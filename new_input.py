import api_manager
import RPi.GPIO as GPIO
import time


def engageAlarm():
    headers = {'content-type': 'application/json'}
    parameters = {'alarmEngaged': "true"}
    response = api_manager.post_request_with_url(parameters, headers)


def disengageAlarm():
    headers = {'content-type': 'application/json'}
    parameters = {'alarmEngaged': "false"}
    response = api_manager.post_request_with_url(parameters, headers)


GPIO.setmode(GPIO.BCM)

GAS_DETECTOR_GPIO = 17
GPIO.setup(GAS_DETECTOR_GPIO, GPIO.IN)


def takeInput():
    alarm_engaged = false
    currentStatus = GPIO.input(GAS_DETECTOR_GPIO)
    if currentStatus:
        print("1")
        alarm_engaged = true
        engageAlarm()
    else:
        print("2")
        if alarm_engaged == true:
            print("3")
            disengageAlarm()
            alarm_engaged = false
    if alarm_engaged == true:
        print("4")
        time.sleep(5)
    takeInput()


takeInput()
