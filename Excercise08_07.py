'''Enter a string:
1-800-3569377
Enter a string:
18003569377
1-800-Flowers
1800flowers'''

numberValue = {"a":"2","b":"2","c":"2",
               "d":"3","e":"3","f":"3",
                "g":"4","h":"4","i":"4",
                "j":"5","k":"5","l":"5",
                "m":"6","n":"6","o":"6",
              "p":"7", "q":"7", "r":"7",
              "s": "7", "t": "8", "u":"8",
              "v":"8", "w":"9", "x": "9","y":"9","z":"9"}

def translated_number(num):
    translatednum = ""
    for i in range(len(num)):
        if(not num[i].isalpha()):
            translatednum += num[i];
        else:
            translatednum += numberValue[num[i]];
    return translatednum;

def main():
    phonenumber = str(input("Enter a phone number: "))
    print(translated_number(phonenumber.lower()))
if __name__ == "__main__":
        main()