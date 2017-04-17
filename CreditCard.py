#  File: CreditCard.py

#  Description: Checks if Creditcard number is valid

#  Student Name: Kevin Yee

#  Student UT EID: kjy252

#  Course Name: CS 303E

#  Unique Number:  51850

#  Date Created: 04/07/2017

#  Date Last Modified:

# This function checks if a credit card number is valid\
'''
Multiply all the odd digits d1, d3, … d15 by 2.
Sum the digits of each product.
Now add all the even digits d0, … d14 and the single digit products of the odd digits.
If the final sum is divisible by 10 then the credit card is valid, otherwise it is invalid.
'''
def is_valid (cc_num):
    list_of_odds =[]
    list_of_evens = []
    list_to_sum= [];
    length = len(str(cc_num));
    for i in range(0,length):
        if(i % 2 !=0):
            list_of_odds.append((cc_num%10)*2);
        else:
            list_of_evens.append((cc_num%10));
        cc_num =cc_num//10;
    for i in range(len(list_of_odds)):
        list_to_sum.append(list_of_odds[i]%10 + list_of_odds[i]//10);
    for i in range(len(list_of_evens)):
        list_to_sum.append(list_of_evens[i]%10);
    totalsum = sum(list_to_sum);
    if totalsum% 10 == 0:
        return True;
    else:
        return False;
    return False;
# This function returns the type of credit card
def cc_type (cc_num):
    if (cc_num[0] == '4'):
        return "Valid Visa credit card number"
    if (cc_num[0] == '5' and (int(cc_num[1]) - 5) <= 0):
        return "Valid MasterCard credit card number"
    if (cc_num == '6011' or cc_num[:3] == '644' or cc_num[:2] == '65'):
        return "Valid Discover credit card number"
    if (cc_num[:2] == '34' or cc_num[:2] == '37'):
        return "Valid American Express credit card number"
    return "Valid credit card number"
def  main ():
    cnumber = int(input("Enter 15 or 16-digit credit card number: "));
    if(len(str(cnumber)) < 15 or len(str(cnumber)) >16 or cnumber<0):
        print("Not a 15 or 16-digit number");
        return;
    if(is_valid(cnumber)):
        print(cc_type(str(cnumber)));
    else:
        print("Invalid credit card number");
main()
