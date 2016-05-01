"""
This is a FFT profiling test file
FFTW library is 3.56x faster than numpy's fft

by Josh Ring
01/05/16
"""
import time # For timing processes
import numpy as np  # Array library more flexible than default
import pyfftw   # FFTW library python bindings
import multiprocessing # Gets num cpu threads
import matplotlib.pyplot as plt # graph plotting

nthreads = multiprocessing.cpu_count()
sampleRate = 41000 # Hz
tInput = 0.1 # Seconds
lenInput = tInput * sampleRate
freq1 = 200 # Hz  
freq2 = 7000 # Hz
nyquist = 2*sampleRate # Hz, this is the max freq, can reliably be sampled
time_s = np.linspace( 0.0, (lenInput/sampleRate),  num = lenInput ) # Time for cosine functions

def dataInitialise(lenInput, sampleRate):
    """
    Creates linear sequences for time to create cosines of known frequencies
    Creates noise to add to the signal
    Returns fft test input data as a numpy array
    """
    start = time.time() # start timer
    
    inputData = 2*np.random.rand(lenInput).astype('complex128') # 64 bit real and 64 bit imag, further 4x speed if use 32bit
    inputData += np.cos( 2*np.pi*time_s * freq1 ) + np.cos( 2*np.pi*time_s * freq2 )
    dataAverage = np.average( inputData )
    inputData -= dataAverage # Detrending the input data so it is zero centred
    
    timetaken = time.time() - start
    print('Time taken for data initialisation %.3f secs.' % (timetaken))
    return inputData 


def fft( inputData ):
    """
    Takes inputData as numpy array
    Returns forward FFT calculated by FFTW
    """
    pyfftw.forget_wisdom() # Detail of FFTW
    start = time.time()
    fftOutput = np.empty_like(inputData)
    # Setting up and running FFT (forward) calculation
    fft = pyfftw.FFTW( inputData, fftOutput, direction='FFTW_FORWARD', flags=('FFTW_MEASURE', ), threads=nthreads, planning_timelimit=None )
    fft()
    
    timetaken = time.time() - start
    print('Time taken for FFT with %d cores is %.3f secs.' % (nthreads, timetaken))
    fftOutput = (1/ (0.5*len(fftOutput)) ) * fftOutput # FFT normalisation
    return fftOutput


def plotGraphs( fftOutput, sampleRate ):
    """
    Use matplotlib to plot graphs
    
    TODO: Not currently set up to handle odd numbered lengths of input
    """
    lenInput = int( len(fftOutput) )
    halfLenInput = int( lenInput/2 ) # Used for graphing 

    # Frequencies from 0 to 1/2 sampling freq, number of elements = 1/2 total, due to FFT symmetry
    freq = np.linspace( 0.0, (0.5*sampleRate), (0.5*lenInput) )   

    
    """ Plot frequencies in signal """
    plt.subplot(2, 1, 1)
    plt.plot( freq, np.abs( fftOutput[:halfLenInput] ) ) # Take first half of FFT, take abs value
    plt.title('Frequency and time data')
    plt.ylabel('Amplitude a.u.')
    plt.xlabel('Frequency / Hz')
    plt.grid()
    
    """ Plot input signal as a function of time """ 
    plt.subplot(2, 1, 2)
    plt.plot( time_s, inputData )
    plt.xlabel('time / s')
    plt.ylabel('Intensity')
    plt.grid()
    
    plt.show()
    

# Run the functions; compute and look at output
#--------------------------------------------------
inputData = dataInitialise(lenInput, sampleRate)
fftOutput = fft( inputData )
plotGraphs( fftOutput, sampleRate )




    





