def index_words1(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result


def index_words2(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1


if __name__ == '__main__':
    hhh = 'Every dog has its day!'
    result = index_words1(hhh)
    print('result1', result)
    result = list(index_words2(hhh))
    print('result2:', result)
