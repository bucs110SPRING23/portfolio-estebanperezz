# # def bar(param1=4,param2=3):
# #     return param1 + param2
# # result = bar(10,20)
# # print(result)
# def percentage_to_letter(percent):
#     """This is a function that returns a letter grade based on  %
#     args: percent(int)
#     return:letter(str) """ ## Doc Strings 
#     let = "A"
#     if percent < 90:
#         let = "B"
#     elif percent < 80:
#         let = "C"
#     elif percent < 70:
#         let = "D"
#     else:
#         let = "F"

#     pass
# def is_passing(letter): ## Boolean functions, is_* convention 
#     return letter.lower() in "abc"
# def main():
#     letter = percentage_to_letter(90)
#     if is_passing(letter):
#         print("You passed")
#     else:
#         print("Someone messed up")
# # for - programming pattern
# ##accumaltor 
# result = 0
# for i in range(10):
#     result = result + i 
# print(result)
def remove_vowels(string):
    vowels = "aeiou"
    vowels.upper()
    result = ""
    for ch in string:
        if ch not in vowels:
            result+=ch 
    return result 
def main():
    myString ="Hello World"
    print(remove_vowels(myString))
    print(myString)
main() 

def multiplytwo(x,y):
    for _ in range(0,y):
        x = x+x
    pass
def raisedto(exponent):
    
    pass
def sqaure(parameter):
    pass
def main():
    pass
