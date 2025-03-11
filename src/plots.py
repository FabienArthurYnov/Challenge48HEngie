import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from maths import moving_average


def prepare_num_for_occurence_plot(numbers, window_average_size):
    """
    Input a list of numbers to output the sorted_number and corresponding frequencies (with a window average)
    """
    frequency = Counter(numbers)

    # Get the sorted list of unique numbers (keys)
    sorted_numbers = sorted(frequency.keys())
    
    # Create the corresponding list of frequencies
    sorted_frequencies = [frequency[num] for num in sorted_numbers]
    smoothed_frequencies = moving_average(sorted_frequencies, window_average_size)
    return sorted_numbers, smoothed_frequencies


def length_msg_frequency_graph(numbers):
    window_average_size = 5

    sorted_numbers, smoothed_frequencies = prepare_num_for_occurence_plot(numbers, window_average_size)

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

def msg_per_weekday(datetimes):
    sorted_numbers, smoothed_frequencies = prepare_num_for_occurence_plot(datetimes, 1)

    plt.figure(figsize=(10, 6))
    plt.bar(sorted_numbers, smoothed_frequencies, label='Frequency of messages', color='blue')

    # Adding labels and title
    plt.xlabel('Weekday')
    plt.ylabel('Frequency')
    plt.title('Frequency of messages per weekday')
    plt.legend()

    print("Saving message_weekday.png...")
    # save the plot
    plt.savefig('./ressources/img/graph/message_weekday.png', format='png')

def msg_per_date(datetimes):
    sorted_numbers, smoothed_frequencies = prepare_num_for_occurence_plot(datetimes, 5)

    plt.figure(figsize=(10, 6))
    plt.plot(sorted_numbers, smoothed_frequencies, label='Smoothed Frequency of messages', color='blue')

    # Adding labels and title
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.title('Frequency of messages per date')
    plt.legend()

    print("Saving message_date.png...")
    # save the plot
    plt.savefig('./ressources/img/graph/message_date.png', format='png')

def word_occurence_graph(word_dict):
    words = list(word_dict.keys())
    frequencies = list(word_dict.values())

    # Create the bar plot
    plt.figure(figsize=(200, 6))
    plt.bar(words, frequencies, color='skyblue', width=0.5)

    # Add labels and title
    plt.xticks(rotation=60, ha="right", fontsize=7)
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Word Occurrences in Messages')
    plt.tight_layout()

    # save the plot
    print("Saving occurence_word.png...")
    plt.savefig('./ressources/img/graph/occurence_word.png', format='png')