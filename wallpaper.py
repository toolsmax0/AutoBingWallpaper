import shutil
import ctypes
import requests
import os
if os.path.exists("c:/bingimg"):shutil.rmtree("C:/bingimg")#to delete the old directory
os.makedirs("c:/bingimg")#to make a new directory
url=requests.get("https://area.sinaapp.com/bingImg/")#wo get the link of the picture
with open ("C:/bingimg/wp.jpg","wb") as file:#to save the picture as a local file
    file.write(url.content)
ctypes.windll.user32.SystemParametersInfoW(20,0,"C:/bingimg/wp.jpg",0)#to set the picture as the deskop wallpaper