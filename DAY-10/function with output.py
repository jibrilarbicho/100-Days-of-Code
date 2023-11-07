from traceback import print_tb


def formatName(fname, lname):
    if fname == "" or lname == "":
        return "You did not enter First Name or Last Name"
    f_name = fname.title()
    l_name = lname.title()
    return f"{f_name} {l_name}"


Name = formatName(input("What is your first Name\n"), input("what is your Last name\n"))
print(Name)
