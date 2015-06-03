import webbrowser
import time

print("This program started on " + time.ctime())
for x in range(0,3):
	time.sleep(1*60*60)
	webbrowser.open_new("https://www.youtube.com/watch?v=8mP5xOg7ijs")
