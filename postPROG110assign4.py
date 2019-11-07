#James Post Submission for Assignment 4


#import necessary modules
#import numpy
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#get read and write from scipy's input/output module
from scipy.io.wavfile import write,read

#1.
#Generate a numpy array of uniform random noise at a specified sample-rate and duration (say 1.5 seconds)
#create a uniform-distribution noise array
#create 66510 samples (1.5 seconds at 44.1kHz) with random values between -1 and 1
noise = np.random.uniform(-1,1,66150)

#2.
#Scale that array to make maximum use of a sixteen-bit sample-space, suitable for writing to a .wav file.
#scale the noise to a max of 16 bits (up from -1 to 1)
noise = noise/np.max(np.abs(noise)) * ((2 << 14) -1)
#convert to 16 bit ints
noise = np.int16(noise)

#3.
#Write the data to a wave file.
#write the noise to a new wav file
write("noisy.wav",44100,noise)


#plot it and save it to a wav file
#plot the noise
plt.plot(noise)

#plot the scaled noise
plt.plot(noise)

#print the values of noise
print(noise)
