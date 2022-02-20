import random

def main():
    
    #prompts the user to specify a path and then opens that file
    file = open_file()
    #if the specified file can not be found
    if file == False: return
    
    #process the file
    words = file_processing(file)
    #if the file contains non-ascii characters then we exit
    if words == False: return

    top_10_most_used_words = find_most_important_words(words)

    top_3_combinations_for_first_2_letters = find_top_combinations_for_first_2_letters(words)

    top_3_combinations_for_first_3_letters = find_top_combinations_for_first_3_letters(words)

    #program exits
    print("Terminating Program")
    input("press any key to continue...")
    return


#reads the file with the ASCII characters
def open_file():
    #get users input about the file's path
    path=input("please enter the path of the file or enter the name of the file if it is in the same directory \n")

    #add .txt in the end if the user has not specified it
    if path.endswith(".txt") == False:
        path = path + ".txt"

    try:
        file = open(path,"r")
        return file
    #if the path does not exist prompt the user and terminate the program
    except:
        print("specified file does not exist/incorrect path \n")
        print("program terminating")
        input("press any key to continue...")
        return False

#makes the neccessary processing and returns the given text
def file_processing(file):
    text=file.read()
    #check if the file contains non-ascii characters and exits if it fails
    if text.isascii() == False:
        print("the text file contains non ascii characters \n")
        print("program terminating")
        input("press any key to continue...")
        return False
    
    #removes all numbers
    text = ''.join([letter for letter in text if not letter.isdigit()])
    
    #removes unwanted ascii characters
    list_of_characters = ["{","|","}","~","_","^","`","@","?",">","=","<",";",":","/",".","-",",","+","*",")","(","&","%","\\"]
    for character in list_of_characters:
        text= text.replace(character,'')

    #makes all the text lowercase
    text = text.lower()

    #split words based on space
    words = text.split(" ")

    new_words = []
    #removes empty characters 
    #NOTE I am sorry for the implementation, but I was running out of time
    for word in words:
        if word != '':
            new_words.append(word)
    
    #NOTE print(new_words) for checking
    
    file.close()
    return new_words 

#it finds the most important words
def find_most_important_words(words):
    
    top_ten_words = helper_function_for_sorting_and_creating_dictionaries(words)

    #TODO if there are multiple numbers that are in the tenth spot find them and randomize which one will be returned

    top_ten_words = top_ten_words[:10]
    print(top_ten_words)
    return top_ten_words

#finds the combination of the 2 first letters that appear at most in the given words
def  find_top_combinations_for_first_2_letters(words):
    first_2_letters = []
    #get the first 2 letters from each word
    for word in words:
        #the exercise does not specify it, so I decided to skip word, whose size is less than 2
        if len(word) < 2:
            continue
        first_2_letters.append(word[:2])
        #print(first_2_letters) #NOTE for checking
    
    top_3_combinations = helper_function_for_sorting_and_creating_dictionaries(first_2_letters)

    #get the first 2 letters that appear the most in the given words
    top_3_combinations = top_3_combinations[:3]
    print(top_3_combinations)

    return top_3_combinations

def find_top_combinations_for_first_3_letters(words):
    first_3_letters = []
    #get the first 3 letters from each word
    for word in words:
        #the exercise does not specify it, so I decided to skip word, whose size is less than 3
        if len(word) < 3:
            continue
        first_3_letters.append(word[:3])
        #print(first_3_letters) #NOTE for checking
    
    top_3_combinations = helper_function_for_sorting_and_creating_dictionaries(first_3_letters)

    #get the first 3 letters that appear the most in the given words
    top_3_combinations = top_3_combinations[:3]
    print(top_3_combinations)

    return top_3_combinations

def helper_function_for_sorting_and_creating_dictionaries(items):
    occurances = dict()
    for item in items:
        #if it exists in the dictionary it adds one
        if item in occurances:
            occurances[item] += 1
        #if it does not it instantiates it at one
        else:
            occurances[item] = 1

    top_occurances = []
    #return back to list to sort the items
    for key, value in occurances.items():
        temp = [value,key]
        top_occurances.append(temp)
    
    #sort the 2 dimensional list and return it
    top_occurances.sort(reverse=True)
    return top_occurances
    

#program's entry poiny
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
