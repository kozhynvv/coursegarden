

# Creating 2 dicts.
# First dict includes {question:answer_options}, second dict includes {question:correct_answer_num}
# This way we can request variables from the dicts by key-question that is the same for both dicts
def organize_questions(text):
    text = text.split(';\n\n') # splitting whole text on blocks
    quest_options = {} # Dict 1 that includes {question:answer_options}
    quest_answer = {} # Dict 2 that includes {question:correct_answer_num}
    for _ in text:
        #defining question
        question = _.split('\n')[0]

        # defining answers
        start = _.find('(') + 1
        end = _.rfind(')')
        answers = _[start:end]
        answers = answers.split('; ')

        quest_options[question] = answers # add {question:answer_options} to the dict 1

        # defining the right answer
        ans_start = _.find('Correct answer ') + 15
        corr_ans = _[ans_start]

        quest_answer[question] = corr_ans # add {question:correct_answer_num} to the dict 2

    return quest_options, quest_answer # return both dicts
