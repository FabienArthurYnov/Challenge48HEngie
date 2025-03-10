

def moving_average(data, window_size):
    """
    Return the moving_avg of data with window_size
    """
    # Create a list to hold the moving averages
    moving_avg = []
    for i in range(len(data)):
        # Define the window's start and end based on the index and window size
        start = max(i - window_size + 1, 0)
        end = i + 1
        
        # Calculate the average of the values in the window
        avg = sum(data[start:end]) / (end - start)
        moving_avg.append(avg)
    return moving_avg

def sci_str_to_int(s):
    return int(float(s.replace(',', '.')))