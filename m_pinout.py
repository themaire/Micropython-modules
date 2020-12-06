#### Variables ####
#pinmap="     PINOUT\nADC      TOUT ----- GPIO 16_ USER    WAKE \nRéservé       ----- GPIO 5                \nRéservé       ----- GPIO 4 ~              \nGPIO 10  SSD3 ----- GPIO 0   FLASH        \nGPIO 9   SDD2 ----- GPIO 2   TX D1        \nMOSI     SDD1 ----- 3.3V                  \nCS      SDCMD ----- GND                   \nMISO     SDD0 ----- GPIO 14          HSCLK\nSCLK    SDCLK ----- GPIO 12          HMISO\nGND           ----- GPIO 13  RX D2   HMOSI\n3.3V          ----- GPIO 15  TX D2     HCS\nEN            ----- GPIO  3  RX D0        \nRST           ----- GPIO  1  TX D0        \nGND           ----- GND                   \nVIN           ----- 3.3V\n"

pinmap=(
"       --        PINOUT       --          ",
"ADC      TOUT | A0 ----- D0  | GPIO 16  USER     WAKE",
"Réservé       |    ----- D1  | GPIO 5                ",
"Réservé       |    ----- D2  | GPIO 4 ~              ",
"GPIO 10  SSD3 |    ----- D3  | GPIO 0   FLASH        ",
"GPIO 9   SDD2 |    ----- D4  | GPIO 2   TX D1        ",
"MOSI     SDD1 |    ----- 3.3 | 3.3V                  ",
"CS      SDCMD |    ----- GND | GND                   ",
"MISO     SDD0 |    ----- D5  | GPIO 14 ~        HSCLK",
"SCLK    SDCLK |    ----- D6  | GPIO 12 ~        HMISO",
"GND           |    ----- D7  | GPIO 13  RX D2   HMOSI",
"3.3V          |    ----- D8  | GPIO 15 ~TX D2     HCS",
"EN            |    ----- RX  | GPIO  3  RX D0        ",
"RST           |    ----- TX  | GPIO  1  TX D0        ",
"GND           |    ----- GND | GND                   ",
"VIN           |    ----- 3.3 | 3.3V                  ",
"                                              ~ : PWM"
)

#### Fonctions ####
def pinout():
    for i in pinmap:
        print(i)

#### Programme ####
if __name__ == '__main__':

    pinout()
