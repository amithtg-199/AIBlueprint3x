# num = "0123456789"
# garbled_text = input("Enter the garbled_text: ")
# clean_text = ""
# length_str = len(garbled_text)
# for i in garbled_text:
#     if i not in num:
#         clean_text += i
# print(clean_text)
def string_clean(s):
    """
    Function will return the cleaned string
    """
    num = "0123456789"
    clean_text = ""
    for i in s:
        if i not in num:
            clean_text += i
    return(clean_text)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet.index("z"))
