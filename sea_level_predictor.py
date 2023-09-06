import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv') 

    # Create scatter plot
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope1, intercept1, r, p, se = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(1880,2060,10)
    best_fit_line_1 = slope1 * x1 + intercept1
    plt.plot(x1,best_fit_line_1,color = 'red')

    # Create second line of best fit
    slope2, intercept2, r, p, se = linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000,2060,10)
    best_fit_line_2 = slope2 * x2 + intercept2
    plt.plot(x2,best_fit_line_2,color = 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()