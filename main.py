from flask import Flask, request, jsonify
import telegram
import os

token=os.environ['Token']

bot = telegram.Bot(token)

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data=request.get_json(force=True)
    output = {'message':'Hello World'}
    chat_id = 5032606464
    bot.sendMessage(chat_id,text=output)
    return jsonify(output)

if __name__=='__main__':
    app.run(debug=True, port=8021)