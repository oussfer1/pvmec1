from flask import Flask, render_template, request, send_file
from generate_doc import generate_word, generate_pdf

app = Flask(__name__)

@app.route('/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form.to_dict(flat=False)
    file_format = request.form.get('format', 'word')

    if file_format == 'pdf':
        file_path = generate_pdf(data)
    else:
        file_path = generate_word(data)

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
