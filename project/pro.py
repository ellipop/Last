import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
fromFolder = "C:/Users/Ellinor/Downloads"
toFolder = "C:/Users/Ellinor/Desktop/Todooo/Thing"

china = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class mud(FileSystemEventHandler):
    def on_created(self, event):
        name,extension = os.path.splitext(event.src_path)
        print(event.src_path)
        for key,value in china.items():
            time.sleep(1)
            if extension in value:
                fileName = os.path.basename(event.src_path)
                print("downloading... " + fileName)
                path1 = fromFolder + "/" + fileName
                path2 = toFolder + "/" + key
                path3 = toFolder + "/" + key + "/" + fileName
                
                if os.path.exists(path2):
                    print("moving " + fileName + "...")
                    shutil.move(path1,path3)
                else:
                    print("creating folder...")
                    os.makedirs(path2)
                    print("moving " + fileName + "...")
                    


happens = mud()

iSeeU = Observer()
iSeeU.schedule(happens, fromFolder,recursive=True)
iSeeU.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stop")
    iSeeU.stop()