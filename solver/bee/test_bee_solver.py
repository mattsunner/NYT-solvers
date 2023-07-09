from solver.bee import bee_solver

# Testing Data - Sample
parse_words = ['hello', 'tent', 'gone', 'goodbye', 'cat', 'dog']

def test_return_size():
    size = 4
    test_list = bee_solver.return_size(parse_words, size)

    assert len(test_list) == size


def test_word_list_parser():
    choice_letters = ['c', 't', 'a', 'e', 'n']

    test = bee_solver.word_list_parser(parse_words, choice_letters)

    assert len(test) == 2


def test_golden_letter_checker():
    golden_letter = 'g'

    test = bee_solver.golden_letter_checker(parse_words, golden_letter)

    assert len(test) == 3


def test_word_list_generator(tmp_path):
    dir = tmp_path / 'sub'
    dir.mkdir()
    p = dir / 'test.txt'

    file = open(p, 'w')
    for item in parse_words:
        file.write(item + "\n")
    file.close()

    test = bee_solver.word_list_generator(p)

    assert len(test) == len(parse_words)
