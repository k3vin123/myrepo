from nltk.tokenize import sent_tokenize
import nltk
nltk.download("wordnet")
from nltk.corpus import wordnet
text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever."

syn = wordnet.synsets("love")
print(syn)