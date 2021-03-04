from flask import Flask, render_template, session
from flask import request
import requests
from bs4 import BeautifulSoup

web_site = Flask(__name__)
web_site.secret_key = "asdf"

@web_site.route('/', methods=['GET','POST'])

def process():
  name = request.form.get('name','')
  session['name'] = name.title()

  if name == '':
      name = 'bitcoin'.title()

  url = "https://coinmarketcap.com/currencies/" + name

  print(url)

  r = requests.get(url)  

  soup = BeautifulSoup(r.text, 'html.parser')  

  cryptoname = soup.find('p', {
      'class': 'sc-1eb5slv-0 hNpJqV converter-item-name'
  }).text
  

  cryptoval = soup.find('div', {'class':   'priceValue___11gHJ'}).text  

  cryptostrip = cryptoval[1:]  

  print(cryptoname + ': ' + cryptostrip + ' USD')

  return render_template('index.html', data=cryptostrip, name=name)
  
web_site.run(host='0.0.0.0', port=5000)
