import time
import webbrowser

#Count X time and open google 3 times
total_breaks = 3
break_count = 0

print('This program started on' + time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open('http://google.com.br')
    break_count = break_count + 1