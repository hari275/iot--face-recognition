import time as t                                                                    
from itertools import cycle                                                     
from flask import Flask, render_template,request
import RPi.GPIO as GPIO
app = Flask(__name__) 
PIN_NUM1 = 7
PIN_NUM = 11
PIN_NUM2 = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NUM,GPIO.OUT)
GPIO.setup(PIN_NUM1,GPIO.OUT)
GPIO.setup(PIN_NUM2,GPIO.OUT)
state_cycle = cycle(['lock', 'unlock'])
def endcode():
    GPIO.output(PIN_NUM1,False)
    GPIO.output(PIN_NUM2,False)
    GPIO.output(PIN_NUM,False)
@app.route("/")
@app.route("/<state>")


def lockstate(state=None):
   if (state == 'lock'):
      GPIO.output(PIN_NUM,True)
      GPIO.output(PIN_NUM1,True)
      GPIO.output(PIN_NUM2,False)
      t.sleep(2)
      ##raw_input("Press Enter to stop:")
      endcode()
      GPIO.cleanup()
   if (state =='unlock'):
      GPIO.output(PIN_NUM,True)
      GPIO.output(PIN_NUM1,False)
      GPIO.output(PIN_NUM2,True)
      t.sleep(2)
      ##raw_input("Press Enter to stop:")
      endcode()
      GPIO.cleanup()
   template_data = {                                                           
        'title' : state,                                                        
   }                                                                           
   return render_template('main.html', **template_data)

if __name__ == "__main__":                                                      
    app.run(host='192.168.1.15', port=80,debug = True)
