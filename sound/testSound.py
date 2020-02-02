#from playsound import playsound
import subprocess

#playsound('beep.mp3')
#for x in range(3):

#subprocess.call(["afplay", "beep.mp3"])
p = subprocess.Popen(["afplay", "beep.mp3"])
p.kill()