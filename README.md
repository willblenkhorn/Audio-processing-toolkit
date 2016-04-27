# Audio-processing-toolkit
Audio processing toolkit which will allow audio filtering using a Fourier transform, short time Fourier transform or a continous wavelet transform. It can also support frequency shifting for voice modulation and volume normalisation throughout a recording.

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
* Create basic GUI using PyQT5 library to display graphical output, enable options, load files etc

## Coding organisation:

* Aim to associate data with their associated functions within a class to better organise the code as it grows
* Class heirarchies with inheritance.
* sndLoad( file ) # loaded into data
* sndPlay( data )
* sndDownSample( data ) # Reduce sampling rate
* sndPadZeros( data ) # FFT() is faster on 2^N length arrays so add zeros to one end to the nearest 2^N
* FFT( data )   # decompose sound into sinusoid and cosine frequencies
* freqShift( data, absShift ) # can shift the sound up or down in frequency by absShift by multiplying the sound's frequency spectrum by a cosine wave
* volumeNorm( data, normMethod ) # detrends the data with respect to time, normMethod could be linear or some tailor expansion
* FIR_filter( data, windowFn, bandwidth, isHighPass, isLowPass )  # This is a filter on the FFT() output
* data is an array, windowFn is a window function to prevent high frequency "ringing", bandwidth is the width of the filter, isHighPass is a bool for if the filter will reduce low frequency amplitudes preserving high frequency amplitudes, isLowPass is a bool for if the filter will reduce high frequency amplitudes preserving low frequency amplitudes.
* IFFT( data ) # converts frequency information back into time information (sound)
* STFFT( data, dt, windowFn ) # Short time FFT() allows the frequencies to monitored as a fn of time, dt is the time interval, windowFn is the window function.
* plot( FFT( data ) ) # graphs the FFT information using Matplotlib
* CWT( data ) # shows how frequency information changes in time using a continuous wavelet transform method
* CWT_smooth( data, blurWidth ) # Apply blur of width blurWidth to CWT
* CWT_filter( data ) # use amplitude to filter, can use local amplitude density to filter too
* plot( CWT( data ) ) # Plots the frequencies present as a function of time

## Background reading:

* CWT is discussed here: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
* CWT library: https://github.com/regeirk/pycwt
* **FIR filters are discussed here** **[READ FIRST]**: http://www.fourier-series.com/fourierseries2/FIR-filter.html
* Implemented using a FFT from numpy: http://www.scipy.org/ there are Faster FFT options to try later: https://github.com/hgomersall/pyFFTW # A FFTW python wrapper with a numpy dropin replacement, handy or SciPy's FFT seems faster than numpy's http://stackoverflow.com/questions/6365623/improving-fft-performance-in-python
* To measure the frequencies as a function of time we divide the signal, apply a "smoothing function" called a window function and then do a FFT: 
* https://en.wikipedia.org/wiki/Short-time_Fourier_transform
* https://en.wikipedia.org/wiki/Window_function
* GUI library for python, which uses the cross-platform PyQT5 toolkit: https://www.riverbankcomputing.com/news
* Graphing library in python: http://matplotlib.org/
* Integrating matplotlib into PyQT: http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
* Graphing library in C++ in case that's too slow: http://www.qcustomplot.com/ which turns out to have some DIY python bindings of it's own https://github.com/dimV36/QCustomPlot-PyQt5  usage: http://developers-club.com/posts/260761/
* Discussion about loading and playing sound files: http://bastibe.de/2013-11-27-audio-in-python.html
* Discussion about normalisation and about Cython for speeding it all up: http://bastibe.de/2012-11-02-real-time-signal-processing-in-python.html
* There are easier alternatives for speedups such a Numba: http://numba.pydata.org/ which uses native python code, lovely.

