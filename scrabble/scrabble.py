import sys

## Importing the module where the score dictionsary is stored.
import score_word

## Reading the dicstionary and assign it to score_dict
score_dict = score_word.score_word()

## Reading sowpods.txt file to get the data of words
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

## Set the range of letters for users to enter
letter_range = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*", "?"]


## Checking if the first argument is placed or not
try:
    if len(sys.argv) == 1:
        raise Exception("Please enter 2-7 alphabets or wildcards(* or ?) in the 1st argument.")

    else:
        user_input = sys.argv[1].upper()

except Exception as error:
    print(error)
    sys.exit()


## Making further check on the user's entry
try:
    if False in [letter in letter_range for letter in user_input]:
        raise Exception("Please enter 2-7 alphabets or wildcards(* or ?) in the 1st argument.")

    elif len(user_input) not in range(2, 8):
        raise Exception("Please enter 2-7 letters in the 1st argument.")

    elif user_input.count("*") > 1 :
        raise Exception("You can use * maximum one time in the 1st argument.")
        
    elif user_input.count("?") > 1 :
        raise Exception("You can use ? maximum one time in the 1st argument.")
        
except Exception as error:
    print(error)
    sys.exit()


## Checking if the user placed 2nd and 3rd arguments or not
if len(sys.argv) == 4:
    want_to_specify = "yes"

else:
    want_to_specify = "no"


##############################################################################
### If the user entered 2nd and 3rd arguments, running the following codes ###
##############################################################################

if want_to_specify == "yes":

    ## Asking the user which letter to choose 
    try:
        user_letter_choice = sys.argv[2].upper()
        
        if user_letter_choice not in list(user_input):
            raise Exception("Please choose a letter from the letters you entered, and enter it in the 2nd argument.")
            
        elif user_letter_choice == "*" or user_letter_choice == "?":
            raise Exception("You can not choose wildcard in the 2nd argument.")
            
    except Exception as error:
        print(error)
        sys.exit()


    ## Asking the user where to place the letter 
    try:
        user_letter_location = sys.argv[3]
        
        if int(user_letter_location) < 0 or int(user_letter_location) >= len(user_input):
            raise Exception(f"Please enter a integer within the length of your input (from 0 to {len(user_input)-1}) in the 3rd argument")
                
    except Exception as error:
        print(error) 
        sys.exit()   


    ## Collecting words from "data" which meet the user's request 
    ## Store the words in the new list "data_new"

    data_new = []

    for word in data:
        list_word_letters = list(word)
        list_user_letters = list(user_input)
        
        ## Skipping the words whose length is longer that the length of letters which the user entered
        if len(list_word_letters) > len(list_user_letters):
            continue

        ## Skipping the words whose length is shorter than the location that user specified    
        elif  len(list_word_letters) < int(user_letter_location)+1 :
            continue
        
        ## if the word matches the user's request, store the word in data_new list
        elif list_word_letters[int(user_letter_location)] == user_letter_choice:
            data_new.append(word)


    ## Finding the words which meats the requirements
    ## Setting empty list of "matched_words" and "wildcard_score_list"
    matched_words = []
    wildcard_score_list = []

    ## Looping each word in data_new
    for word in data_new:
        
        ## Making list of letters for "word" and "user_input"
        ## Removing the letter which the user chose from each list
        list_word_letters_2 = list(word)
        list_word_letters_2.pop(int(user_letter_location))
        
        list_user_letters_2 = list(user_input)
        list_user_letters_2.remove(user_letter_choice)

        ## For each "word", checking if the letter exists in the letters which the user entered
        ## If the letter exists, storing the letter in stored_letters and removing it from list_user_letters 
        stored_letters = []
        wildcard_score = 0

        ## looping from the first letter to the location user specified
        for letter in list_word_letters_2[:int(user_letter_location)]:
            if letter in list_user_letters_2:
                list_user_letters_2.remove(letter)
                stored_letters.append(letter)

            elif '*' in list_user_letters_2:
                list_user_letters_2.remove('*')
                stored_letters.append(letter)
                wildcard_score += score_dict[letter.lower()]

            elif '?' in list_user_letters_2:
                list_user_letters_2.remove('?')
                stored_letters.append(letter)
                wildcard_score += score_dict[letter.lower()]
                
        ## storing the letter user specified        
        stored_letters.append(user_letter_choice)
        
        ## looping all after the location the user specified 
        for letter in list_word_letters_2[int(user_letter_location):]:
            if letter in list_user_letters_2:
                list_user_letters_2.remove(letter)
                stored_letters.append(letter)

            elif '*' in list_user_letters_2:
                list_user_letters_2.remove('*')
                stored_letters.append(letter)
                wildcard_score += score_dict[letter.lower()]

            elif '?' in list_user_letters_2:
                list_user_letters_2.remove('?')
                stored_letters.append(letter)
                wildcard_score += score_dict[letter.lower()]
        
        ## if the stored_letters matches list_word_letters, storing the word in matched_words, 
        ## and storing the score of wildcard in wildcard_score_list
        if stored_letters == list(word):
            matched_words.append(word)
            wildcard_score_list.append(wildcard_score)



