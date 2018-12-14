# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 12:30:05 2018

@author: AQ44828
"""
import cv2
import pytube
YouTube('https://www.youtube.com/watch?v=ng8Wivt52K0').streams.first().download()

yt = pytube.YouTube('https://www.youtube.com/watch?v=LIVa_nkU0j4')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


video = cv2.VideoCapture('Crowded People Walking Down Oxford Street London 4K UHD Stock Video Footage.mp4')

success,image = video.read()
count = 0
while success:
  cv2.imwrite("images/frame%d.JPEG" % count, image,[int(cv2.IMWRITE_JPEG_QUALITY),1000])     # save frame as JPEG file      
  success,image = video.read()
  print('Read a new frame: ', success)
  count += 1
  