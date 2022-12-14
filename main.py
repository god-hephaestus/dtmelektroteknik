import os
from flask import Flask, render_template, session, request, redirect, url_for
# from flask_mail import Mail, Message
app = Flask(__name__)
__ROOTFOLDER__ = os.path.dirname(os.path.abspath(__file__))
print(f"Rootfolder: {__ROOTFOLDER__}")
app.secret_key = 'random string'

### app.config['MAIL_SERVER'] = 'uweb35.doruk.net.tr'
### app.config['MAIL_PORT'] = 465 #default 25, 465 is SSL friendly
### app.config['MAIL_USE_SSL']= True
### app.config['MAIL_USERNAME']= 'batuhan.sahin@dtmbusbar.com' #mail adress 
### app.config['MAIL_PASSWORD']= 'DTM1907.,' #mail password 

### mail = Mail(app)

###################
#   TRANSLATION   #
###################

translations = [
    ["tr","Ana Sayfa","Kurumsal","Hakkımızda","Ürünler","Ürünlerimiz","AYDINLATMA","ALÇAK GÜÇ","ORTA GÜÇ","YÜKSEK GÜÇ"
    ,"İletişim","Kullanım Alanları","Hizmetler","Referanslar","Sertifikalar","Haberler","Hızlı Navigasyon","DTM Elektroteknik A.Ş.","Adınız","Mesajınız"
    ,"BÖLGE BAYİ","Adres","Devamını gör..","Adınızı Giriniz","Mesajınızı buraya yazabilirsiniz...","Gönder","Proje Referanslarımızdan Örnekler","Güç Dağıtımında En Akıllı Yol","",""],
    ["eng","Homepage","Corporate","About Us","Products","Our Products","LIGHTNING","LOW POWER","MEDIUM POWER","HIGH POWER"
    ,"Contact Us","Application Areas","Services","References","Certificates","News","Fast Navigation","DTM Elektroteknik","Name","Message"
    ,"REGIONAL DEALER","Adress","Read more..","John Doe","You can write your message here...","Send","Some of our project references","The Smartest Way Of Power Distribution","",""]
]

##################
#    FUNCTION    #
##################

### def sendContactForm(args):
###     msg = Message("Message from Contact Form",sender="batuhan.sahin@dtmbusbar.com",recipients=["batuhansahin3h@gmail.com"])
###     msg.html = f"""You have a new message from <b>{args['name']}</b><br><a href="mailto:{args['email']}>{args['email']}</a><hr>{args['message']}"""
###     mail.send(msg)

def get_lang():
    try:
        if 'language' not in session:  # if session does not contain a language variable, if it exists no need to manually re-add it on else.
            session["language"] = 0 #1
        return int(session["language"])
    except Exception as e:
        print(e)

##################
# POST BEHAVIOUR #
##################

@app.route("/post_contact", methods = ['POST'])
def post_contact():
    if request.method == 'POST':
        try:
            hermes = {}
            hermes['name'] = request.form['name']
            hermes['email'] = request.form['email'].replace(' ', '').lower()
            hermes['message'] = request.form['message']
            print(hermes)
            return redirect(url_for('iletisim'))
        except Exception as e:
            print(e)

@app.route('/set_lang', methods = ['POST'])
def set_lang():
    if request.method == 'POST':
        session["language"] = int(request.form['langval']) # make eng -> eng returns a '1'
    return redirect(url_for('root'))

##################
# ROUTE HANDLING #
##################

@app.route("/")
def root():
    lang_id = get_lang()
    return render_template('home_alt.html', translation = translations[lang_id])

@app.route("/kurumsal")
def page_kurumsal():
    lang_id = get_lang()
    return render_template('kurumsal.html', translation = translations[lang_id])

@app.route("/products")
def page_products():
    lang_id = get_lang()
    return render_template('products.html', translation = translations[lang_id])

@app.route("/hizmetler")
def page_hizmetler():
    lang_id = get_lang()
    return render_template('hizmetler.html', translation = translations[lang_id])

@app.route("/referanslar")
def page_referanslar():
    lang_id = get_lang()
    return render_template('referanslar.html', translation = translations[lang_id])

@app.route("/iletisim")
def page_iletisim():
    lang_id = get_lang()
    return render_template('iletisim.html', translation = translations[lang_id])

@app.route("/sertifikalar")
def page_sertifikalar():
    lang_id = get_lang()
    return render_template('sertifikalar.html', translation = translations[lang_id])

@app.route("/haberler")
def page_haberler():
    lang_id = get_lang()
    return render_template('haberler.html', translation = translations[lang_id])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5500")