# Audio-processing-toolkit-
Audio processing toolkit 

## Aims

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
