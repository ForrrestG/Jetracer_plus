#4-21-23
#Importing required libraies
from jetracer.nvidia_racecar import NvidiaRacecar

import argparse 
#createing the objects, for control over the car robot and parser
car = NvidiaRacecar()

parser = argparse.ArgumentParser()
#adding a way to input into the program "--value" flag
parser.add_argumen('--value', type=float, required=True)
#we are parcing the input of the usser
args = parser.parse_args()
#we're commanding the car to change steering
car.steering = args.value

print = ("the command servor value is:  ", args.value)