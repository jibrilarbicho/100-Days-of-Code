from traceback import print_tb


def formatName(fname, lname):
    f_name = fname.title()
    l_name = lname.title()
    return f"{f_name} {l_name}"


Name = formatName("jibril", "arbicho")
print(Name)
