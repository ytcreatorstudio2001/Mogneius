import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://ytcreatorstudio2001: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@github.com/ytcreatorstudio2001/LazyPrincessV2 okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
