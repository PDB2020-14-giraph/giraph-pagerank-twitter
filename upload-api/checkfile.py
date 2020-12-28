# import time module, Observer, FileSystemEventHandler 
import subprocess
import time 
import sys
import os
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler 
  
  
class OnMyWatch: 
    # Set the directory on watch 
    watchDirectory = "D:\Kuliah\PDB\giraph-pagerank-twitter\\upload-api"
  
    def __init__(self): 
        self.observer = Observer() 
  
    def run(self): 
        event_handler = Handler() 
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True) 
        self.observer.start() 
        try: 
            while True: 
                time.sleep(5) 
        except: 
            self.observer.stop() 
            print("Observer Stopped") 
  
        self.observer.join() 
  
  
class Handler(FileSystemEventHandler): 
  
    @staticmethod
    def on_any_event(event): 
        if event.is_directory: 
            return None
  
        elif event.event_type == 'created':
            if os.path.basename(event.src_path) == 'twt.txt':
            # Event is created, you can process it now 
                print("Watchdog received created event - % s." % os.path.basename(event.src_path))
                p = subprocess.Popen(["powershell.exe", "-ExecutionPolicy","Unrestricted","-File", "D:\Kuliah\PDB\\tugas\docker-call.ps1"], stdout=sys.stdout)
                p.communicate()
                print("page rank output has been created!")
        elif event.event_type == 'modified': 
            # Event is modified, you can process it now 
            print("Watchdog received modified event - % s." % event.src_path) 
              
  
if __name__ == '__main__': 
    watch = OnMyWatch() 
    watch.run() 