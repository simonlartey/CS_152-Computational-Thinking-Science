
'''Simon Lartey
CS152B
11/07/2023
'''

# wordmap.py

def main():
    # Print out a prompt for the user
    print("Please provide responses to the following prompts:")

    # Create a list of words
    words = ["yes_", "no_", "apple_", "banana_", "dog_", "cat_", "red_", "blue_", "happy_", "sad_"]

    # Create an empty dictionary
    mapping = {}

    # Loop over the words list
    for word in words:
        # Assign a response using the input function
        response = input(f"Enter a response for '{word}': ")
        
        # Assign the response to the dictionary with the word as the key
        mapping[word] = response

    # Loop over the keys in the dictionary and print key/response pairs
    for key in mapping.keys():
        print(f"{key}: {mapping[key]}")

if __name__ == "__main__":
    main()
