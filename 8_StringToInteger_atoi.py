import time

class Solution:

    def myAtoi(self, s: str) -> int:
        number = 0
        is_negative = False
        first = True
        for digit in s:
            if digit == " ":
                continue
            if first:
                first = False
                if digit == "+":
                    continue
                if digit == "-":
                    is_negative = True
                    continue

            # stop processing if hit a non digit text
            if digit not in "0123456789":
                break
            number = number * 10 + int(digit)

            # I can clamp the result easily because python store numbers than int32_max*10
            if number > 2**31 - 1 and not is_negative:
                return 2**31 - 1
            if number > 2**31 and is_negative:
                return -(2**31)

        if is_negative:
            number = -number
        return number


def validate(s, exp):
    start = time.time()
    result = (Solution()).myAtoi(s)

    if result != exp:
        print(s, exp, result)
    print("--T: {:.2f}".format(time.time() - start))


validate("42", 42)
validate("-042", -42)
validate("1337c0d3", 1337)
validate("+-12", 0)
validate("0-1", 0)
validate("words and 987", 0)
validate("-2147483647", -2147483647)
validate("-2147483648", -2147483648)
validate("-2147483649", -2147483648)
validate("2147483647", 2147483647)
validate("2147483648", 2147483647)
