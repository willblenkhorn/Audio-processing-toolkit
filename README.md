# Audio-processing-toolkit-
Audio processing toolkit 

## Aims:

* To accept an audio file input with some python audio libraries
* To copy this into an array (numpy array?)
* To see the frequency information in the array via FFT (in numpy)
* To plot the frequency information in the array with Matplotlib
* To use a FIR filter to remove background noise in the sound in the frequency domain
* Use cross-correlation (multiplication of the FFTs) of two independent microphones to reduce noise
* To run a CWT, with the PyCWT library
* Display the results with Matplotlib (as an image)
* To compare FIR filters to a filter made with a CWT with the PyCWT library
* Use CWT to find "low energy" parts of the spectrum and remove these from the result, assumes low energy = noise
* create a "sound profile" of speach and then filter outside this with a CWT to remove background noise eg road (low frequencies)
* Create basic GUI using PySide library to display graphical output, enable options, load files etc

## Coding organisation:

* Aim to associate data with their associated functions within a class to better organise the code as it grows
* Class heirarchies with inheritance.
* sndLoad( file ) # loaded into data
* sndPlay( data )
* sndDownSample( data ) # Reduce sampling rate
* sndPadZeros( data ) # FFT() is faster on 2^N length arrays so add zeros to one end to the nearest 2^N
* FFT( data )   # decompose sound into sinusoid and cosine frequencies
* FIR_filter( data, windowFn, bandwidth, isHighPass, isLowPass )  # This is a filter on the FFT() output
* data is an array, windowFn is a window function to prevent high frequency "ringing", bandwidth is the width of the filter, isHighPass is a bool for if the filter will reduce low frequency amplitudes preserving high frequency amplitudes, isLowPass is a bool for if the filter will reduce high frequency amplitudes preserving low frequency amplitudes.
* IFFT( data ) # converts frequency information back into time information (sound)
* STFFT( data, dt, windowFn ) # Short time FFT() allows the frequencies to monitored as a fn of time, dt is the time interval, windowFn is the window function.
* plot( FFT( data ) ) # graphs the FFT information using Matplotlib
* CWT( data ) # shows how frequency information changes in time using a continuous wavelet transform method
* CWT_smooth( data, blurWidth ) # Apply blur of width blurWidth to CWT
* CWT_filter( data ) # use amplitude to filter, can use local amplitude density to filter too
* plot( CWT( data ) ) # Plots the frequencies present as a function of time
* 
* More concrete plans will be made once we know the data structures we need to organise in more detail.

## Background reading:

* CWT is discussed here: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
* CWT library: https://github.com/regeirk/pycwt
* FIR filters are discussed here: http://www.fourier-series.com/fourierseries2/FIR-filter.html
* Implemented using a FFT from numpy: http://www.scipy.org/
* Faster FFT options to try later:
* https://github.com/hgomersall/pyFFTW # A FFTW python wrapper with a numpy dropin replacement, handy
* SciPy's FFT seems faster than numpy's http://stackoverflow.com/questions/6365623/improving-fft-performance-in-python
* To measure the frequencies as a function of time we divide the signal, apply a "smoothing function" called a window function and then do a FFT: 
* https://en.wikipedia.org/wiki/Short-time_Fourier_transform
* https://en.wikipedia.org/wiki/Window_function
* GUI library for python, which uses the cross-platform QT toolkit: https://wiki.qt.io/PySide
* Graphing library in python: http://matplotlib.org/
* Graphing library in C++ in case that's too slow: http://www.qcustomplot.com/