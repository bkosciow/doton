from worker.openweather import OpenweatherWorker
import time
 
if __name__ == '__main__':
    w = OpenweatherWorker('f84b3bdc96fa56451de722087658bffb')
    print("start")
    w.start()
    try:
        while 1:
            d = w.weather()
            print("current weather :", d)
            d = w.forecast()
            print("forecast :", d)
            print("-----------------")
            time.sleep(5)
    except KeyboardInterrupt:
        print("closing...")
    except:
        raise
    finally:
        w.shutdown()