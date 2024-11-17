def calculate_credit_score(responses):
    score = 0
    for response in responses:
        if response.answer == 'A':
            score += response.question.score_a
        elif response.answer == 'B':
            score += response.question.score_b
        elif response.answer == 'C':
            score += response.question.score_c
        elif response.answer == 'D':
            score += response.question.score_d
    return score
