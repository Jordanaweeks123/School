#  File: TestCipher.py

#  Description: This assignment has two coded examples of ciphers, a
#  transposition cipher (rail fence) and a substitution cipher (vigenere)

#  Student's Name: Jordan Weeks

#  Student's UT EID: jaw6235

#  Partner's Name: Rakim Hirji

#  Partner's UT EID: rah4387

#  Course Name: CS 313E 

#  Unique Number: 50295

#  Date Created: February 6th, 2020

#  Date Last Modified: February 7th, 2020

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    position = 0 #This gives the row of the character
    rows = [] #Creates an empty list
    answer = "" #Creates an empty string
    direction = 1 #Controls whether diagonal is moving up or down

    for i in range(key): #Since key is an integer, do not need len()
        rows.append("") #Adds blank spaces
    #strng1 = list(strng)
    for element in strng: #loops through each element of the string
        rows[position] += element #Appends element of strng to the list rows
        position += direction
        if position == (key - 1) or position == 0:
            direction *= (-1) #Changes direction (-1 means up, 1 means down)

    for element in rows: #Loops through every element in rows list
        answer += element #Adds the characters to the empty string
    return answer	# placeholder for the actual return statement

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    position = 0
    rows = []
    answer = ""
    direction = 1
    string_len = len(strng)

    for i in range(key):
        rows.append("")

    for element in strng:
        rows[position] += " " #Adds a blank space to list (same as num of characters in each row)
        position += direction
        if position == (key - 1) or position == 0:
            direction *= (-1) #Same as above
    #This will fill all the empty rows with their corresponding charcters
    for i in range(len(rows)):
        char_ind = len(rows[i]) #Gives how many elements are in ith sub element
        rows[i] = strng[0:char_ind]
        strng = strng[char_ind:] #Goes until end

    #default direction and position once more
    direction = 1
    position = 0
    for j in range(string_len):
        answer = answer + rows[position][0]
        rows[position] = rows[position][1:]
        position = position + direction
        if position == (key - 1) or position == 0:
            direction *= (-1) #Same as above
    
    return answer	# placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    strng = strng.lower() #Converts to lower case
    string = "" #empty string
    for element in strng: #Ensures only letters remain
        x = element.isalpha()
        if x == True:
            string += element
    
    return string	# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list
#Shall make use of ord() function here
#ord() returns an integer representing the Unicode character
def encode_character (p, s):
    #As mentioned in lecture we shall convert the top row of letters to nums
    #Set equal to 1 less than expected, then use mod 26
    p_num = ord(p) - ord('a')
    s_num = ord(s) - ord('a')
    new_num = (s_num + p_num) % 26 + ord('a') #This is increased
    x = chr(new_num) #chr does the opposite of ord (goes backwards)
    return x	# placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    #Same code as encode, save for the minus sign in new_num and the addition
    #of 26
    p_num = ord(p) - ord('a')
    s_num = ord(s) - ord('a')
    new_num = (s_num - p_num) % 26 + ord('a') #This is decreased
    if new_num < ord('a'):
        new_num += 26 #Adds 26 if its value is below ord(a)
    x = chr(new_num) #chr does the opposite of or (goes backwards)
    return x	# placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
#Shall first filter strng and phrase by using the function written above
    string = filter_string(strng)
    phrase = filter_string(phrase)
    string1 = ""
    '''
    for i in range(len(strng)):
        for j in range(len(phrase)):
            if i == j:#if indices match
                p_num = ord(p) - ord('a')
                s_num = ord(s) - ord('a')
                new_num = (s_num + p_num) % 26 + ord('a')
                string1 = string1 + chr((s_num + p_num) % 26 + ord('a'))
    '''
    for i in range(len(string)):
        string1 = string1 + encode_character(phrase[i % len(phrase)], strng[i])
    return string1	# placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    strng = filter_string(strng)
    phrase = filter_string(phrase)
    string1 = ""
    for i in range(len(strng)):
        string1 = string1 + decode_character(phrase[i%len(phrase)], strng[i])
    return string1	# placeholder for the actual return statement

def main():
    print("Rail Fence Cipher")
  # prompt the user to enter plain text
    strng = input("Enter Plain Text to be Encoded: ")
  # prompt the user to enter the key
    key = eval(input("Enter Key: "))
  # encrypt and print the plain text using rail fence cipher
    z = ("Encoded Text: ") + str(rail_fence_encode(strng, key))
    print(z)
  # prompt the user to enter encoded text
    strng = input("Enter Encoded Text to be Decoded: ")
  # prompt the user to enter the key
    key = eval(input("Enter Key: "))
  # decrypt and print the encoded text using rail fence cipher
    z = ("Decoded Plain Text: ") + str(rail_fence_decode(strng, key))
    print(z)
    
    print("Vigenere Cipher")
  # prompt the user to enter plain text
    strng = input("Enter Plain Text to be Encoded: ")

  # prompt the user to enter pass phrase
    phrase = input("Enter Pass Phrase (no spaces allowed): ")

  # encrypt and print the plain text using Vigenere cipher
    z = ("Encoded Text: ") + str(vigenere_encode ( strng, phrase ))
    print(z)
  # prompt the user to enter encoded text
    strng = input("Enter Encoded Text to be Decoded: ")

  # prompt the user to enter pass phrase
    phrase = input("Enter Pass Phrase (no spaces allowed): ")

  # decrypt and print the encoded text using Vigenere cipher
    z = ("Decoded Plain Text: ") + str(vigenere_decode(strng, phrase))
    print(z)

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
