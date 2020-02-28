def clock():
    import time
    print('Seconds since beginning')
    count = 0
    while True:
        print(count, end="\r")
        time.sleep(1)
        count += 1
