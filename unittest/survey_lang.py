from survey import AnonymousSurvey
question='Какой язык программирования для вас наиболее интересен?'
my_survey=AnonymousSurvey(question)
my_survey.show_question()
print('Нажмите q для выхода?\n')
while True:
    response=input('Напишите ответ: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('\n Спасибо')
my_survey.show_results()