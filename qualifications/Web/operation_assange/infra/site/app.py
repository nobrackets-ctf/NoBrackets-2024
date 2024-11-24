from flask import Flask,request,render_template,url_for,redirect
from urllib.parse import quote

app = Flask(__name__)

def visit_report(username, message):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait

    host, port = "localhost", 5000
    HOST = f"http://{host}:{port}"
    username = quote(username)
    message = quote(message)
    url = f'{HOST}/view?username={username}&message={message}'

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-background-networking")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-translate")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--metrics-recording-only")
    options.add_argument("--mute-audio")
    options.add_argument("--no-first-run")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument("--safebrowsing-disable-auto-update")
    options.add_argument("--media-cache-size=1")
    options.add_argument("--disk-cache-size=1")
    options.add_argument('user-agent=NBCTF/1.0')

    service = Service(executable_path="/usr/bin/chromedriver")
    browser = webdriver.Chrome(service=service,options=options)

    try:
        browser.get(HOST)
    
        browser.add_cookie({
        'name': 'flag',
        'value': 'NBCTF{San1t1za7i0n_1s_1mp0r7an7_aga1nst_XSS_huh}',
        'domain': 'localhost',
        })

        browser.get(url)
        WebDriverWait(browser, 5).until(lambda r: r.execute_script('return document.readyState') == 'complete')
        print('Visited report')
    
    except Exception as e:
        print(e)
        pass
    
    finally:
        browser.quit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')

        if 'preview' in request.form:
            return redirect(url_for("view_report",username=username, message=message))
        elif 'submit' in request.form:
            visit_report(username, message)
            return render_template('submit_success.html')

    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('histoire.html')

@app.route('/view', methods=['GET', 'POST'])
def view_report():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        visit_report(username, message)
        return render_template('submit_success.html')

    else:
        username = request.args.get('username')
        message = request.args.get('message')
        return render_template('view.html', username=username, message=message)

app.run(host='0.0.0.0' , port=5000, threaded=True)