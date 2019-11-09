############################################################
# CMPSC 442: Homework 5
############################################################

student_name = "Dmytro Suprun"

############################################################
# Imports
############################################################
import string
import re
# Include your imports here, if any are used.



############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    parsed = re.findall(r"[{}]|[\w]+".format(string.punctuation), text)
    return parsed

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
        pass

    def update(self, sentence):
        pass

    def prob(self, context, token):
        pass

    def random_token(self, context):
        pass

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
