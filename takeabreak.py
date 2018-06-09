import time
import webbrowser
breaks=int(input("enter the numbers of break you want"))
count=0
print("program started on time"+time.ctime())
while(count<breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=_SCdj9d8SUQ")
    count=count+1
