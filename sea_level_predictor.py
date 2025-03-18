import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data')
    
    # Line of best fit for entire dataset
    slope1, intercept1, r_value, p_value, std_err = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051)
    plt.plot(years_extended, intercept1 + slope1 * years_extended, 'r', label='Best Fit Line (1880-2050)')
    
    # Line of best fit from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = stats.linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'g', label='Best Fit Line (2000-2050)')
    
    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid()
    
    # Save plot and return data
    plt.savefig("sea_level_plot.png")
    return plt.gca()

# Run the function
draw_plot()
plt.show()
