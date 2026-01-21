# DO NOT modify code except "YOUR CODE GOES HERE" blocks

import collections
import argparse

from query import Query, QuerySyntaxError


class IRSystem:
    def __init__(self, f):
        # inverted index as discussed in class
        self.invertedIndex = collections.defaultdict(lambda: [])
        # set of documents to implement the NOT operator
        self.docs = set()

        for line in f:
            tokens = line.lower().split()
            doc_id = int(tokens[0])
            self.docs.add(doc_id)

            for token in set(tokens[1:]):
                if token != '-':
                    self.invertedIndex[token].append(doc_id)

        self.docs = sorted(self.docs)

    def q_term(self, term):
        return self.invertedIndex[term]

    def q_not(self, docs):
        results = [i for i in self.docs if i not in docs]
        return results

    @staticmethod
    def q_and(docs1, docs2):
        results = []
        # YOUR CODE GOES HERE
        #   Implement an AND between docs1 and docs2

        return results

    @staticmethod
    def q_or(docs1, docs2):
        results = []
        # YOUR CODE GOES HERE
        #   Implement an OR between docs1 and docs2

        return results

    def run_query(self, query):
        # Tokens are reversed to facilitate running arbitrary boolean queries (see below)
        tokens = reversed(list(Query.tokenize(query)))
        tokens = [token.lower() if token not in ["NOT", "AND", "OR"] else token for token in tokens]

        results = []
        if len(tokens) == 1:
            assert tokens[0] not in ["NOT", "AND", "or"], "Invalid query"
            results = self.q_term(tokens[0])
        elif len(tokens) == 2:
            assert tokens[1] == "NOT", "Unary operator is not NOT"
            results = self.q_not(self.q_term(tokens[0]))
        elif len(tokens) == 3:
            if tokens[2] == "AND":
                results = self.q_and(self.q_term(tokens[0]), self.q_term(tokens[1]))
            elif tokens[2] == "OR":
                results = self.q_or(self.q_term(tokens[0]), self.q_term(tokens[1]))
            else:
                assert False, "Binary operator is neither AND nor NOT"

        # YOUR CODE GOES HERE - GRADUATE STUDENTS ONLY
        #   Substitute the code above to run arbitrary boolean queries
        #   You will need a stack (and lots of care)

        return results


def main(corpus):
    ir = IRSystem(open(corpus))

    while True:
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to file with the corpus")
    args = parser.parse_args()
    main(args.CORPUS)
