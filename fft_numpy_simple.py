"""
FFT example, annotated version of: http://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
Vary N and see how the precision changes, vary T also.

This is meant as an intro to numpy basics as well as FFTs and simple plotting with matplotlib

"""

import numpy as np
from scipy.fftpack import fft

N = 600  # Number of sample points
T = 1.0 / 800.0 # sample spacing
x = np.linspace(0.0, N*T, N) # Make linear sequence, start(0), end(N*T), length(N)

# Create vector with two sine waves 50 Hz and 80 Hz of amplitude 1 and 0.5 respect.
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

yf = fft(y)
# Create frequency scale from 0Hz to 1/(0.5*sample interval), of length(N/2)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2) # N.B 1/(2*T) = 1/(samplingFreq*0.5)

import matplotlib.pyplot as plt # Import plotting library

# Plot frequency scale vs (normalised) FFT up until 1/2 way, which is the fft mirror axis.
# Take only the abs value, which does sqrt( imag**2 + real**2 )  N.B [  x**2 = x^2  ]
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2])) 
plt.grid()
plt.show()
