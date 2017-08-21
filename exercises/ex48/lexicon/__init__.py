directions = [
    'north',
    'south',
    'east',
    'west',
    'down',
    'up',
    'left',
    'right',
    'back'
]

verbs = [
    'go',
    'stop',
    'kill',
    'eat'
]

stops = [
    'the',
    'in',
    'of',
    'from',
    'at',
    'it'
]

nouns = [
    'door',
    'bear',
    'princess',
    'cabinet'
]

def scan(text):
    result = []
    for word in text.split():
        word = word.lower()
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        else:
            try:
                result.append(('number', int(word)))
            except ValueError:
                result.append(('error', word))

    return result
