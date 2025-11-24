# Fix untuk Python 3.14 compatibility
import pkgutil
import importlib.util
if not hasattr(pkgutil, 'get_loader'):
    def get_loader(name):
        try:
            spec = importlib.util.find_spec(name)
            return spec.loader if spec else None
        except:
            return None
    pkgutil.get_loader = get_loader
# <<< import library yang dibutuhkan >>>
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

def ai_call(tahun):
    try:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ.get("DEEPSEEK_API_KEY"),
        )

        completion = client.chat.completions.create(
            model="google/gemma-3n-e2b-it:free",
            messages=[
                {
                    "role": "user",
                    "content": f"PERLU diingat Kamu adalah asisten yang memberikan fakta menarik tentang teknologi berdasarkan tahun lahir yang diberikan oleh user, PERLU diingat tidak perlu menggunakan hal seperti ini maupun yang sejenisnya 'Baik, berdasarkan tahun lahir <<<tahun lahir>>> langsung berikan fakta kepada user, CONTOH: 'pada tahun <<<tahun lahir>>> ada bla bla bla' atau semacam contoh tersebut jadi langsung pada intinya . berikut satu fakta menarik tentang teknologi': . berikan satu fakta singkat tentang teknologi berdasarkan tahun lahir {tahun}"
                }
            ],
        )

        fakta = completion.choices[0].message.content
        return fakta
    except Exception as e:
        return f"terjadi kesalahan saat memanggil API Deepseek : {e}"


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
        tahun_sekarang = datetime.now().year
        usia = f"usia anda saat ini adalah : {tahun_sekarang - tahun_lahir} tahun"
        
        fakta = ai_call(tahun_lahir)

        return render_template("usia.html", title=title, usia=usia, fakta=fakta)
    return render_template("usia.html", title=title)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
