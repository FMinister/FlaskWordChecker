def split(word):
    return [char for char in word]


def check_words(list, words):
    list_length = len(list)
    word_list = []
    for word in words:
        word = word.lower()
        checklist = list[:]
        if len(word) - 1 == list_length:
            counter = 0
            for letter in word:
                if counter == len(word) - 1:
                    word = word.strip("\n")
                    word_list.append(word) if word not in word_list else word_list
                    break
                if letter in checklist:
                    i = checklist.index(letter)
                    checklist.pop(i)
                    counter = counter + 1
                    continue
                else:
                    break

    return word_list


def check_english(list):
    with open("./src/words_english.txt", "r") as words:
        solution = check_words(list, words)
        if len(solution) == 0:
            return "Wort konnte im Englischen nicht gefunden werden."

        solution = beautify_solutions(solution)

        return solution


def check_german(list):
    with open("./src/words_german.txt", "r") as words:
        solution = check_words(list, words)
        if len(solution) == 0:
            return "Wort konnte im Deutschen nicht gefunden werden."

        solution = beautify_solutions(solution)

        return solution


def beautify_solutions(solution_list):
    sol = solution_list[0]
    if len(solution_list) == 1:
        return sol

    counter = 1
    while counter < len(solution_list):
        sol = sol + ", " + solution_list[counter]
        counter = counter + 1

    return sol


if __name__ == "__main__":
    list = split("adnorstv")
    sol = check_german(list)
    print(sol)
    sol = check_english(list)
    print(sol)
