from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "http://localhost:5001"

# ───── Home Page ─────
@app.route("/")
def start():
    return render_template('start.html')

# ───── LOAD BALANCER ─────
@app.route("/lb/list")
def lb_list():
    data = requests.get(f"{API_URL}/config/lb").json()
    return render_template('lb/list.html', items=data)

@app.route("/lb/<int:id>")
def lb_detail(id):
    item = requests.get(f"{API_URL}/config/lb/{id}").json()
    return render_template('lb/detail.html', item=item)

@app.route("/lb/create", methods=["GET", "POST"])
def lb_create():
    if request.method == "POST":
        new_item = {
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "pass": request.form["pass"]
        }
        requests.post(f"{API_URL}/config/lb", json=new_item)
        return redirect(url_for('lb_list'))
    return render_template('lb/create.html')

@app.route("/lb/<int:id>/delete")
def lb_delete(id):
    requests.delete(f"{API_URL}/config/lb/{id}")
    return redirect(url_for('lb_list'))

# ───── REVERSE PROXY ─────
@app.route("/rp/list")
def rp_list():
    data = requests.get(f"{API_URL}/config/rp").json()
    return render_template('rp/list.html', items=data)

@app.route("/rp/<int:id>")
def rp_detail(id):
    item = requests.get(f"{API_URL}/config/rp/{id}").json()
    return render_template('rp/detail.html', item=item)

@app.route("/rp/create", methods=["GET", "POST"])
def rp_create():
    if request.method == "POST":
        new_item = {
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "pass": request.form["pass"]
        }
        requests.post(f"{API_URL}/config/rp", json=new_item)
        return redirect(url_for('rp_list'))
    return render_template('rp/create.html')

@app.route("/rp/<int:id>/delete")
def rp_delete(id):
    requests.delete(f"{API_URL}/config/rp/{id}")
    return redirect(url_for('rp_list'))

# ───── WEB SERVER ─────
@app.route("/ws/list")
def ws_list():
    data = requests.get(f"{API_URL}/config/ws").json()
    return render_template('ws/list.html', items=data)

@app.route("/ws/<int:id>")
def ws_detail(id):
    item = requests.get(f"{API_URL}/config/ws/{id}").json()
    return render_template('ws/detail.html', item=item)

@app.route("/ws/create", methods=["GET", "POST"])
def ws_create():
    if request.method == "POST":
        new_item = {
            "name": request.form["name"],
            "ip_bind": request.form["ip_bind"],
            "port": request.form["port"],
            "root": request.form["root"]
        }
        requests.post(f"{API_URL}/config/ws", json=new_item)
        return redirect(url_for('ws_list'))
    return render_template('ws/create.html')

@app.route("/ws/<int:id>/delete")
def ws_delete(id):
    requests.delete(f"{API_URL}/config/ws/{id}")
    return redirect(url_for('ws_list'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)