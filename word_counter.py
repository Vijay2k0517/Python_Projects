from collections import Counter

def wordCounter():
    text = input("Enter the text or Paragraph: ")

    text = text.strip().lower() 

    words = text.split()  

    no_of_words = len(words)  

    frequency_of_word = Counter(words) 

    print(f"The total number of words: {no_of_words}")
    print("Frequency of words:")
    for word, count in frequency_of_word.items():
        print(f"{word}: {count}")

wordCounter()
