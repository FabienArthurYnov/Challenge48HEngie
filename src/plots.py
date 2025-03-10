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

    print("Saving length_average.png...")
    # save the plot
    plt.savefig('./ressources/img/graph/length_average.png', format='png')

def word_occurence_graph(word_dict):
    words = list(word_dict.keys())
    frequencies = list(word_dict.values())

    # Create the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')

    # Add labels and title
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Word Occurrences in Messages')

    # save the plot
    print("Saving occurence_word.png...")
    plt.savefig('./ressources/img/graph/occurence_word.png', format='png')