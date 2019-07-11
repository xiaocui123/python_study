from datetime import datetime

if __name__ == '__main__':

    dt=datetime.now()

    print("now is %s" % dt)

    t=dt.timestamp()

    print("timestamp %d" %t)

    print("timestamp2time is %s" %datetime.fromtimestamp(t))

    cday=datetime.strptime("2019-5-16 15:02:12",'%Y-%m-%d %H:%M:%S')

    print("datetime.strptime:%s" %cday)

    print("datetime.strftime %s" % dt.strftime('%a, %b %d %H:%M'))




