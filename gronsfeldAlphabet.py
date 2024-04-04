
# #GRONSFELD CYPHER
# #Starts with the alphabet ABCDEFGHIJKLMNOPQRSTUVWXYZ
# #We will use a numeric key, and each digit of the numeric key will represent how many spaces on the alphabet we are going to shift a specific letter, repeating the alphabet if necessary

# #   ABCDEFGHIJKLMNOPQRSTUVWXYZ
# # 0 ABCDEFGHI...XYZ
# # 1 BCDEFGHI...XYZA
# # 2 CDEFGHI...XYZAB
# # 3 DEFGHI...XYZABC
# # .
# # .
# # .

# #Alphabet_length = 26


# #For example, if we have the message ACE, for the key 123
# # A : 1 = 1(position of A in the alphabet) - 26(length of alphabet) + 1(number of positions shifted) = 2
# # let's say we have an array of numbers for our key: key = [1,2,3]
# # This array's length is 3

# # We also have an array of characters: str = ['h','o','l','a',]

# # We need to assign a key value to each character of str, repeating the key as needed
# # H O L A
# # 1 2 3 1

# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
# 1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

# encoded_str = []

# #ord(char) returns the ascii number of the given character
# #chr(ascii_number) returns the character of the given ascii number



# print(0 % 3)
# print(1 % 3)
# print(2 % 3)
# print(3 % 3)
# print(4 % 3)
# print(5 % 3)
# print(6 % 3)
# print(7 % 3)

# #key_pos = str_pos % key_length'

# key[key_pos]

# ascii_num = ord(str_pos)

# res_ascii = ascii_num - 64 + key[key_pos]

import re 
def gronsfeld_cypher(text, key):

  if (not key.isdigit()): #if the given key is not a digit, return
    print('Entered key is not only numeric')
    return 1
    
  uppercase_text = text.upper() #convert the given text to uppercase
  no_space_text = uppercase_text.replace(' ','') #and remove all blank spaces

  if (not re.match(r"^[A-Z]+$", no_space_text)): #if the given text doesn't contain latin alphabet letters only, return
    print('Text to encode doesn\'t only contain latin alphabet letters')
    return 2
  
  if (len(key) > len(no_space_text)): #if the given key is longer than the given text, return
    print("The given key is longer than the given text")
    return 3

  key_list = [] #lists
  text_list = []
  encrypted_list = []
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  for char in no_space_text: #populating text_list
    text_list.append(char)

  for char in key: #populating key_list
    key_list.append(int(char))

  for i in range(0,len(text_list)): #iterate as many times as elements in text_list

    # key index for this given position in encrypted_list will be the
    # module between the current string position and the key length
    key_index = i % len(key_list)
    
    current_letter_index = alphabet.index(text_list[i]) #ascii for the current letter in text_list

    current_key = key_list[key_index] #number for the found key index
    resulting_letter_pos = current_letter_index + current_key

    if(resulting_letter_pos > 25): 
      resulting_letter_pos = resulting_letter_pos - 26

    resulting_letter = alphabet[resulting_letter_pos]

    encrypted_list.append(resulting_letter)
  converted_list = map(str, encrypted_list)
  result = ''.join(converted_list)
  print(result)

def gronsfeld_decypher(text, key):

  if (not key.isdigit()): #if the given key is not a digit, return
    print('Entered key is not only numeric')
    return 1
    
  uppercase_text = text.upper() #convert the given text to uppercase
  no_space_text = uppercase_text.replace(' ','') #and remove all blank spaces

  if (not re.match(r"^[A-Z]+$", no_space_text)): #if the given text doesn't contain latin alphabet letters only, return
    print('Text to decode doesn\'t only contain latin alphabet letters')
    return 2
  
  if (len(key) > len(no_space_text)): #if the given key is longer than the given text, return
    print("The given key is longer than the given text")
    return 3

  key_list = [] #lists
  text_list = []
  decrypted_list = []
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

  for char in no_space_text: #populating text_list
    text_list.append(char)

  for char in key: #populating key_list
    key_list.append(int(char))

  for i in range(0,len(text_list)): #iterate as many times as elements in text_list

    # key index for this given position in encrypted_list will be the
    # module between the current string position and the key length
    key_index = i % len(key_list)
    
    current_letter_index = alphabet.index(text_list[i]) #ascii for the current letter in text_list

    current_key = key_list[key_index] #number for the found key index
    resulting_letter_pos = current_letter_index - current_key

    if(resulting_letter_pos < 0): 
      resulting_letter_pos = resulting_letter_pos + 26

    resulting_letter = alphabet[resulting_letter_pos]

    decrypted_list.append(resulting_letter)
  
  
  converted_list = map(str, decrypted_list)
  result = ''.join(converted_list)
  print(result)


gronsfeld_cypher("HOLA", "123")
gronsfeld_cypher("ABCDEFGHIJKLMNOPQRSTUVWXYZ","9")
gronsfeld_cypher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1")
gronsfeld_cypher("ABCDEFGHIJKLMNOPQRSTUVWXYZ","0")
gronsfeld_cypher("ABCDEFGHIJKLMNOPQRSTUVWXYZ","5")

gronsfeld_decypher("JKLMNOPQRSTUVWXYZABCDEFGHI","9")
gronsfeld_decypher("BCDEFGHIJKLMNOPQRSTUVWXYZA","1")
gronsfeld_decypher("ABCDEFGHIJKLMNOPQRSTUVWXYZ","0")
gronsfeld_decypher("FGHIJKLMNOPQRSTUVWXYZABCDE","5")




