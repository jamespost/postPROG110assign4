#James Post Submission for PROG110 Assignment 4

#import necessary modules
#import numpy
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
#get write from scipy's input/output module
from scipy.io.wavfile import write

#methods provided on handout in class on 11/6/2019 (used to complete problems 5 and 6)
#a method to generate nrCycles of a sine wave (provided on handout in class 11/6/19)
def generateSinewave(nrCycles, nrdataPointsPerCycles = 2048):
    """a method to generate nrCycles of a sine wave """
    cycles = np.linspace(0,nrCycles * 2 * np.pi, nrdataPointsPerCycles)
    cyclesArray = np.array(np.sin(cycles))
    plt.plot(cyclesArray)
    plt.xlabel('angle [rad]')
    plt.ylabel('sin (x)')
    plt.axis('tight')
    plt.show()
    
    wave = int16scale(cyclesArray)
    plt.plot(wave)
    plt.xlabel('angle [rad]')
    plt.ylabel('sin (x)')
    plt.axis('tight')
    plt.show()

#a method to scale the data in numpy arrays to a 16bit data space ((provided on handout in class 11/6/19)
def int16scale(npArray):
    """a method to scale the data in numpy arrays to a 16bit data space"""
    maxVal = np.max(np.abs(npArray))
    int16Scaler = (2**15) - 1
    res = npArray/maxVal * int16Scaler
    return res

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

#4.
#Using the matplotlib plotting routines, plot the waveform data to screen
#plot the noise
plt.plot(noise)

#5. && #6.
#Generate a numpy array of samples of one cycle of a sine wave and plot the array.
generateSinewave(1)

#7.
#Generate a numpy array of samples of two cycles of a sine wave and plot the array.
generateSinewave(2)