#Importing required libraies
from jetracer.nvidia_racecar import NvidaRacecar

import argparse 
#createing the objects, for control over the car robot and parser
car = NvidiaRacecar()

parser = argparce.ArgumentParser()
#adding a way to input into the program "--value" flag
parser.add_argument('--value', type=float, required=True)
#we are parcing the input of the usser
args = parser.parse_args()
#we're commanding the car to change steering
car.steering = args.value

print=("the command servor value is:  ", args.value)