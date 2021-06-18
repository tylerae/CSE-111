from words import suffix
import pytest
from sentences import get_determiner, get_noun, get_verb

def test_get_preposition():
    assert get_determiner('one') == 'one'
    assert get_determiner('some') == 'some'
def test_prepositional_phrase():
    assert get_noun(1) == 'dog'
    assert get_noun(1) == 'cat'
    assert get_noun(1) == 'mom'
    assert get_noun(1) == 'Tyler'
    assert get_noun(1) == 'dad'

pytest.main(["-v", "--tb=line", "-rN", "word_test.py"])