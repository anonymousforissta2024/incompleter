#Source: https://stackoverflow.com/questions/53622257/attributeerror-nonetype-object-has-no-attribute-send-pigpiod
import time
import pigpio

START_DELAY=600
FINAL_DELAY=500
STEP=1

GPIO=20

pi = pigpio.pi()

pi.set_mode(GPIO, pigpio.OUTPUT)
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(26,pigpio.INPUT)
pi.set_mode(16,pigpio.INPUT)
#pi.write(21,1)
pi.wave_clear()

statee = 0
try:
    while True:

        pi.write(21,statee)
        pi.wave_clear()

        wf=[]
        offset = pi.wave_get_micros()
        for delay in range(START_DELAY, FINAL_DELAY, -STEP):
           wf.append(pigpio.pulse(1<<GPIO, 0,       delay))
           wf.append(pigpio.pulse(0,       1<<GPIO, delay))

        for i in range(500):
            wf.append(pigpio.pulse(1<<GPIO, 0,       FINAL_DELAY))
            wf.append(pigpio.pulse(0,       1<<GPIO, FINAL_DELAY))
        wf.append(pigpio.pulse(0, 0, offset))

        for delay in range(FINAL_DELAY, START_DELAY, STEP):
           wf.append(pigpio.pulse(1<<GPIO, 0,       delay))
           wf.append(pigpio.pulse(0,       1<<GPIO, delay))

        pi.wave_add_generic(wf)

        wid2 = pi.wave_create()

        #pi.wave_send_once(wid2)
        pi.wave_send_using_mode(wid2, pigpio.WAVE_MODE_ONE_SHOT_SYNC)

        if pi.read(26) == 0:
            pi. wave_tx_stop()
            pi.stop()
        if pi.read(16) == 0:
            pi.wave_tx_stop()
            pi.stop()

        time.sleep(0.75)
        if statee == 0:
            statee = 1
        elif statee == 1:
            statee = 0
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
    pi.wave_tx_stop()
    pi.stop()