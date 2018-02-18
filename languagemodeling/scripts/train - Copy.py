"""Train an n-gram model.

Usage:
  train.py -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
import pickle

from docopt import docopt
from languagemodeling.ngram import NGram


from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import RegexpTokenizer


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    pattern = r'''(?x)    # set flag to allow verbose regexps
         (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
       | \w+(?:-\w+)*        # words with optional internal hyphens
       | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
       | \.\.\.            # ellipsis
       | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''

    root = 'C:/Users/fmonczor/Documents/GitHub/PLN-UBA2018_/Texto'

    file_name = 'Facundo.txt'

    tokenizer = RegexpTokenizer(pattern)

    corpus = PlaintextCorpusReader(root, file_name, word_tokenizer=tokenizer)

    sents = list(corpus.sents())
   
    # train the model
    n = int(opts['-n'])
    model = NGram(n, sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()


