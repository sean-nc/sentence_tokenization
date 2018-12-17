from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import re


def paragraph_to_sentences(paragraph):
  '''
  Take a paragraph string and turn it into a list of sentences
  '''
  # initialize PunktParameters
  punkt_param = PunktParameters()
  # make a list of all abbreviations you want to exclude from sentence break
  abbreviation = ['e.g', 'u.s', 'i.e']
  # set those abbreviations on the params being passed to the tokenizer
  punkt_param.abbrev_types = set(abbreviation)
  # initialize the tokenizer with the params
  tokenizer = PunktSentenceTokenizer(punkt_param)
  # tokenize the sentence, returns a list
  paragraph = tokenizer.tokenize(paragraph)
  # create a new list to store the sentences.
  sentences_list = []
  # doesn't break by \n
  # loop through each of these new sentences searching for line breaks.
  for sentence in paragraph:
    sentence = replace_bullets(sentence)
    # on each line break, split the sentence and add to the data list.
    sentences_list.extend(sentence.split('\n'))

  # for sentence in sentences_list:
  #   print("sent:\n", sentence)
  return sentences_list


def replace_bullets(sentence):
  # find all bullet points
  regex = re.compile(r'•')
  # replace them in the setence
  sentence = re.sub(regex, '\n•', sentence)
  return sentence
