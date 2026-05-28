def chk_lgl_age(x):
    if x >= 18:
        return "Good to Vote"
    else:
        return "Not legal age"


print(chk_lgl_age(98))