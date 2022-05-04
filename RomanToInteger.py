
class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.nextval = None


class LinkedList:
    def __init__(self) -> None:
        self.root = None


class RomanToInteger:
    def __init__(self) -> None:
        self.numerals = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def convert(self, rString):
        if self.validateString(rString):
            romStr = rString[::-1]
            list = self.strToLinkedList(romStr)
        else:
            raise TypeError("Not a string")

        digit = total = count = int()

        char = list.root

        while char is not None:
            currentChar = None
            nextChar = None
            # Check if node exsists in numerals
            if (self.validateNumeral(char)):
                currentChar = self.numerals[char.val]
            else:
                raise ValueError("Not a valid roman numeral")
            # check if nextNode exists in numerals
            if char.nextval is not None:
                if (self.validateNumeral(char.nextval)):
                    nextChar = self.numerals[char.nextval.val]
                    # check if next character is equal current character, and there aren't 3 characters in a row
                    if nextChar == currentChar and count < 3:
                        count += 1
                        if count >= 3:
                            raise ValueError("Not a valid roman numeral")
                        digit += currentChar
                    #  check if next character is smaller then curret character
                    elif nextChar < currentChar:
                        if digit > 0:
                            raise ValueError("Not a valid roman numeral")
                        if currentChar / 10 == nextChar or currentChar / 5 == nextChar:
                            digit -= nextChar + nextChar
                            digit += currentChar
                        count = 0

                    # check if next character is bigger then current character It is the last numeral
                    elif nextChar > currentChar:
                        digit += currentChar
                        count = 0
                        if not currentChar * 5 == nextChar:
                            total += digit
                            digit = 0
                else:
                    raise ValueError("Not a valid roman numeral")
            # last character
            else:
                digit += currentChar
                total += digit
            char = char.nextval
        return total

    def validateString(self, value) -> bool:
        if isinstance(value, str):
            if len(value) <= 15 and len(value) > 0:
                return True
        return False

    def strToLinkedList(self, value) -> LinkedList:
        list = LinkedList()
        node = Node(value[0])
        nextNode = None
        list.root = node
        strLen = len(value)
        for i in range(strLen):
            if i + 1 < strLen:
                nextNode = Node(value[i + 1])
                node.nextval = nextNode
            else:
                nextNode = None
            node = nextNode
        return list

    def validateNumeral(self, char):
        return char.val in self.numerals.keys()

    def lastNumeral(self, digit, count, currentChar):
        if digit > 0 and count == 0:
            digit -= currentChar
        else:
            digit += currentChar

        return digit
