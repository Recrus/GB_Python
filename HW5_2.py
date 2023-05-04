def RLE(s):
    if not s.isalpha():
        raise ValueError("Извините, но строка должна включать только буквы")
    if not s:
        return ""

    result = ""
    current_char = s[0]
    current_count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            current_count += 1
        else:
            result += current_char + str(current_count) if current_count > 1 else current_char
            current_char = s[i]
            current_count = 1

    result += current_char + str(current_count) if current_count > 1 else current_char

    return result


s1 = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB"
print(RLE(s1))  # результат: "A4B3C2XYZD4E3F3A6B4"

s2 = "BBBBBBBBBBBBBBBBBBBBBBBB"
print(RLE(s2))  # результат: "B24"

s3 = "123ABC"
print(RLE(s3))  # результат: ValueError: Извините, но строка должна включать только буквы

s4 = ""
print(RLE(s4))  # результат: ""
