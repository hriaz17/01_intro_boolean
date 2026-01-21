# DO NOT modify code except "YOUR CODE GOES HERE" blocks

class QuerySyntaxError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'Syntax Error: %s' % self.message


class Query:
    @staticmethod
    def tokenize(string):
        k = 0
        i = 0

        while i < len(string):
            if string[i].isspace() or string[i] == '"':
                substring = string[k:i]
                if substring:
                    yield substring
                k = i + 1

                if string[i] == '"':
                    j = string[i + 1:].find('"')
                    if j < 0:
                        raise QuerySyntaxError('Mismatched " (double quote) at %i' % i)
                    j += i + 1
                    substring = string[i + 1:j]
                    if substring:
                        yield substring.split()
                    k = j + 2
                    i = j + 1
            i += 1

        substring = string[k:]
        if substring:
            yield substring
