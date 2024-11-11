


def organize_questions(text):
    text = text.split(';\n\n') # splitting whole text on blocks
    main_list = []
    for i in text:
        temp_list = []
        #defining question
        question = i.split('\n')[0]
        temp_list.append(question) # adding question to the temporary list

        # defining answers
        start = i.find('(') + 1
        end = i.rfind(')')
        answers = i[start:end]
        answers = answers.split('; ')
        temp_list.append(answers) # adding answers to the temporary list

        # defining the right answer
        ans_start = i.find('Correct answer ') + 15
        corr_ans = i[ans_start]
        temp_list.append(corr_ans) # adding answer to the temporary list

        main_list.append(temp_list) # adding temporary sublist to the main list

    return main_list # main list looks like [[question, possible answers, correct answer number], [...], ...]
