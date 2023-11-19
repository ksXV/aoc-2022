def checkForSignal(charToInsert: str, chars: list):
    amountOfCharsRead = {}
    for char in chars:
        if amountOfCharsRead.get(char):
            amountOfCharsRead[char] += 1
        else:
            amountOfCharsRead[char] = 1
    for char in amountOfCharsRead.values():
        if char > 1:
            chars.pop(0)
            chars.append(charToInsert)
            return False
    return True


with open("input.txt", "r+") as f:
    chars = []
    readChars = f.read(14)
    readBytes = 14
    for char in readChars:
        chars.append(char)
    while True:
        readChar = f.read(1)
        readBytes += 1
        if checkForSignal(readChar, chars):
            print(readBytes - 1)
            break
