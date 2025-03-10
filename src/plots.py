import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from maths import moving_average

def length_msg_frequency_graph(numbers):
    window_average_size = 5

    frequency = Counter(numbers)

    # Get the sorted list of unique numbers (keys)
    sorted_numbers = sorted(frequency.keys())
    
    # Create the corresponding list of frequencies
    sorted_frequencies = [frequency[num] for num in sorted_numbers]
    smoothed_frequencies = moving_average(sorted_frequencies, window_average_size)


    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_numbers, smoothed_frequencies, label='Smoothed Frequency', color='blue')

    # Adding labels and title
    plt.xlabel('Length of the message')
    plt.ylabel('Frequency')
    plt.title('Frequency of message length with average window_size of ' + str(window_average_size))
    # cut outliers
    plt.xlim(0, 400)
    plt.legend()

    # Display the plot
    plt.savefig('./ressources/img/graph/length_average.png', format='png')