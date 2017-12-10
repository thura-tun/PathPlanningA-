import cv2
import numpy as numpy
import time 
from skimage.measure import compare_ssim as ssim
import astarsearch
import traversal


def main(image_filename):

	# 2 arrays
	occupied_grids = []
	planned_path = {}

	#load image
	image = cv2.imread(image_filename)
	(winW, winH) = (60, 60)

	obstacles = []
	index = [1,1]

	#create a blank image with zeros
	blank_image = np.zeroes((60,60,3), np.uint8)

	#create an array of 100 blank images
	list_images = [[blank_image for i in xrange(10) for i in xrange[10]]]
	maze = [[0 for i in xrange(10) for i in xrange(10)]]

	

