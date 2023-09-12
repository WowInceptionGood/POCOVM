# this is POCO official lib, for more info visit trypoco.dexpaz.ru
import os
import math

def cdi(arg,image,arg2):
	os.system("docker run"+arg+image+arg2)

def test():
	print("Hello world!")

def setupworkapt():
	os.system("apt-get install docker.io")

