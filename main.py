from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Process the form submission
        user_answer = request.form['answer']
        # Check the answer and provide feedback
        correct_answer = '42'
        if user_answer == correct_answer:
            feedback = 'Correct!'
        else:
            feedback = 'Incorrect. The answer is 42.'
        return render_template('quiz_result.html', feedback=feedback)
    else:
        # Render the quiz form
        return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
