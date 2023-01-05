def create_list(words_file, ipa_file):
    # Open the files
    with open(words_file, "r", encoding="utf-8") as words:
        with open(ipa_file, "r", encoding="utf-8") as ipa:
            # Read the lines from the files into lists
            word_list = words.readlines()
            ipa_list = ipa.readlines()
            
            # Remove the newline characters from the lists
            word_list = [word.strip() for word in word_list]
            ipa_list = [ipa.strip() for ipa in ipa_list]

            # Zip the lists together into a list of tuples
            combined_list = list(zip(word_list, ipa_list))

            # Return the list as a string
            return str(combined_list)

# Test the function
print(create_list("words.txt", "ipa.txt"))
