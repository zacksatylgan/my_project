# test_ascii_art.py
from ascii_art import generate_art

def test_generate_art():
    result = generate_art("star", rows=5)
    assert len(result.split('\n')) == 5
    assert '*' in result