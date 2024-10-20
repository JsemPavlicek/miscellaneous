def na_druhou_text(num):
    string_number = ""
    for one in str(num):
        string_number += str(int(one) **2)
    return string_number


result = na_druhou_text(965)
print(result)

