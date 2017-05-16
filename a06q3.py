import check
import math

## Some useful message constants.
verification_message = "Exact: {0}, Other: {1}"
incorrect_message = "Your guess contains an incorrect number of characters."
keyword_message = "The keyword has {0} characters."
congratulations_message = "Congratulations! "
correct_keyword_message = "The correct keyword was {0}."
guess_message = "Please enter a guess: "

# number_exact(keyword,message) proudces the number of characters in message 
# that have the exact same value and in the same position.
# number_exact: Str Str -> Nat
def number_exact(keyword, message):
    pos = 0
    m = 0
    while pos < len(keyword):
        if keyword[pos] == message[pos]:
            pos = pos + 1
            m = m + 1
        else:
            pos = pos + 1
    return m

# updated_str(keyword, message) proudces a new string like keyword, but is
# without the characters that are the same to the one in message that is at the
# same position.
# updated_str: Str Str -> Str
def updated_str(keyword, message):
    string = ""
    for x in range(0,len(keyword)):
        if keyword[x] != message[x]:
            string = string + keyword[x]
        else:
            string = string
    return string 

# number_other(keyword, message) produces the number of characters that are both
# in keyword and message, but are not in the same position.
def number_other(keyword,message):
    message_str = updated_str(message,keyword)
    keyword_str = updated_str(keyword,message)
    num_other = 0
    for x in message_str:
        num_other = num_other + min(message_str.count(x), keyword_str.count(x))
        message_str = message_str.replace(x,"")
        keyword_str = keyword_str.replace(x,"")
    return num_other


# verbal_mastermind(keyword) informs the user how many characters are in the 
# keyword and prompts the user for input until the user guesses the keyword or 
# quits.
# Effects: Prints the length of the keyword and prints out messages to inform
# users it their guesses are correct or not.
# verbal_mastermind: Str -> None
# Examples:
# Calling verbal_mastermind("answers") will print "The keyword has 6 characters.
# " and input "bananas" will print "Exact: 1, Other: 2"
# Calling verbal_mastermind("failed") will print "The keyword has 6 characters."
# and input "!quit" will print "The correct keyword was failed."

def verbal_mastermind(keyword):
    print(keyword_message.format(len(keyword)))
    message = input(guess_message)
    while (message != keyword) and (message != "!quit"):
            if len(keyword) != len(message):
                print(incorrect_message)
                print(keyword_message.format(len(keyword)))
                message = input(guess_message)
            elif len(keyword) == len(message):
                print (verification_message.format(number_exact\
                                                   (keyword,message),\
                                                   number_other\
                                                   (keyword,message)))
                message = input(guess_message)
    if message == keyword:
        print (congratulations_message,correct_keyword_message.format(keyword)\
              ,sep = "")
    elif message == "!quit":
                print (correct_keyword_message.format(keyword))
# Test 1:
check.set_input(["bananas", "aaaaaaa","andoras","peelers","startle","answers"])
check.set_screen(
"The keyword has 7 characters."
     "Please enter a guess: bananas"
     "Exact: 1, Other: 2"
     "Please enter a guess: aaaaaaa"
     "Exact: 1, Other: 0"
     "Please enter a guess: andoras"
     "Exact: 3, Other: 1"
     "Please enter a guess: peelers"
     "Exact: 3, Other: 0"
     "Please enter a guess: startle"
     "Exact: 0, Other: 4"
     "Please enter a guess: answers"
     "Congratulations! The correct keyword was answers.")
check.expect("Q3T1",verbal_mastermind("answers"), None)

# Test 2:
check.set_input(["money"])
check.set_screen(
"The keyword has 5 characters."
"Please enter a guess: money"
"Congratulations! The correct keyword was money.")
check.expect("Q3T2",verbal_mastermind("money"), None)

# Test 3:
check.set_input(["banana","toomanycharacters","!quit"])
check.set_screen(
"The keyword has 6 characters."
"Please enter a guess: banana"
"Exact: 1, Other: 0"
"Please enter a guess: toomanycharacters"
"Your guess contains an incorrect number of characters."
"The keyword has 6 characters."
"Please enter a guess: !quit"
"The correct keyword was failed.")
check.expect("Q3T3", verbal_mastermind("failed"),None)

# Test 4: Empty string
check.set_input([""])
check.set_screen(
"The keyword has 0 characters."
'Please enter a guess: ""'
"Congratulations!")
check.expect("Q3T4",verbal_mastermind(""), None)
        
            
        