####################################################################################
### If the user did not enter 2nd and 3rd arguments, running the following codes ###
####################################################################################

elif want_to_specify == "no":

    ## Finding the words which meats the requirements
    ## Setting empty list of "matched_words" and "wildcard_score_list" 
    matched_words = []
    wildcard_score_list = []

    ## Looping each word in data
    for word in data:
        ## Making list of letters for "word" and "user_input"
        list_word_letters = list(word)
        list_user_letters = list(user_input)
        
        ## Skipping the words whose length is longer that the length of letters which the user entered
        if len(list_word_letters) > len(list_user_letters):
            continue
        
        ## For each "word", checking if the letter exists in the letters which the user entered
        ## If the letter exists, storing the letter in stored_letters and removing it from list_user_letters 
        else:
            stored_letters = []
            wildcard_score = 0

            for letter in list_word_letters:
                if letter in list_user_letters:
                    list_user_letters.remove(letter)
                    stored_letters.append(letter)
                    
                elif '*' in list_user_letters:
                    list_user_letters.remove('*')
                    stored_letters.append(letter)
                    wildcard_score += score_dict[letter.lower()]
                    
                elif '?' in list_user_letters:
                    list_user_letters.remove('?')
                    stored_letters.append(letter)
                    wildcard_score += score_dict[letter.lower()]

            ## if the stored_letters matches list_word_letters, storing the word in matched_words, 
            ## and storing the score of wildcard in wildcard_score_list              
            if stored_letters == list_word_letters:
                matched_words.append(word)
                wildcard_score_list.append(wildcard_score)


############################################
### Common procedure for "Yes" and "No"  ###
############################################


## Conver the words in matched_words to lower case 
matched_words_lower = [word.lower() for word in matched_words]

## Making an empty list of score_list
score_list = []

## Looing each word in matched_words_lower to calculate the score
for word in matched_words_lower:
    word_score = 0
    for letter in word:
        word_score += score_dict[letter] 
    score_list.append(word_score)

## Removing the scores which came from the use of wildcard
score_list_wildcard_counted = [(score_list[n] - wildcard_score_list[n]) for n in range(len(score_list))]

## Zipping score_list_wildcard_counted and matched_words_lower
zipped_list = list(zip(score_list_wildcard_counted, matched_words_lower))

## Sorting the list based on the scores
zipped_list.sort(key = lambda t: t[0], reverse=True)

## Printing the result in accordance with the instruction/requirement
for n in range(len(zipped_list)):
    print("(" + str(zipped_list[n][0]) + ", " + str(zipped_list[n][1]) + ")")
    
print('Total number of words:', str(len(zipped_list)))