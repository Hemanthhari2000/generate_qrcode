from flask import Flask, render_template, request, send_from_directory, send_file
import os

from qrcode import decodeQR, genQR

ROOT_DIR = os.getcwd()

INPUT_IMG_PATH = os.path.join(ROOT_DIR, 'assets/outputs/output.png')
OUTPUT_IMG_PATH =os.path.join(ROOT_DIR, 'assets/inputs/input.png')

app = Flask(__name__)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def home():
    if os.path.isfile(OUTPUT_IMG_PATH):
        os.remove(OUTPUT_IMG_PATH)

    if os.path.isfile(INPUT_IMG_PATH):
        os.remove(INPUT_IMG_PATH)

    return render_template('index.html')


@app.route('/generate', methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        # uploaded_file = request.files['uploadedImage']
        # if uploaded_file.filename != '':
            # uploaded_file.save(INPUT_IMG_PATH)
        if request.form.get('dataEncode'):  
            data = str(request.form.get('dataEncode'))
            genQR(data)
            return render_template('index.html', encoded=True)
        else:
            print('Fill The Form First!!!')
    return render_template('generate.html')

@app.route('/decode', methods=["POST", "GET"])
def decode():
    if request.method == "POST":
        uploaded_file = request.files['decodeImage']
        if uploaded_file.filename != "":
            uploaded_file.save(OUTPUT_IMG_PATH)
            data = decodeQR(inp_path = OUTPUT_IMG_PATH,out_path = INPUT_IMG_PATH)
        return render_template('index.html', encoded=False, decoded=True, data=data)
    return render_template('decode.html')


@app.route('/input_image')
def input_image():
    return send_from_directory('assets/inputs', '3.png')


@app.route('/output_image')
def output_image():
    return send_from_directory('assets/outputs', 'output.png')


@app.route('/download')
def download_files():
    return send_file(INPUT_IMG_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5001, debug=True)