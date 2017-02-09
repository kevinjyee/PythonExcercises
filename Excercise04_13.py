


def getTax(income, status):



    moneybracket = [
        [8350, 33950, 82250, 171550, 372950],
        [16700, 67900, 137050, 208850, 372950],
        [8350, 33950, 68525, 104425, 186475],
        [11950, 45500, 117450, 190200, 372950]
        ]

    if income <= moneybracket[status][0]:
        tax = income * 0.10
    elif income <= moneybracket[status][1]:
        tax = moneybracket[status][0] * 0.10 + (income - moneybracket[status][0]) * 0.15
    elif income <= moneybracket[status][2]:
        tax = moneybracket[status][0] * 0.10 + (moneybracket[status][1] - moneybracket[status][0]) * 0.15 + \
        (income - moneybracket[status][1]) * 0.25
    elif income <= moneybracket[status][3]:
        tax = moneybracket[status][0] * 0.10 + (moneybracket[status][1] - moneybracket[status][0]) * 0.15 + \
        (moneybracket[status][2] - moneybracket[status][1]) * 0.25 + (income - moneybracket[status][2]) * 0.28
    elif income <= moneybracket[status][4]:
        tax = moneybracket[status][0] * 0.10 + (moneybracket[status][1] - moneybracket[status][0]) * 0.15 + \
        (moneybracket[status][2] - moneybracket[status][1]) * 0.25 + (moneybracket[status][3] - moneybracket[status][2]) * 0.28 + \
        (income - moneybracket[status][3]) * 0.33
    else:
        tax = moneybracket[status][0] * 0.10 + (moneybracket[status][1] - moneybracket[status][0]) * 0.15 + \
        (moneybracket[status][2] - moneybracket[status][1]) * 0.25 + (moneybracket[status][3] - moneybracket[status][2]) * 0.28 + \
        (moneybracket[status][4] - moneybracket[status][3]) * 0.33 + (income - moneybracket[status][4]) * .35

    return tax






# Prompt the user to enter filing status
status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

# Prompt the user to enter taxable income
income = eval(input("Enter the taxable income: "))

# Compute tax
tax = 0

if status == 0:
    tax = getTax(income, status)

elif status == 1:  # Compute tax for married file jointly
    tax = getTax(income, status)
elif status == 2:  # Compute tax for married separately
    tax = getTax(income, status)
elif status == 3:  # Compute tax for head of household
    tax = getTax(income, status)
else:
    print("Error: invalid status")
    sys.exit()


# Display the result
print("Tax is", format(tax, ".2f"))