#!/usr/bin/python2
import os
from shutil import move

for i in range(10,0,-1):
  filename = 'samples' + str(i) + '.complex'
  filename_next = 'samples' + str(i+1) + '.complex'
  if os.path.exists(filename):
    move(filename,filename_next)
if os.path.exists('samples.complex'):
  move('samples.complex','samples1.complex')
