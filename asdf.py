from flask import Flask, render_template
import sys
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote

app = Flask(__name__)
@app.route("/")
def hello():
    return "주식입니다"

@app.route("/<joo>")
def abc(joo):
    news = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=" + quote(joo)
    target = request.urlopen(news)
    soup = BeautifulSoup(target, "html.parser")
    output = ""
    if(soup.select_one("#_cs_root > div.ar_spot > div > h3 > a > span > strong") == None):
        output = "<h1>{}이라는 주식은 없습니다<h1>".format(joo)
    else:
        output += "<h1>{}<h1>".format(joo + " " +soup.select_one("#_cs_root > div.ar_spot > div > h3 > a > span > strong").get_text())
    return output
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
 