# Microython

# ATTENTION la ligne ci dessous doit etre dans boot.py!
from machine import Pin,I2C
from math import pi
from time import sleep

i2c = I2C(scl=Pin(0),sda=Pin(2))

TO_READ = 6

#BMI160_DEVICE_ADDRESS = const(0x69)
#BMI160_DEVICE_ADDRESS = const(105)
bmi = const(104)
bmibis = const(105)

BMI160_OK = const(0xD1)

# Register adress
BMI160_REGA_USR_CHIP_ID         = const(0x00)
BMI160_REGA_USR_ACC_CONF_ADDR   = const(0x40)
BMI160_REGA_USR_ACC_RANGE_ADDR  = const(0x41)
BMI160_REGA_USR_GYR_CONF_ADDR   = const(0x42)
BMI160_REGA_USR_GYR_RANGE_ADDR  = const(0x43)

BMI160_REGA_CMD_CMD_ADDR        = 0x7e
BMI160_REGA_CMD_EXT_MODE_ADDR   = 0x7f
## ---------------------------------------------
CMD_SOFT_RESET_REG      = 0xb6
## ---------------------------------------------
CMD_PMU_ACC_SUSPEND     = 0x10
CMD_PMU_ACC_NORMAL      = 0x11
CMD_PMU_ACC_LP1         = 0x12
CMD_PMU_ACC_LP2         = 0x13
CMD_PMU_GYRO_SUSPEND    = 0x14
CMD_PMU_GYRO_NORMAL     = 0x15
CMD_PMU_GYRO_FASTSTART  = 0x17

# Adresses mémoires à lire pour récup' les données
BMI160_USER_DATA_14_ADDR = 0X12 # accel x (LSB)
BMI160_USER_DATA_15_ADDR = 0X13 # accel x (MSB)
BMI160_USER_DATA_16_ADDR = 0X14 # accel y (LSB)
BMI160_USER_DATA_17_ADDR = 0X15 # accel y (MSB)
BMI160_USER_DATA_18_ADDR = 0X16 # accel z (LSB)
BMI160_USER_DATA_19_ADDR = 0X17 # accel z (MSB)

BMI160_USER_DATA_8_ADDR  = 0X0C 
BMI160_USER_DATA_9_ADDR  = 0X0D
BMI160_USER_DATA_10_ADDR = 0X0E
BMI160_USER_DATA_11_ADDR = 0X0F
BMI160_USER_DATA_12_ADDR = 0X10
BMI160_USER_DATA_13_ADDR = 0X11

chipid = i2c.readfrom_mem(bmi,0x00,1)

# Commandes i2c :
# i2c.writeto_mem(bmi,0x41,int('0b1000').to_bytes(1,'little'))     # définir le range de l'accelerometre en 8g
# bin(int.from_bytes( i2c.readfrom_mem(bmi,0x41,1) ,1 ))           # lire le range de l'accelerometre

class bmi160:
    def __init__(self, no=0):
        #self.bmi = const(0x69)
        #self.bmi = const(105)
        if(no == 0):
            self.bmi = bmi
        else:
            self.bmi = bmibis

        self.chipid = i2c.readfrom_mem(self.bmi,0x00,1)
        self.init_setting()

    def init_setting(self):
        self.initialised = True
        i2c.writeto_mem(self.bmi, BMI160_REGA_USR_ACC_CONF_ADDR, int(0x2c).to_bytes(1,'little'))
        # Verifier en lisant la valeur ci-dessus :
        # bin(int.from_bytes(i2c.readfrom_mem(bmi,BMI160_REGA_USR_ACC_CONF_ADDR,1),1))

        #i2c.writeto_mem(self.bmi, BMI160_REGA_USR_ACC_RANGE_ADDR, int(0x5).to_bytes(1,'little'))
        i2c.writeto_mem(self.bmi,0x41,int('0b1000').to_bytes(1,'little'))     # définir l'accelerometre en 8g
        self.acc_range = bin(int.from_bytes( i2c.readfrom_mem(bmi,0x41,1) ,1 ))

        #i2c.writeto_mem(self.bmi, BMI160_REGA_USR_GYR_CONF_ADDR, int(0x26).to_bytes(1,'little'))
        self.conf_acc(0x26)

        ###i2c.writeto_mem(self.bmi, BMI160_REGA_USR_GYR_RANGE_ADDR, int(0x1).to_bytes(1,'little'))

    def decodeValue(self,value):
        
        if(value > 32768):
            value = value - 65536
        
        #result = (value * pi) / 180
        #result = value / 256
        #result = value * 0.004
        #result = value * 0.244
        result = value / 4096
        return result

    def softReset(self):
        # Use the command register
        # Soft RESET with 0xb6 command
        i2c.writeto_mem(self.bmi, BMI160_REGA_CMD_CMD_ADDR, int(0xb6).to_bytes(1,'little'))

    def reg_write_bits(self,reg,data):
        """
        Write easyly into the IC.
        
        @param reg : register adress in hexa
        @param data : is the data in hexa (but works in bytes)
        """
        i2c.writeto_mem(self.bmi, reg, int(data).to_bytes(1,'little'))

