#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
from  pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stop):
    mixer.init()
    mixer.music.load()
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stop:
            mixer.music.stop()
            break

def log_file(msg):
    with open("music.mp3","a")as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyeexe = time()
    init_exe = time()
    water_sec = 30*60
    eye_exe = 40*60
    exec = 45*60

    while True:
        if time() - init_water > water_sec:
            print("water drinking time type Drank to stop")
            musiconloop("music.mp3","Drank")
            init_water = time()
            log_file("you drank at:")

        elif time() - init_eyeexe > eye_exe:
            print("eye excercise time type done to stop")
            musiconloop("eye.mp3", "done")
            init_eyeexe = time()
            log_file("you do your eye excercise at:")

        elif time() - init_exe > exec:
            print("excercise time press done to stop ")
            musiconloop("exc.mp3", "done")
            init_exe = time()
            log_file("you done your excercise at:")

