import psutil

if __name__ == '__main__':
    # for x in range(10):
    #     print(psutil.cpu_percent(interval=1,percpu=True))

    print(psutil.disk_partitions())