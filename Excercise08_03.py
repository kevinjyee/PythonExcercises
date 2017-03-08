'''Check password) Some Web sites impose certain rules for passwords. Write a
function that checks whether a string is a valid password. Suppose the password
rules are as follows:
■ A password must have at least eight characters.
■ A password must consist of only letters and digits.
■ A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays
valid
password
if the rules are followed or invalid password otherwise.'''

def check_valid(num):
    count =0;
    if(len(num) < 8 or not num.isalnum()):
        return "Invalid"
    for i in range(len(num)):
        if(num[i].isdigit()):
            count +=1;

    if(count < 2):
        return "Invalid"
    return "Valid"
def main():
    number = str(input("Enter a password"))
    print (check_valid(number));

if __name__ == "__main__":
        main()