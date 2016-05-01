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
tInput = 0.02 # Seconds
lenInput = tInput * sampleRate
freq1 = 2000 # Hz  
freq2 = 500 # Hz
nyquist = 2*sampleRate # Hz, this is the max freq, can reliably be sampled
time_s = np.linspace( 0.0, (lenInput/sampleRate),  num = lenInput ) # Time for cosine functions

def dataInitialise(lenInput, sampleRate):
    """
    Creates linear sequences for time to create cosines of known frequencies
    Creates noise to add to the signal
    Returns fft test input data as a numpy array
    """
    start = time.time() # start timer
    #inputData = np.zeros(lenInput).astype('complex128') # To initialise the data without noise uncomment this
    # Noise
    inputData = 1*np.random.rand(lenInput).astype('complex128') # 64 bit real and 64 bit imag, further 4x speed if use 32bit
    # Signal frequencies
    inputData += 1*np.cos( 2*np.pi*time_s * freq1 ) + 1*np.cos( 2*np.pi*time_s * freq2 )
    dataAverage = np.average( inputData )
    inputData -= dataAverage # Detrending the input data so it is zero centred
    
    timetaken = time.time() - start
    print('Time taken for data initialisation %.3f secs.' % (timetaken))
    return inputData 


def fft( fftInput ):
    """
    Takes fftInput as numpy array
    Returns forward FFT calculated by FFTW
    """
    pyfftw.forget_wisdom() # Detail of FFTW needed to stop it messing up
    start = time.time()
    fftOutput = np.empty_like( fftInput )
    # Setting up and running FFT (forward) calculation
    fft = pyfftw.FFTW( fftInput, fftOutput, direction='FFTW_FORWARD', flags=('FFTW_MEASURE', ), threads=nthreads, planning_timelimit=None )
    fft()
    
    timetaken = time.time() - start
    print('Time taken for FFT with %d cores is %.3f secs.' % (nthreads, timetaken))
    fftOutput *= (1/ (0.5*len(fftOutput)) ) # FFT normalisation
    return fftOutput
    

def primativeFilter( filterInput ):
    """
    Very simple filter which just zeros frequencies
        You must use np.copy to avoid simply passing a reference
    """
    filterOutput = np.copy( filterInput )
    bandwidth = int( len(filterOutput)*0.5*0.95 )
##
    filterOutput[ (len(filterOutput)*0.5-bandwidth) : (len(filterOutput)*0.5+bandwidth) ] = 0.+0.J
    return filterOutput
    
    
def ifft( ifftInput ):
    """
    Takes ifftInput as numpy array
    Returns backward (reverse) FFT calculated by FFTW
    """
    pyfftw.forget_wisdom() # Detail of FFTW needed to stop it messing up
    start = time.time()
    
    
    ifftOutput = np.empty_like( ifftInput )
    # Setting up and running FFT (Backward) calculation
    fft = pyfftw.FFTW( ifftInput, ifftOutput, direction='FFTW_BACKWARD', flags=('FFTW_MEASURE', ), threads=nthreads, planning_timelimit=None )
    fft()
    
    timetaken = time.time() - start
    print('Time taken for FFT with %d cores is %.3f secs.' % (nthreads, timetaken))
    ifftOutput *=  0.5*len(ifftOutput) # FFT normalisation
   
    
    return ifftOutput


def plotGraphs( originalData, originalFFT, filteredData, filteredFFT, samplingRate ):
    """
    Use matplotlib to plot graphs
    TODO: Not currently set up to handle odd numbered lengths of input
    """
    halfLength = int( lenInput/2 ) # Used for graphing, needs ints
    # Frequencies from 0 to 1/2 sampling freq, number of elements = 1/2 total, due to FFT symmetry
    freqAxis = np.linspace( 0.0, (0.5*samplingRate), (0.5*lenInput) )   

    f, axarr = plt.subplots(2, 2)
    axarr[0, 0].set_title('Signal orig.') 
    axarr[0, 0].plot( time_s, originalData )
    axarr[1, 0].set_title('FFT original')
    axarr[1, 0].plot( freqAxis, np.abs( originalFFT[:halfLength] ) )
    axarr[0, 1].set_title('Signal filt.')
    axarr[0, 1].plot( time_s, filteredData )
    axarr[1, 1].set_title('FFT filt')
    axarr[1, 1].plot( freqAxis, np.abs( filteredFFT[:halfLength] ) )
    
    plt.show()

# Run the functions; compute and look at output
#--------------------------------------------------
data = dataInitialise(lenInput, sampleRate)
dataFFT = fft( data )
dataFFTfiltered = primativeFilter( dataFFT )
dataFiltered = ifft( dataFFTfiltered )


plotGraphs( data, dataFFT, dataFiltered, dataFFTfiltered, sampleRate )



