# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name("AMiTh", "hathwar"))

def format1(text):
    return text + text

def format2(text):
    return text.title()

output = format2(format1("hello"))
print(output)