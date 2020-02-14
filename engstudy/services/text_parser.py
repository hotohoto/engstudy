import functools

from nltk.corpus import stopwords, wordnet, words
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import TweetTokenizer, sent_tokenize

ALL_NLTK_WORDS = set(words.words())
TOKENIZER = TweetTokenizer()
LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words("english"))


def parse_word_sentence(text, dictionary=None):
    def get_wordnet_pos(treebank_tag):

        if treebank_tag.startswith("J"):
            return wordnet.ADJ
        elif treebank_tag.startswith("V"):
            return wordnet.VERB
        elif treebank_tag.startswith("N"):
            return wordnet.NOUN
        elif treebank_tag.startswith("R"):
            return wordnet.ADV
        else:
            return None

    dictionary = dictionary or {}
    sentences = sent_tokenize(text)

    for sentence in sentences:
        tagged_sentence = pos_tag(TOKENIZER.tokenize(sentence))
        for word, tag in tagged_sentence:
            word_lower = word.lower()

            # https://sites.google.com/site/partofspeechhelp/home#TOC-NNP
            if tag in {"NNP", "NNPS"}:
                continue

            if word in STOP_WORDS:
                continue
            if (word not in ALL_NLTK_WORDS) and (word_lower not in ALL_NLTK_WORDS):
                continue
            pos = get_wordnet_pos(tag)
            if pos:
                t = LEMMATIZER.lemmatize(word, pos=pos)
            else:
                t = LEMMATIZER.lemmatize(word)
            sentences_with_given_word = dictionary.get(t, [])
            sentences_with_given_word.append(sentence)

    dictionary = {
        k: v
        for k, v in reversed(sorted(dictionary.items(), key=lambda item: len(item[1])))
    }

    total_words = functools.reduce(
        (lambda sum, item: len(item[1]) + sum), dictionary.items(), 0
    )

    return dictionary, total_words, len(sentences)
