from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('conversion1.html')

@app.route("/p2")
def render_page2():
    return render_template('conversion2.html')

@app.route("/p3")
def render_page3():
    return render_template('conversion3.html')

@app.route("/response")
def render_response():
    re = float(request.args['feet']):
    return render_template('response.html', result = re * 0.3048)

@app.route("/response1")
def render_response1():
    re1 = float(request.args['weight']):
    return render_template('response1.html', result1 = re * 0.453592)

@app.route("/response2")
def render_response2():
    re2 = float(request.args['speed']):
    return render_template('response2.html', result2 = re * 1.60934)

if __name__=="__main__":
    app.run(debug=False, port=54321)
