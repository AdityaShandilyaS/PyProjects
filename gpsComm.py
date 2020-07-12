import serial, time

data = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)
file = open("gpslog.txt", "w+")
file.write(" -1 = No Data Received\n")
DOLLAR = 36
LETTERG = 71
LETTERV = 86
LETTERL = 76


def data_read(data):
    serial_data = data.readline()

    return serial_data


def check_for_gnvtg_gpgll(serial_data):
    if len(serial_data):
        if serial_data[0] == DOLLAR and serial_data[1] == LETTERG and (serial_data[3] == LETTERV or serial_data[4] == LETTERL):
            nmea_message = serial_data.decode("utf-8").split(",")
            processed.add(nmea_message)
            if serial_data[3] == LETTERV:
                flag = 0
            else:
                flag= 1
            processed.add(flag)
    return processed


def read_speed(nmea_message):
    if nmea_message[7] == "":
        km = -1
    else:
        km = float(nmea_message[7])

    return km


def read_latlng(nmea_message):

    if nmea_message[1] == "":
        lat = -1
    else:
        lat = float(nmea_message[1])
    coordinates.add(lat)
    northorsouth = nmea_message[2]
    coordinates.add(northorsouth)

    if nmea_message[3] == "":
        lng = -1
    else:
        lng = float(nmea_message[3])
    coordinates.add(lng)
    eastorwest = nmea_message[4]
    coordinates.add(eastorwest)

    utc = nmea_message[5]
    hh = int(utc[0] + utc[1]) + 5
    if hh > 24:
        hh = hh - 23
    coordinates.add(hh)
    mm = int(utc[2] + utc[3]) + 30
    if mm > 60:
        mm = mm - 60
    coordinates.add(mm)
    ss = int(utc[4] + utc[5])
    coordinates.add(ss)

    return coordinates


def print_serial_data(km=None, coordinates=None):
    if coordinates is None:
        print("Speed: ", km, "km/h")
    elif km is None:
        print("Lat: ", coordinates.lat, coordinates.northorsouth, "Lng: ", coordinates.lng, coordinates.eastorwest,
              " UTC: ", coordinates.hh, ":", coordinates.mm, ":", coordinates.ss)

    return 0


def write_to_file(km=None, coordinates=None):
    if coordinates is None:
        file.write("Speed: %f \n" % km)
    elif km is None:
        file.write("Lat: %f " % coordinates.lat)
        file.write(lst[2])
        file.write(" Lng: %f " % coordinates.lng)
        file.write(lst[4])
        file.write(" UTC: %d:" % coordinates.hh)
        file.write("%d:" % coordinates.mm)
        file.write("%d\n" % coordinates.ss)

    return 0


while True:
    try:
        serial = data_read(data)
        decoded = check_for_gnvtg_gpgll(serial)
        if decoded.flag == 0:
            speed = read_speed(decoded.nmea_message)
            print_serial_data(speed)
            write_to_file(speed)
        else:
            latlng = read_latlng(decoded.nmea_message)
            print_serial_data(latlng)
            write_to_file(latlng)

        sleep(10*1000)

    except Exception as e:
        file.close()
        print(e)
        print("Restart")
        break
