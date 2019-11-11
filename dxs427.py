############################################################
# CMPSC 442: Homework 5
############################################################

student_name = "Dmytro Suprun"

############################################################
# Imports
############################################################
import string
import re
import random
import math


############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    tokens = re.findall(r"[{}]|[\w]+".format(string.punctuation), text)
    return tokens

def ngrams(n, tokens):
    n_gr = [(tuple(['<START>' if index - n +i < 0 \
                    else tokens[index - n + i] for i in range(1, n)]), (word))\
                        for index, word in enumerate(tokens)]
    index = len(tokens)
    n_gr.append( (tuple(['<START>' if index - n + i < 0 \
                    else tokens[index - n + i] for i in range(1, n)]), '<END>'))
    return n_gr

class NgramModel(object):

    def __init__(self, n):
        self.order_n = n
        self.probabilities = dict()

    # TODO speedup this function
    def update(self, sentence):
        new_input = ngrams(self.order_n, tokenize(sentence))
        for context, token in new_input:
            if context in self.probabilities:
                if token in self.probabilities[context]:
                    self.probabilities[context][token] += 1
                else:
                    new_token = {token: 1}
                    self.probabilities[context].update(new_token)
            else:
                self.probabilities.update({context:{token: 1}})

    def prob(self, context, token):
        probability = 0
        count = 0
        if context in self.probabilities:
            if token in self.probabilities[context]:
                for a_token in self.probabilities[context]:
                    count += self.probabilities[context][a_token]
                probability =  self.probabilities[context][token]/count
        # if it's not in the dictionary, returns 0
        return probability

    # TODO save tokens in the sorted order to avoid sorting extra time
    def random_token(self, context):
        cumulative = 0
        r = random.random()
        for token in sorted(self.probabilities[context]):
            summ = cumulative + self.prob(context, token)
            if summ > r:
                return token
            else:
                cumulative = summ

    def random_text(self, token_count):
        starting_context = ['<START>' for _ in range(self.order_n-1)]
        context = starting_context.copy()
        result = list()
        for i in range(token_count):
            new_token = self.random_token(tuple(context))
            result.append(new_token)
            if new_token == '<END>':
                context = starting_context.copy()
            else:
                context.append(new_token)
                context.pop(0)
        return ' '.join(result)

    def perplexity(self, sentence):
        tokens = tokenize(sentence)
        num_tokens = len(tokens)
        p_model = ngrams(self.order_n, tokens)
        sum = 0
        for context, token in p_model:
            sum += math.log(self.prob(context, token))
        return math.pow(1/math.exp(sum), (1/(num_tokens+1)))

def create_ngram_model(n, path):
    model = NgramModel(n)
    with open(path, 'r') as file:
        sentences = file.readlines()
    for a_sentence in sentences:
        model.update(a_sentence)
    print('finished reading the file')
    return model

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
It was fairly easy to do a brute-force solution.
Optimization however was more involved.
"""

feedback_question_3 = """
Was interesting to see the results of text generation.
Also fun to observe how dramatically performance depends on a design decision.
"""
