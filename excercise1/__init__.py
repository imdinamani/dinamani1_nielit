import webbrowser
import time
#print("hello world by python!")

#a = "nielit"
#print (a)

'''url1 = "https://www.youtube.com/watch?v=XRnyxCy14Ms"
url2 = "https://www.youtube.com/watch?v=XRnyxCy14Ms"
url3 = "https://www.youtube.com/watch?v=XRnyxCy14Ms"'''

i=1
while(i<4):
    time.sleep(15)
    url = url+i
    webbrowser.open(url)
    i = i+1
