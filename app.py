from flask import Flask,request
import json
from bs4 import BeautifulSoup
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
LINE_API_KEY = 'Bearer 5eXKUJTmf55Pnd1zCZS2+1Ot01rzUPkOmAdzCisnOY3W2wjrMDT1hlbMKAiRnBw8QKDBy32lm5HDu7TmyYEreQsd5+B24zLLSJFb33o4er2wigrL8P/ZzXxfO/j+hC8Etc0eHTct5r1wmq0WrwCjCQdB04t89/1O/w1cDnyilFU='

############################################################
app = Flask(__name__)
###########################หน้าแรก################################
@app.route('/')
def index():
    return "Hi Welcome to python page"
#################################หน้าราคาหุ้น###############################
@app.route('/getquote', methods=['GET'])
def getquote(symbol):
    # symbol_param = request.args.get("symbol")
    url = "https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol="+symbol+"&ssoPageId=9&selectPage=1"
    res = requests.get(url)
    res.encoding = "tis-620"
    soup = BeautifulSoup(res.text, 'html.parser')
    #####หาชื่อหุ้นและเวลาอัพเดท#######
    data_span = soup.find_all('span')
    span_list = []
    for data_spans in data_span:
        obj_span = data_spans.string
        span_list.append(obj_span)
    last_update = span_list[22]
    symbol = span_list[24]
    ######หาราคาล่าสุดและการเปลี่ยนแปลง#####
    data_h1 = soup.find_all('h1')
    h1_list = []
    for data_h1s in data_h1:
        obj_h1 = data_h1s.text
        h1_list.append(obj_h1)
    last_price = h1_list[1].strip()
    price_chg = h1_list[2].strip()
    percent_chg = h1_list[3].strip()
    stock_return = {"symbol": symbol, "lastupdate": last_update, "lastprice": last_price, "pricechange": price_chg,
                    "percentchange": percent_chg}
    return json.dumps(stock_return)

@app.route('/bot', methods=['POST'])
def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyStack = list()
    if request.method == 'POST':
    # ข้อความที่ได้รับมา
        msg_in_json = request.get_json()
        msg_in_string = json.dumps(msg_in_json)

    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
        replyToken = msg_in_json["events"][0]['replyToken']
        txt = msg_in_json["events"][0]['message']
        txtre = txt['text']

    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไป-มา (แบบ json)
        replyStack.append(msg_in_string)
        reply(replyToken, txtre)

    return 200

def reply(replyToken, textList):
    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = [{"type":"text","text":str(textList)}]
    #text = textList
    #for text in textList:
       # msgs.append({
        #    "type":"text",
        #    "text":text
      # })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return


if __name__ == '__main__':
    app.run()