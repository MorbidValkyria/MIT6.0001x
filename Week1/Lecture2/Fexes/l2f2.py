def to_nato(words):
    nato = {
        "a": "Alfa",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliett",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu"
    }
    if len(words) < 1:
        return ''
    new = ''
    words = words.lower()
    for i in range(len(words)):
        if words[i] != ' ':
            new += nato[words[i]]

            if i != len(words) - 1:
                new += ' '

    return new


print(to_nato('Did not see that coming'))
