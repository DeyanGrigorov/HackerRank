def timeConversion(s):
    time = s[-2:]
    if time == 'PM':
        new_str = s[:2]
        new_str = int(new_str)

        if new_str == 12:
            new_str = '12'
            return new_str + s[2:-2]
        new_str += 12
        if new_str == 24:
            new_str = '00'
            s = new_str + s[2:]
        else:
            new_str = str(new_str)
            s = new_str + s[2:]
        return s[:-2]

    else:
        new_str = int(s[:2])
        if new_str == 12:
            new_str = '00'
            return new_str + s[2:-2]
        return s[:-2]





if __name__ == '__main__':
    s = input()

    result = print(timeConversion(s))


