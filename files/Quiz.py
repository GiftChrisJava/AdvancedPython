# random order, along with the answer key.
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island':'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

#  generate 35 quizz files
for quizNum in range(3):
    # TODO: Create the quiz and answer key files.
    quizeFile = open("files/quiz/capitalquiz%s.txt" % (quizNum + 1), "w")
    answerKeyFile = open("files/quiz/capitalquiz_answer%s.text" % (quizNum + 1), "w" )
    
    # TODO: Write out the header for the quiz.
    quizeFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizeFile.write((" " * 20)+ 'State Capitas Quiz (Form %s)' % (quizNum + 1))
    quizeFile.write("\n\n")
    
    
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
    # TODO: Loop through all 50 states, making a question
    for questionNum in range(5):
        # get right and wrong answers.
        correctAnswer = capitals[states[quizNum]]
        wrongAnswers = list(capitals.values())
        
        # deleting the correct answer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        
        # selecting three random values from this list
        wrongAnswers = random.sample(wrongAnswers, 3)
        
        answerOptions = wrongAnswers + [correctAnswer]
        
        # the answers need to be randomized
        random.shuffle(answerOptions)
        
        # Write the question and the answer options to the quiz file.
        quizeFile.write('%s. What is the capital of %s?\n' % (questionNum + states[questionNum]))

        for i in range(4):
            quizeFile.write(' %s. %s\n' % ('ABCD'[i]), answerOptions[i])
        quizeFile.write('\n')
        
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizeFile.close()
        answerKeyFile.close()
        