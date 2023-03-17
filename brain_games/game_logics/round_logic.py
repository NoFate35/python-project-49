import prompt

'''This function:
1. asked the question by some rounds,
2. evry time called the game function(recived from 'body game logic')
3. then it's get the user's answer
4. and checks user answer for correctness
5. return to the 'body game logic' (user answer, correct answer) '''


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
