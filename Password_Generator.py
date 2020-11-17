#Importing statement required.
import random

#Declaring list for character for password.
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   

lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                    'z'] 
uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                    'Z'] 

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
        '*', '(', ')'] 

#Declaring min lengt of password.
min_length = 8


def generate_password(password_length = min_length):
    
    # Make password have atleast one of each character
    one_digit = random.choice(digits)
    one_lowercase_char = random.choice(lowercase_chars)
    one_uppercase_char = random.choice(uppercase_chars)
    one_symbol = random.choice(symbols)

    # Making base passowrd with each character
    pseudo_password = one_digit + one_lowercase_char + one_uppercase_char + one_symbol

    combined_chars = digits + symbols + uppercase_chars + lowercase_chars

    # Adding remaining characters to password
    for _ in range(password_length - int(len(pseudo_password))):
        pseudo_password += random.choice(combined_chars)

    random.shuffle(list(pseudo_password))
    print(pseudo_password)

# Main function to call our generator function
if __name__ == "__main__":

    # Taking Length input.
    def getInput():
        print("Enter the length of password")
        input_length = input()

        # Testing input.
        if input_length != "default":
            if int(input_length) < 8:
                print("Password too short , minimum is 8 characters")
                getInput()
            else:
                generate_password(int(input_length))
        else:
            generate_password()
    getInput()
    
    

    