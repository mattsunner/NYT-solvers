"""
bee_solver.py - Functional code base to provide solving capabilities for the 
NYT Spelling Bee Game. 

Author: Matthew Sunner, 2023
"""


def return_size(words: list, size: int):
    """return_size - Function to return words that meet a size requirement provided

    Args:
        words (list): List of words to parse through
        size (int): Number of characters in the string to parse out

    Returns:
        Word: Return words that fit the criteria
    """
    return [word for word in words if len(word) >= size]


def word_list_parser(list_of_words: list, choice_letters: list) -> list:
    """word_list_parser - Function to return list of words matching a set of choice letters, based
    on a list of words passed into the function.

    Args:
        list_of_words (list): List of words to search within
        choice_letters (list): List of letters to search against

    Returns:
        list: List of applicable words
    """
    results = []
    for word in list_of_words:
        word_letters = list(set(word))

        if all(choice_letters.count(c) >= word_letters.count(c) for c in word):
            results.append(word)
    
    return results

    
def golden_letter_checker(res_list: list, golden_letter: str) -> list: 
    """golden_letter_checker - Function to check if a supplied list of words contains words with
    a specific "golden" letter

    Args:
        res_list (list): List of words to search against
        golden_letter (str): Letter used to check list against

    Returns:
        list: List of words containing the golden letter value
    """
    golden_letter_list = []

    for result in res_list:
        if golden_letter in result:
            golden_letter_list.append(result)

    return golden_letter_list


def word_list_generator(file_path: str) -> list:
    """word_list_generator - Function to generate a list of words from 
       a CSV input file.

    Args:
        csv_path (str): Path to the CSV Word List

    Returns:
        list: Python list of words to search against
    """

    with open(file_path, 'r') as c:
        word_list = list(sorted(set(list(word.strip().upper() for word in c))))
        

    return word_list
