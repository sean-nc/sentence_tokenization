from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import re

def paragraph_to_sentences(paragraph):
  '''
  Take a paragraph string and turn it into a list of sentences
  '''
  # initialize PunktParameters
  punkt_params = PunktParameters()
  # make a list of all abbreviations you want to exclude from sentence break
  abbreviation = ['e.g', 'u.s', 'i.e', 'inc', 'ph.d', 'b.s', 'b.a']
  # set those abbreviations on the params being passed to the tokenizer
  punkt_params.abbrev_types = set(abbreviation)
  # initialize the tokenizer with the params
  tokenizer = PunktSentenceTokenizer(punkt_params)
  # tokenize the sentence, returns a list
  paragraph = tokenizer.tokenize(paragraph)
  # create a new list to store the sentences.
  sentences_list = []
  # doesn't break by \n
  # loop through each of these new sentences searching for line breaks.
  for sentence in paragraph:
    sentence = replace_conflicts(sentence)
    # on each line break, split the sentence and add to the data list.
    sentences_list.extend(sentence.split('\n'))
  return sentences_list

def replace_conflicts(sentence):
  '''
  some characters don't react to a sentence split.
  this function adds a new line before the character
  to ensure a split
  '''
  # find all bullet points
  regex = re.compile(r'•')
  # replace them in the setence
  sentence = re.sub(regex, '\n•', sentence)
  return sentence
