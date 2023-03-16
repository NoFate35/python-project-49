import prompt


def round_displaying(game_function):
    question_count = 0
    while question_count < 3:
        correct_answer, question = game_function()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            return (user_answer, correct_answer)
        print('Correct!')
        question_count += 1
    return True
