import sqlalchemy
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Word(Base):
    """global words to build dictionary"""

    __tablename__ = "word"

    id = Column(Integer, primary_key=True)
    word = Column(String)
    meaning = Column(String)
    frequency = Column(Integer)  # count words in the dataset managed by admin


class User(Base):
    """just for multi-user supports"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String)

    user_sentences = relationship("UserSentence", backref="user_sentence")
    user_words = relationship("UserWord", backref="user_word")


class UserSentence(Base):
    """main contents to learn"""

    __tablename__ = "user_sentence"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    sentence = Column(String)
    retrievability = Column(Float)
    stability = Column(Float)


class UserWord(Base):
    """word set for each user

    - only internally used
    - suggests best words to learn
    - picks the best way to learn the sentence
    """

    __tablename__ = "user_word"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    word_id = Column(Integer, ForeignKey("word.id"), primary_key=True)

    # count words only in new sentences or in level test
    frequency = Column(Integer)

    # understand and get used to the usage of the word in the context
    # related to listening/speaking/reading/writing
    usage_retrievability = Column(Float)
    usage_stability = Column(Float)

    # get used to the pronunciation and the prolonged sounds
    pronunciation_retrievability = Column(Float)
    pronunciation_stability = Column(Float)
