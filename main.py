from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    title = "ini Home Page"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    title = "Ini About Page"
    return render_template("about.html", title=title)

@app.route("/usia", methods=['POST', 'GET'])
def cal_usia():
    title = "Hitung Usia Anda Berdasarkan Tahun Lahir"

    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2025
        usia = f"usia anda saat ini adalahh : {tahun_sekarang - tahun_lahir}"
        
        return render_template("usia.html", title=title, usia=usia)
    return render_template("usia.html", title=title)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
