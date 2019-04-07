#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Exemplo para apresentação de números no Display          #
#  São apresentados os númeors de 0 até 9 no Display de     #
#  sete segmentos                                           #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 10/07/2017                                         #
#############################################################

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
segments =  (21,20,16,26,19,13,6,5)
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
num = {10:(0,0,0,0,0,0,0),
    0:(1,1,1,1,1,1,0),
    1:(0,1,1,0,0,0,0),
    2:(1,1,0,1,1,0,1),
    3:(1,1,1,1,0,0,1),
    4:(0,1,1,0,0,1,1),
    5:(1,0,1,1,0,1,1),
    6:(1,0,1,1,1,1,1),
    7:(1,1,1,0,0,0,0),
    8:(1,1,1,1,1,1,1),
    9:(1,1,1,1,0,1,1)}
try:
    while True:
        for dig in range(0,11):
            for loop in range(0,7):
                GPIO.output(segments[loop], num[dig][loop])
            time.sleep(.5)
finally:
    GPIO.cleanup()
