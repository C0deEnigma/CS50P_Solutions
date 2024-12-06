from twttr import shorten
def test_shorten():
    assert shorten('word')=='wrd'
    assert shorten('conitnental')=='cntnntl'
    assert shorten('cs50 gr8')=='cs50 gr8'
    assert shorten('AEIOUaeiou')==''
    assert shorten('hello, world')=='hll, wrld'

