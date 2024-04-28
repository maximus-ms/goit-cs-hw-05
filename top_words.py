import string
import requests

from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from matplotlib import pyplot as plt


def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTP errors if any exceptions
        return response.text
    except requests.RequestException as e:
        return None


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def map_function(word):
    return word, 1


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)


# Perform MapReduce
def map_reduce(text):
    # Remove punctuation and convert to lowercase
    text = remove_punctuation(text).lower()
    words = text.split()

    # Parallel Mapping
    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))

    # Step 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Step 3: parallel reduce
    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)


def visualize_top_words(result, top_n=10):
    top_words = Counter(result).most_common(top_n)
    labels, values = zip(*top_words)
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values)
    plt.xlabel("Frequency")
    plt.ylabel("Words")
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == "__main__":
    # Input text for processing
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    if text:
        # Perform MapReduce on input text
        result = map_reduce(text)
        # Show top 10 words
        visualize_top_words(result, 10)
    else:
        print("Error: Failed to retrieve input text.")
