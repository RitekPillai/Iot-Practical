from time import sleep
import tm1637

tm=tm1637.TM1637(clk=20,DIO=21,brightness=1.0)
tm.StartClock(military_time=True)

while True:
    tm.ShowDoublePoint(True)
    sleep(1)
    tm.ShowDoublePoint(False)
    sleep(1)