########## ACCELEROMETER'S FUNCTIONS

    def conf_acc(self,data):
        """
        Set the acc parameters.

        @param data : is the data in hexa
        """
        self.reg_write_bits(BMI160_REGA_USR_GYR_CONF_ADDR, data)

    def switch_accel(self,command):
        """
        Active ou non l'accelerometre 
        """


    def getAccelRate(self):
        """
        Set the acc_odr (output data rate).
        @return int: the odr code
        
        *  5 =  25/2Hz
        *  6 =    25Hz
        *  7 =    50Hz
        *  8 =   100Hz
        *  9 =   200Hz
        * 10 =   400Hz
        * 11 =   800Hz
        * 12 =  1600Hz
        * 13 =  3200Hz
        """
        ##return reg_read_bits(BMI160_RA_ACCEL_CONF,  BMI160_ACCEL_RATE_SEL_BIT,  BMI160_ACCEL_RATE_SEL_LEN);
        return int.from_bytes( i2c.readfrom_mem(self.bmi, BMI160_REGA_USR_ACC_CONF_ADDR ,1) ,1 )


    def setAccelRate(self,rate):
        ##return reg_write_bits(BMI160_RA_ACCEL_CONF, rate, BMI160_ACCEL_RATE_SEL_BIT, BMI160_ACCEL_RATE_SEL_LEN);
        return int.from_bytes( i2c.readfrom_mem(self.bmi, BMI160_REGA_USR_ACC_CONF_ADDR ,1) ,1 )

    def readAccRange(self):
        return str(bin(int.from_bytes( i2c.readfrom_mem(bmi,0x41,1) ,1 )))

    def read_accel(self):
        self.acc_value = [0, 0, 0, 0, 0, 0]
        #op_mode set to 0 and go to normal mode
        sleep(0.1)

        i2c.writeto_mem(self.bmi, BMI160_REGA_CMD_CMD_ADDR, int(CMD_PMU_ACC_NORMAL).to_bytes(1,'little'))
        sleep(0.1)

        #read acc xyz
        #acc_value = bus.read_i2c_block_data(BMI160_DEVICE_ADDRESS, BMI160_USER_DATA_14_ADDR, 6)
        self.acc_value = i2c.readfrom_mem(self.bmi,BMI160_USER_DATA_14_ADDR,TO_READ)
        # Read in BINARY = bin(int.from_bytes( i2c.readfrom_mem(bmi,0x40,1) ,1 ))

        self.acc_x =  self.decodeValue( (self.acc_value[1] << 8) + self.acc_value[0] )
        self.acc_y =  self.decodeValue( (self.acc_value[3] << 8) + self.acc_value[2] )
        self.acc_z =  self.decodeValue( (self.acc_value[5] << 8) + self.acc_value[4] )

        self.acc = [self.acc_x, self.acc_y, self.acc_z]

        #print("x: " + str(self.acc_x) + "  y: " + str(self.acc_x) + "   z: " + str(self.acc_x))
        return self.acc;


########## ACCELEROMETER'S FUNCTIONS


    def read_gyro(self):
        self.gyr_value = [0, 0, 0, 0, 0, 0]
        #op_mode set to 0 and go to normal mode
        sleep(0.1)

        i2c.writeto_mem(self.bmi, BMI160_REGA_CMD_CMD_ADDR, int(CMD_PMU_GYRO_NORMAL).to_bytes(1,'little'))
        sleep(0.1)

        #read acc xyz
        #acc_value = bus.read_i2c_block_data(BMI160_DEVICE_ADDRESS, BMI160_USER_DATA_14_ADDR, 6)
        self.gyr_value = i2c.readfrom_mem(self.bmi,BMI160_USER_DATA_8_ADDR,TO_READ)
        # Read in BINARY = bin(int.from_bytes( i2c.readfrom_mem(bmi,0x40,1) ,1 ))

        self.gyr_x =  self.decodeValue( (self.gyr_value[1] << 8) + self.gyr_value[0] )
        self.gyr_y =  self.decodeValue( (self.gyr_value[3] << 8) + self.gyr_value[2] )
        self.gyr_z =  self.decodeValue( (self.gyr_value[5] << 8) + self.gyr_value[4] )

        self.gyr = [self.gyr_x, self.gyr_y, self.gyr_z]

        #print("x: " + str(self.gyr_x) + "  y: " + str(self.gyr_x) + "   z: " + str(self.gyr_x))
        return self.gyr;
