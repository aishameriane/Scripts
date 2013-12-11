import json
import sys

if __name__ == '__main__':

	filename = sys.argv[1]
	FILE = open(filename,'r')
	lines = FILE.readlines()


	FILE.close()
