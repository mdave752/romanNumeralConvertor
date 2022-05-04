
class IntegerToRoman:
    numerals = {1: 'I', 5: 'V', 10: 'X',
                50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    def convert(self, num):
        if not isinstance(num, int):
            raise TypeError("Not a integer")
        if num % 1 != 0.0:
            raise ValueError("Floats are not allowed")
        if num < 0 or num > 3999:
            raise ValueError("value is not in range 0 - 3999")
        res, j = str(), 1
        for x in str(num):
            x = int(x)
            i = 10 ** (len(str(num)) - j)
            if x*i in self.numerals.keys():
                res += self.numerals[x*i]
            elif x == 4:
                res += self.numerals[i] + self.numerals[i*5]
            elif x == 9:
                res += self.numerals[i] + self.numerals[i*10]
            elif x < 4:
                res += (self.numerals[i] * x)
            elif x > 5:
                res += self.numerals[i*5] + (self.numerals[i] * (x-5))
            j += 1
        return res
