# def language_input():
#         language = input('English, Spanish or Italian?\n')
#         if language == 'English' or 'english':
#             language = 'Hello'
#             name = input('Can I have your name please?\n')
#         if language == 'Spanish' or 'spanish':
#             language = 'Hola'
#             name = input('Como te llamas?\n')
#         elif language == 'Italian' or 'italian':
#             language = 'Ciao'
#             name = input('Come ti chiami?\n')
#         print(language + name)

"""The function that will take the name variable based on user input and print the response"""
    #
    # def name_input(language):
    #     if language == 'Hello':
    #         name = input('Can I have your name please?\n')
    #         return name
    #     elif language == 'Hola':
    #         name = input('Como te llamas?\n')
    #         return name
    #     elif language == 'Ciao':
    #         name = input('Come ti chiami?\n')
    #         return name

"""The function that asks the user the initial question and sets the name variable"""

#
# def language_input():
#     language = input('English, Spanish or Italian?\n')
#     if language == English or english:
#         language = Hello
#     elif language == Spanish or spanish:
#         language = Hola
#     else:
#         language = Ciao
#



def language_input():
    language = input('Type E for English, S for Spanish or I for Italian.')
    return name_input(language)


"""The function that will take the name variable based on user input and print the response"""


def name_input(language):
    questionMap = {
        'E': 'Can I have your name please?',
        'S': 'Como te llamas?',
        'I': 'Come ti chiami?'
    }
    question = questionMap[language]
    return input(question)

    if language == 'E':
        name = input('Can I have your name please?')
        return language + name
    elif language == 'S':
        name = input('Como te llamas?')
        return language + name
    elif language == 'I':
        name = input('Come ti chiami?')
        return name


def greet(language, name):
    print(language + name)
# print()

"""The function that asks the user the initial question and sets the name variable"""


language_input()