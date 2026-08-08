def my_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Formated name is {formated_f_name} {formated_l_name}"

print(my_name(f_name=input("what is your first name?"), l_name=input("what is your last name?")))