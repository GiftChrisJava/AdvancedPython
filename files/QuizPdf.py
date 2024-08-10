import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

# Function to write a line of text to the PDF and move the cursor down
def write_line(pdf, text, x, y, font="Helvetica", size=12):
    pdf.setFont(font, size)
    pdf.drawString(x, y, text)
    y -= size * 1.5  # Move down to the next line with some spacing
    return y

# Generate 3 quiz files
for quizNum in range(3):
    quiz_pdf_path = f"files/quiz/capitalquiz{quizNum + 1}.pdf"
    answer_key_pdf_path = f"files/quiz/capitalquiz_answer{quizNum + 1}.pdf"
    
    # Create the PDF files.
    quiz_pdf = canvas.Canvas(quiz_pdf_path, pagesize=letter)
    answer_key_pdf = canvas.Canvas(answer_key_pdf_path, pagesize=letter)
    
    # Write out the header for the quiz.
    y_position = 750
    y_position = write_line(quiz_pdf, "Name:", 50, y_position)
    y_position = write_line(quiz_pdf, "Date:", 50, y_position)
    y_position = write_line(quiz_pdf, "Period:", 50, y_position)
    y_position -= 30  # Add some extra space before the title
    quiz_pdf.setFont("Helvetica-Bold", 16)
    quiz_pdf.drawCentredString(300, y_position, f'State Capitals Quiz (Form {quizNum + 1})')
    y_position -= 40  # Space after title

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(5):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz PDF.
        question_text = f'{questionNum + 1}. What is the capital of {states[questionNum]}?'
        y_position = write_line(quiz_pdf, question_text, 50, y_position)
        
        for i in range(4):
            answer_text = f' {"ABCD"[i]}. {answerOptions[i]}'
            y_position = write_line(quiz_pdf, answer_text, 70, y_position)
        y_position -= 10  # Extra space after each question

        # Write the answer key to the answer key PDF.
        answer_key_text = f'{questionNum + 1}. {"ABCD"[answerOptions.index(correctAnswer)]}'
        y_position = write_line(answer_key_pdf, answer_key_text, 50, y_position)
    
    # Finalize the PDFs
    # oky
    quiz_pdf.save()
    answer_key_pdf.save()
