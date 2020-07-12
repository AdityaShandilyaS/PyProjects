import serial

class gpsComm:

    def __init__(self):
        data = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)

        file = open("gpslog.txt", "w+")
        file.write(" -1 = No Data Received\n")
        lst = []
        frame = []

    def dataRead(data):
        encoded_data = data.readline()
        if len(encoded_data):
            # print(encoded_data)
            lst = encoded_data.decode("utf-8").split(",")
            frame.add(lst)

            if encoded_data[0] == 36 and encoded_data[1] == 71 and (encoded_data[3] == 86 or encoded_data[4] == 76):
                i = 0
                lst = encoded_data.decode("utf-8").split(",")
                # print(lst)
                if encoded_data[3] == 86:
                    readSpeed(lst)
                else:
                    readLatLng(lst)
                # time.sleep(0.125)
        return 0

    def readSpeed(lst):
        if lst[7] == "":
            km = -1
        else:
            km = float(lst[7])
        # km = lst[i-1]
        print("Speed: ", km, "km/h")
        file.write("Speed: %f \n" % km)

        return 0

    def readLatLng(lst):
        if lst[1] == "":
            lat = -1
        else:
            lat = float(lst[1])
        # lat = lst[1]
        if lst[3] == "":
            lng = -1
        else:
            lng = float(lst[3])
        # lng = lst[3]
        utc = lst[5]
        hh = int(utc[0] + utc[1]) + 5
        if hh > 24:
            hh = hh - 23
        mm = int(utc[2] + utc[3]) + 30
        if mm > 60:
            mm = mm - 60
        ss = int(utc[4] + utc[5])
        print("Lat: ", lat, lst[2], "Lng: ", lng, lst[4], " UTC: ", hh, ":", mm, ":", ss)
        file.write("Lat: %f " % lat)
        file.write(lst[2])
        file.write(" Lng: %f " % lng)
        file.write(lst[4])
        file.write(" UTC: %d:" % hh)
        file.write("%d:" % mm)
        file.write("%d\n" % ss)

        return 0
