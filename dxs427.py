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
# Include your imports here, if any are used.



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
        pass

    def perplexity(self, sentence):
        pass

def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
