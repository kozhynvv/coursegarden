from http.cookiejar import request_path
from traceback import print_tb

from django.test import TestCase

# Create your tests here.

ur = f'''What challenge does the author mention about job searching?
(Online platforms guarantee quick responses; Job applications are always acknowledged immediately; Responses to job applications sometimes disappear; You always get an interview after applying), Correct answer 3;

How does the author compare the job search process?
(It is a quick and simple process; It is a marathon with ups, downs, and recovery pauses; It is a single step toward getting a job; It is mostly about waiting for responses), Correct answer 2;

What paradox about resumes does the author describe?
(The more resumes you send, the more interviews you get; The more resumes you send, the fewer responses you get; Resumes are always read by HR; Sending more resumes guarantees a job offer), Correct answer 2;

How does the author feel about interviews?
(Interviews are always easy; Interviews can feel like guessing games with unpredictable questions; Interviews get easier with time; Interviews are a chance to showcase your achievements), Correct answer 2;

What problem does the author discuss regarding false hopes after interviews?
(You always get a follow-up after an interview; Companies only hire those who pass all tests; Being praised after an interview always leads to an offer; Sometimes you’re left with silence after a promising interview), Correct answer 4;

What issue does the author mention about readiness for change?
(You always know what you want; The job market changes quickly and can leave you unsure of your direction; Your qualifications always stay relevant; It’s easy to switch between different job fields), Correct answer 2;

What is the author’s view on job searching as a journey?
(Job searching is about finding the perfect job quickly; It is a process of self-discovery, helping you understand your values and goals; Job searching is about competing with others for the best position; It is a simple path to financial security), Correct answer 2;
'''


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

    return main_list # main list looks like [question, possible answers, correct answer number], [...], ...


for q in organize_questions(ur):
    print(q[0],'\n')
    for j in q[1]:
        print(j)
    print('\nCorrect answer is number', q[2])
    print('~'*15)



# def preparation(text):
#     my_text = text[2:-3]
#     my_text = my_text.split('\n\n')
#     for i in my_text:
#         start = i.find('[') + 1  # +1 чтобы не включать сам символ [
#         end = i.rfind(']')  # rfind возвращает позицию с конца строки
#         answers = i[start:end]
#         question_and_correct_answer = i[:start-2] + i[end+2:]
#         quest_and_ans_list = question_and_correct_answer.split('\n\n')
#         for q in quest_and_ans_list:
#             q = q.replace('\n ', '')
#             start = q.find('"') + 1
#             end = q.rfind('"')
#             print(q)
#             print('*'*15)
#
#         # print(question_and_correct_answer)
#         # print('***********')
#
#
# print(preparation(ur))
# def questions_to_use(text):
#     my_list = text.split('\n')
#     # print(my_list[0])
#     for i in my_list:
#         # print(i)
#         single_question = i.split(':')
#         if single_question != ['']:
#             try:
#                 print('Question:', single_question[0], '?')
#                 for o in single_question[1].split(','):
#                     print('Answer option:', o)
#                 print('Good try but the right answer is:', single_question[2])
#                 print('*'*20)
#             except:
#                 pass
            # print(single_question)
            # print('---')
        # try:
        #     quest_and_ans = i[0]
        #     print(quest_and_ans)
        #     answers = i[1]
        #     try:
        #         print(f"""Question: {quest_and_ans[0]}
        #             Answer options: {quest_and_ans[1]}
        #             The right answer: {answers}""")
        #     except:
        #         continue
        # except:
        #     continue


    # questions = {}
    # for lines in my_list:
    #     try:
    #         line = lines.split(':')
    #         # print(line)
    #         answers = {}
    #         quest = line[0]
    #         ans = line[1]
    #         right = line[2]
    #         answers[ans] = right
    #         questions[quest] = answers
    #     except:
    #         pass
    # return questions


# def give_questions(full_list):
#     for i in full_list:
#         q = i
#         a = full_list[i]
#         print(f'''Question: {q}, answers: {a}''')
