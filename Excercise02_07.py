
def main():
    minutes = int(eval(input("Enter the number of minutes: ")))
    years = minutes / 60 / 24 // 365
    days = int(minutes / 60 / 24 % 365)
    print(minutes,"minutes is approximately",years,"years and",days);
if __name__ == '__main__':
    main()

