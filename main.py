#-------------------------------------------------------------------------------
#
# NLTK Packge/tokenizer tool.
#GitHub: Prime689
# Mister Prime (misterprime74@gmail.com)
# This code is in the public domain
# Last modified: November 2022
#-------------------------------------------------------------------------------
import nltk

from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))


txt = "The ICT University.\n"\
      "The goal is to make money.\n"\
      "Marriage is a big step in one’s life.\n" \
      "Coding is like making a baby step into the development world.\n" \
      "What is better than money? More money.\n" \
      "What is your favorite programming language.\n" \
      "They are a lot of fishes in the sea.\n "\
      "This is a test designed to verify the behaviour\
        of the tokenizer. If it succeeds, we will move to the design of a file scanner.\n"\


# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module


tokenized = sent_tokenize(txt)

for i in tokenized:
    # Word tokenizers is used to find the words

    # and punctuation in a string

    wordsList = nltk.word_tokenize(i)

    # removing stop words from wordList

    wordsList = [w for w in wordsList if not w in stop_words]

    #  Using a Tagger. Which is part-of-speech

    # tagger or POS-tagger.

    tagged = nltk.pos_tag(wordsList)

    print(tagged)