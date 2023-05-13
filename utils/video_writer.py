# -*- coding: utf-8 -*-
# @Author: ath
# @Date:   2023-03-11 16:15:03
# @Last Modified by:   ath

import cv2


class VidWriter:
	# defining the opencv video writer
	def __init__(self, frame, timestep  = 0, save_path = './videos', ):
		self.frame = frame
		self.save_path = save_path+f'/learned_model_{timestep * 1000}.mp4'
		self.writer = cv2.VideoWriter(self.save_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (self.frame.shape[0] * 4 , self.frame.shape[1] * 4))

		# h264 as codec gives an encoder error. safest to use mp4v, however firefox (probably other browsers too) doesn't natively support this   

	def write(self, frame):
		# scale frame to four times for easy viewing
		resized_frame = cv2.resize(frame, dsize = (self.frame.shape[0] * 4 , self.frame.shape[1] * 4), interpolation = cv2.INTER_CUBIC)
		self.writer.write(resized_frame[:, :, ::-1])

	def close(self):
		self.writer.release()


		
