# wap to get new string from a given string where "is" has been added to
# the front. if the given string already begins with "is" then return the 
# string unchanged


def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

print(new_string("IsArray"))

