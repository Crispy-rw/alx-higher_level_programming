def no_c(my_string):
    arr = [chr for chr in my_string if chr not in "cC"]
    return "".join(arr)
