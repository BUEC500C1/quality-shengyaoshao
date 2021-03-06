"""
print("enter the integer you want to convert to Roman Numeral")
int1 = input()
while (type(int1) != int):
    try:
        int1 = int(int1)
    except ValueError:
        print("input is not integer, please enter an integer")
        int1 = input()
"""
def convert(int1):
    if type(int1) != int:
        return 'The input must be an integer'
    if int1 > 3999 or int1 < 1:
        return 'Number must be an integer between 1 and 3999'
    res = ''
    romancollection = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    numbercollection = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    i = 0
    while(int1 > 0):
        if (int1 - numbercollection[i] >= 0):
            res = res + romancollection[i]
            int1 = int1 - numbercollection[i]
        else:
            i = i + 1
    return res
