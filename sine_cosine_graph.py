# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:31:09 2019

@author: ramra
"""

# Use NumPy and MatPlotLib to graph one period of sine and cosine on the same set of axes. 
#import numpy and matplotlib libraries used to generate the sin/cosite time and plot the graph
import numpy as np
import matplotlib.pyplot as plot
# Get x values of the graphs starting at 0 and ending at 2Pi.
time        = np.linspace(0, 2*np.pi)
# Amplitude of the sine wave is sine of a variable like time
sin_amplitude   = np.sin(time)
cos_amplitude   = np.cos(time)
tan_amplitude   = np.tan(time)

# Plot a sine wave using time and amplitude obtained for the sine wave
plot.plot(time, sin_amplitude,color="red",label="sine")
plot.plot(time, cos_amplitude,color="blue",label="cosine")
plot.plot(time, tan_amplitude,color="green",label="tangent")

# Give a title for the sine wave plot
plot.title('Sine, Cosine & Tangent wave')
# Give x axis label for the sine wave plot
plot.xlabel('Time')
# Give y axis label for the sine wave plot
plot.ylabel('Amplitude')

plot.xticks((0,np.pi/2,np.pi,np.pi*3/2,np.pi*2),('0','π/2','π','3π/2','2π'))

plot.grid(True, which='both')
plot.axhline(y=0, color='k')
# show the legend
plot.legend()
# show the graph
plot.show()


# Save to a file
figure = plot.figure()
figure.savefig('colab_sine_cosine_tangent.png')

