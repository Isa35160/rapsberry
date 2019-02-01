# Imports
import os
import glob
import time

# Intialisation des broches
os.system('modprobe w1-gpio')  # Allume le module 1wire
os.system('modprobe w1-therm')  # Allume le module Temperature

# Chemin du fichier contenant la température (remplacer par votre valeur trouvée précédemment)
device_file = '/sys/bus/w1/devices/28-01131a446afe/w1_slave'


# Une fonction qui lit dans le fichier température


# Une fonction qui lit dans le fichier température

class TemperatureSensor:

    def read_temp_raw(self):
        f = open(device_file, 'r')  # Ouvre le dichier
        lines = f.readlines()  # Returns the text
        f.close()
        return lines

    # Lis la temperature
    def Convert(self):
        choice = str(input('Choose your degrees Celsius or Fahrenheit (C or F) : \n'))
        lines = self.read_temp_raw()  # Lit le fichier de température
        # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
        # On relis ensuite le fichier
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw()
        # On cherche le '=' dans la seconde ligne du fichier
        equals_pos = lines[1].find('t=')
        # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
        if equals_pos != -1 and choice == 'C':
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float(temp_string) / 1000.0
            print(temp_c, 'degrés celscius')
        elif equals_pos != -1 and choice == 'F':
            temp_string = lines[1][equals_pos + 2:]
            temp_f = float(temp_string) / 1000.0 * 9 / 5 + 32
            print(temp_f, 'degrés fahrenheit')
    #
    # def ConvertFahrenheit(self):
    #     lines = self.read_temp_raw()  # Lit le fichier de température
    #     # Tant que la première ligne ne vaut pas 'YES', on attend 0,2s
    #     # On relis ensuite le fichier
    #     while lines[0].strip()[-3:] != 'YES':
    #         time.sleep(0.2)
    #         lines = self.read_temp_raw()
    #     # On cherche le '=' dans la seconde ligne du fichier
    #     equals_pos = lines[1].find('t=')
    #     # Si le '=' est trouvé, on converti ce qu'il y a après le '=' en degrées celcius
    #     if equals_pos != -1:
    #         temp_string = lines[1][equals_pos + 2:]
    #         temp_f = float(temp_string) / 1000.0*9/5+32
    #         print(temp_f, 'degrés fahrenheit')


tep= TemperatureSensor()
tep.read_temp_raw()
tep.Convert()



