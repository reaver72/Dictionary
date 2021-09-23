# Dictionary
import json
from difflib import get_close_matches
import time

Continue = ""
data = json.load(open("data.json"))
keys = data.keys()
while Continue == "":
    keyword = input("Enter the word you want to search: ")

    while len(keyword) < 1:
        message = print("Warning!\n"
                        "Blank keyword is restricted!\n")
        keyword = input("Enter the word you want to search: ")
        print(f"Searching the word '{keyword}'....\n")
        time.sleep(1.2)
    close_words = get_close_matches(f"{keyword}", keys, cutoff=0.75)

    def meaning(word):

        word = word.lower()
        if word in data.keys():
            result = data[word]
            for i in range(len(result)):
                print(result[i])
        else:
            print(
                f"Sorry, the word '{keyword}' doesn't exist in this dictionary.")
            print(
                f"You can search the word '{keyword}' in web for more information")

            try:
                keyword_new = input(
                    f"\nDid you mean '{close_words[0]}' instead? ")
                if keyword_new == "y" or keyword_new == "yes" or keyword_new == "yeah":
                    print(f"Searching the word '{close_words[0]}'....\n")
                    time.sleep(1.2)
                    meaning(close_words[0])
                else:
                    new_keyword = input(
                        "\nWhat word are you looking for? Type here correctly: ")
                    while len(new_keyword) < 1:
                        message = print(
                            "Sorry, Blank keyword is restricted !\n")
                        new_keyword = input(
                            "What word are you looking for? Type here correctly: ")

                    if new_keyword not in data.keys():
                        print(f"Searching the word '{new_keyword}' ....\n")
                        time.sleep(1.2)
                        print(f"\nOops! You entered the wrong word again!\n"
                              f"The word '{new_keyword}' is not found in this dictionary.\n")
                        close_words_new = get_close_matches(
                            f"{new_keyword}", keys, cutoff=0.6)
                        new_input = input(
                            f"\nDid you mean '{close_words_new[0]}' instead? ")

                        if new_input == "y" or new_input == "yes" or new_input == "yeah":
                            print(
                                f"Searching the word '{close_words_new[0]}'....\n")
                            time.sleep(1.2)
                            print(data[close_words_new[0]])
                            quit()

                        else:
                            print(
                                "\nSorry, can't fulfill your request at this moment")
                            quit()

                    meaning(new_keyword)
            except IndexError:
                pass
            except UnboundLocalError:
                pass
            except:
                print(
                    f"\nYou can search the word '{close_words_new[0]}' in web for more info")
    meaning(keyword)

    Continue = input("\n\nPress enter to continue and type 'exit' to quit: ")
