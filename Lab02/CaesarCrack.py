# Harris Ransom
# Security Engineering Lab 2
# Part 2: Cracking the Crapple Pay Code

# Imports
import string
import matplotlib.pyplot as plt

# Defines character alphabet
alphabet = string.ascii_lowercase

# Defines English alphabet frequencies
englishFrequencies = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}

# Defines sorted English alphabet frequencies
sortedEnglishFrequencies = dict(sorted(englishFrequencies.items(), key=lambda item: item[1], reverse=True))

# Frequency Analysis
def freqAnalysis(text, sort=False):
    # Create dictionary to store letter frequencies
    freqDict = {}
    total = 0
    for letter in alphabet:
        freqDict[letter] = 0

    # Count the frequency of each letter in the text
    for letter in text:
        if letter in alphabet:
            freqDict[letter] += 1
            total += 1

    # Sort freqDict
    if (sort):
        freqDict = dict(sorted(freqDict.items(), key=lambda item: item[1], reverse=True))

    # Print the frequency of each letter
    #for letter in freqDict:
    #    print(f"{letter}: {freqDict[letter]}")

    # Gets relative frequency of each letter
    #print("\nRelative Frequencies:")
    frequencies = []
    for letter in freqDict:
        letterFrequency = (freqDict[letter] / float(total)) #* 100
        frequencies.append(letterFrequency)
        #print(f"{letter}: {letterFrequency:.4f}")

    return freqDict, frequencies

# Plot the relative frequencies
def plotFreqs(freqDict, letterFrequencies):
    # Set up subplots
    fig, (ax1, ax2) = plt.subplots(2)

    # Plots relative frequencies from the text
    rects = ax1.bar(range(len(freqDict)), letterFrequencies, align='center')
    ax1.set_xticks(range(len(freqDict)), list(freqDict.keys()))
    ax1.set_title("Text Letter Frequencies")
    ax1.bar_label(rects, [format(frequency, '.2f') for frequency in letterFrequencies])

    # Plots relative frequencies of the English alphabet
    rects2 = ax2.bar(range(len(sortedEnglishFrequencies)), list(sortedEnglishFrequencies.values()), align='center')
    ax2.set_xticks(range(len(sortedEnglishFrequencies)), list(sortedEnglishFrequencies.keys()))
    ax2.set_title("English Letter Frequencies")
    ax2.bar_label(rects2, [format(frequency, '.2f') for frequency in list(sortedEnglishFrequencies.values())])
    plt.show()

# MAIN
if __name__ == "__main__":
    # Get text from file
    with open("crapple_pay_code.txt") as code_file:
        text = "".join(line for line in code_file)
    text = text.lower()
    print(text)

    # Perform frequency analysis
    freqDict, letterFrequencies = freqAnalysis(text, sort=True)
    #print(freqDict)
    #print(letterFrequencies)

    # Plot the results
    plotFreqs(freqDict, letterFrequencies)

    # TODO: Crack the Caesar cipher in a brute-force manner