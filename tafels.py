import time
for i in range(1, 51):
    for j in range(1, 51):
        print(i * j, end=' ')
    print()
    time.sleep(0.000001)
