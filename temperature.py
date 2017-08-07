import Adafruit_DHT
import time #delay
import datetime #impe pasing
import MySQLdb


sensor = Adafruit_DHT.DHT11
pin = 24 #GPIO

db = MySQLdb.connect("localhost","root","1234","temperature")
cur = db.cursor()

        
while True:
        wtime = datetime.datetime.now()
        print(wtime)
        t_year = wtime.strftime('%Y')
        t_month = wtime.strftime('%m')
        t_day = wtime.strftime('%d')
        t_hour = wtime.strftime('%H')
        t_min = wtime.strftime('%M')

        humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
        print(t_year,t_month,t_day,t_hour,t_min,humidity)
        sql = "insert into DHT11 values ('%s','%s','%s','%s','%s','%s','%s')" %(t_year,t_month,t_day,t_hour,t_min,humidity,temperature)
        try:
                cur.execute(sql)
                db.commit()
        except:
                db.rollback()
        time.sleep(60)
        
        
cur.close()
db.close()



