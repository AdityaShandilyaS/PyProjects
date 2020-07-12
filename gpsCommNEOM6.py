import serial

data = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)
sentence = ""
line = []
file = open("gpslogUART.txt", "w+")
file.write(" -1 = No Data Received\n")


def read_data(data, sbuffer):
    encoded_data = data.readline()
    if len(encoded_data):
        # print(encoded_data)
        if encoded_data != "\n" or encoded_data != "\r":
            # print("string buffer:")
            sbuffer += str(encoded_data)
            # print(sentence)
        else:
            line = sbuffer.split(",")
            # print(line)
            if line[0] == "$GPVTG":
                read_speed(line)
            elif line[0] == "$GPGLL":
                read_latlng(line)
            sbuffer = ""
    return sbuffer


def read_speed(line):
    if line[7] == "":
        km = -1
    else:
        km = float(line[7])
    # km = lst[i-1]
    print("Speed: ", km, "km/h")
    file.write("Speed: %f \n" % km)

    return 0


def read_latlng(line):
    if line[1] == "":
        lat = -1
    else:
        lat = float(line[1])
    if line[3] == "":
        lng = -1
    else:
        lng = float(line[3])
    utc = line[5]
    hh = int(utc[0] + utc[1]) + 5
    if hh > 24:
        hh = hh - 23
    mm = int(utc[2] + utc[3]) + 30
    if mm > 60:
        mm = mm - 60
    ss = int(utc[4] + utc[5])
    print("Lat: ", lat, line[2], "Lng: ", lng, line[4], " UTC: ", hh, ":", mm, ":", ss)
    file.write("Lat: %f " % lat)
    file.write(line[2])
    file.write(" Lng: %f " % lng)
    file.write(line[4])
    file.write(" UTC: %d:" % hh)
    file.write("%d:" % mm)
    file.write("%d\n" % ss)


while True:
    try:
        sentence = readData(data, sentence)

    except Exception as e:
        file.close()
        print(e)
        print("Restart")
        break
