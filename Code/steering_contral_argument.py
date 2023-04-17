from jetracer.nvidia_racercar import NvidarRacecar

import argparse 

car = NvidiaRacecar()

parser = argparce.ArgumentParser()

parser.add_argument('--value', type=float, required=True)

args = parser.parse_args()

car.steering = args.value

print=("the command servor value is:  ", args.value)