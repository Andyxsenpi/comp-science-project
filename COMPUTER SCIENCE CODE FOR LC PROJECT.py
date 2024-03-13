import serial

connection = serial.Serial("COM3", 115200)


while True:
        print("Waiting on steps")
        data = connection.readline().decode().strip()
        
        if data == "start":
             print("Start signal received.")
        else:
             print("steps:", data)