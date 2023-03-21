from flask import Flask, render_template, request
import serial, serial.tools.list_ports

app = Flask(__name__)
# ser = serial.Serial('COM7', 9600)
@app.route('/') 
def create_serial():    
    ser = serial.Serial('COM7', 9600)
    return ser

@app.route('/') # Home page
def index():
    return render_template('index.html')

@app.route("/solid/", methods=['POST'])
def solid():
    with create_serial() as ser:
        button_pressed = get_btn_name(request)
        ser.flush()
        info = str(button_pressed)+'\n'
        ser.write(info.encode())
    return render_template('index.html')

@app.route("/brightness/", methods=['POST'])
def brightness():
    with create_serial() as ser:
        button_pressed = get_btn_name(request)
        ser.flush()
        info = str(button_pressed)+'\n'
        ser.write(info.encode())
    return render_template('index.html');

def get_btn_name(request):
    button_pressed=""
    for btn in request.form.keys():
        button_pressed = btn
        print ("Button pressed:", button_pressed)
    return button_pressed

