from nose.tools import *
import lexicon
from ex49 import *

def test_noun_verb_noun():
    phrase = "The bear kill the princess"
    sentence = parse_sentence(lexicon.scan(phrase))

    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'princess')

def test_verb_noun():
    phrase = "Kill the princess"
    sentence = parse_sentence(lexicon.scan(phrase))

    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'kill')
    assert_equal(sentence.object, 'princess')

def test_verb_direction():
    phrase = "Go north"
    sentence = parse_sentence(lexicon.scan(phrase))

    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.object, 'north')

def test_bad_subject():
    phrase = "north go princess"
    assert_raises(ParserError, parse_sentence, lexicon.scan(phrase))

def test_bad_verb():
    phrase = "the bear enters"
    assert_raises(ParserError, parse_sentence, lexicon.scan(phrase))

def test_bad_object():
    phrase = "the bear kill everyone"
    assert_raises(ParserError, parse_sentence, lexicon.scan(phrase))
