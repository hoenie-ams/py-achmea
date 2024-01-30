

def fahr_to_celcius(x):
    result = 5 * (x - 32) / 9
    return result


def celcius_to_fahr(x):
    result = (x * 9 / 5) + 32
    return result


def convert_temperature(s):
    temp = int(s[:-1])
    if "C" in s:
        return celcius_to_fahr(temp)
    else:
        return fahr_to_celcius(temp)


print(convert_temperature("100F"))
print(convert_temperature("38C"))
