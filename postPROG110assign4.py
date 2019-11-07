#James Post Submission for Assignment 4


#import necessary modules
#import numpy
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#get read and write from scipy's input/output module
from scipy.io.wavfile import write,read

#1.
#Generate a numpy array of uniform random noise at a specified sample-rate and duration (say1.5 seconds)
#create a uniform-distribution noise array, plot it and save it to a wav file
#create 2756 samples with random values between -1 and 1
noise = np.random.uniform(-1,1,2756)


#plot the noise
plt.plot(noise)
#scale the noise to a max of 16 bits (up from -1 to 1)
noise = noise/np.max(np.abs(noise)) * ((2 << 14) -1)
#plot the scaled noise
plt.plot(noise)
#convert to 16 bit ints
noise = np.int16(noise)
#print the values of noise
print(noise)
#write the noise to a new wav file
write("noisy.wav",44100,noise)