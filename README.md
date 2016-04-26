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
* Eg. Snd (baseclass) -> loadSnd (inherited)
* Eg. Snd (baseclass) -> fttSnd (inherited)
* Eg. Snd (baseclass) -> cwtSnd (inherited)
* Eg. iface(interface baseclass) -> sndGraph (inherited toggleable pannel)
* Eg. iface(interface baseclass) -> fftGraph (inherited toggleable pannel)
* Eg. iface(interface baseclass) -> cwtGraph (inherited toggleable pannel)
* 
* More concrete plans will be made once we know the data structures we need to organise in more detail.

## Background reading:

CWT is discussed here: https://en.wikipedia.org/wiki/Continuous_wavelet_transform
CWT library: https://github.com/regeirk/pycwt

FIR filters are discussed here: http://www.fourier-series.com/fourierseries2/FIR-filter.html
Implemented using a FFT from numpy: http://www.scipy.org/

To measure the frequencies as a function of time we divide the signal, apply a "smoothing function" called a window function and then do a FFT:
https://en.wikipedia.org/wiki/Short-time_Fourier_transform
https://en.wikipedia.org/wiki/Window_function
