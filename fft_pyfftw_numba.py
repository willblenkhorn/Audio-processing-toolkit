"""

This is a FFT and numba profiling test file
FFTW library is 3.56x faster than numpy's fft
Numba is 31x faster than stock python when doing loops over arrays

Numba is 92.8% as fast as numpy when doing simple array modifications,
but being able to change per iteration is a big advantage, 
e.g. conditional modification, not possible in numpy

by Josh Ring
29/04/16

"""
import time # For timing processes
import numpy as np  # Array library more flexible than default
import pyfftw   # FFTW library python bindings
import multiprocessing # Gets num cpu threads
import matplotlib.pyplot as plt # graph plotting
nthreads = multiprocessing.cpu_count()
#from numba import jit

nthreads = multiprocessing.cpu_count()
sampleRate = 128 # Hz
tInput = 100000
lenInput = tInput * sampleRate
freq1 = 20 # Hz  
freq2 = 50 # Hz
nyquist = 2*sampleRate # Hz, this is the max freq, can reliably be sampled
start = time.time() # start timer
"""
@jit # Numba accellerated data initialisation
def dataInit( sampleRate, freq1, freq2 ):

    #Data initialisation function, 
    #accepts sampling rate and two input freq 
    
    input = np.random.rand(lenInput).astype('complex128') # 32 bit real and 32 bit imag
    time_s = np.linspace( 0.0, (lenInput/sampleRate),  num = lenInput )
    
    for i in range(len(input)):
        input[i] += np.cos( 2*np.pi* (time_s[i]) * freq1 )
        input[i] += np.cos( 2*np.pi* (time_s[i]) * freq2 )
    return (input, time_s)


# Initialise the input data
input, time_s = dataInit( sampleRate, freq1, freq2 )
"""

# Numpy data initialisation
time_s = np.linspace( 0.0, (lenInput/sampleRate),  num = lenInput )
input = np.random.rand(lenInput).astype('complex128') # 64 bit real and 64 bit imag
input += np.cos( 2*np.pi*time_s * freq1 ) + np.cos( 2*np.pi*time_s * freq2 )

timetaken = time.time() - start
print('Time taken for data initialisation %.3f secs.' % (timetaken))

pyfftw.forget_wisdom() # Detail of FFTW

start = time.time()
fftout = np.zeros_like(input)
# Setting up and running FFT (forward) calculation
fft = pyfftw.FFTW( input, fftout, direction='FFTW_FORWARD', flags=('FFTW_MEASURE', ), threads=nthreads, planning_timelimit=None )
fft()
timetaken = time.time() - start
print('Time taken for FFT with %d cores is %.3f secs.' % (nthreads, timetaken))

# Frequencies from 0 to 1/2 sampling freq, number of elements = 1/2 total, due to FFT symmetry
freq = np.linspace(0.0, (0.5*sampleRate), (lenInput*0.5))   
fftout = (1/ (0.5*lenInput)) * fftout # FFT normalisation

""" Plot frequencies in signal """
plt.plot( freq, np.abs( fftout[:(0.5*lenInput)] ) ) # Take first half of FFT, take abs value
plt.grid()
plt.show()

""" Plot input signal as a function of time """ # Do not uncomment unless time is <100 s, will overload with data...
#plt.plot( time_s, input )
#plt.show()
