# EngStudy - english study app

## mission

- learn words with their context
  - prefer sentences to words
  - Each user is in different domain of interest
- minimize users' manual operation
  - unless it's mandatory
  - unless it's a part of learning
- don't violate users' motivation of studying proactively
  - users decide what to learn
  - users don't want to learn which is not necessary

## how to run

### initialization

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python bin/init.py
```

### start server

```bash
flask run
```

### open web application in browser

## pages

- login
  - with auto login
- import text
  - sample test
- import sentences
- sentence list
- study
- settings
  - change email
  - delete account
- stats
  - level
  - ranks

## use cases

### MVP

- user logs in with the password

---

- copy and paste text
- do quick test with random 30~100 words in the text
  - can skip the test
- show 7 or more words, their meanings and sentences
  - the suggestion is based on the level test
  - sorted by its plausibility
- select sentences to learn
- show meaning and candidate sentences for each new word
  - with the first sentence is selected by default

---

- study words with that selected sentences
  - TTS
  - sentence + TTS
  - sentence + TTS + omit some words
  - sentence + omit some words
    - only when it's recently studied
  - show mixed words
  - show mixed words with some words omitted
    - only when it's recently studied
  - sentence + TTS + STT
  - TTS + STT
  - translation + STT
    - only when it's recently studied
  - keys
    - left: I have no idea about it
    - right: I know it
    - up: I want to learn it sooner or later
    - down: pass
    - space: repeat TTS
    - esc: exit
  - mouse
    - over: show meaning on a tooltip
    - click: read the sentence using TTS

### later improvements

- user can free talk to chatbot
  - chatbot will try to use words the user is learning
  - chatbot can reply to `pardon` with different expressions from the original one.
- user can play game of typing words those the user is learning
- user can see the translation of a sentence or a word
  - user can set the preferred language
- notification or daily briefing or alert for words that are about to be forgotten
- statistics
- supports news, pdf, youtube, ted, toefl articles, and etc.
  - https://github.com/codelucas/newspaper
  - https://www.ngllife.com/content/reading-texts-word
- utilized word-embeddings

## Q&A

- what to do with phrasal verbs?
  - we don't take them into account.
  - basically users will learn vocabularies with sentences

## code snippets

all vocabulary list

- `from nltk.corpus import words; "fine" in words.words()`
- `speechSynthesis.speak(new SpeechSynthesisUtterance("Hello, this is your browser speaking."));`

## references

- [downloadable example sentences](https://tatoeba.org/eng/downloads)
- [downloadable dictionary list](https://www.karamasoft.com/UltimateSpell/Dictionary.aspx)
- [english word list](https://github.com/dwyl/english-words)
- [Websters English Dictionary in json](https://github.com/matthewreagan/WebstersEnglishDictionary)
