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
# from openai import OpenAI
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()

app = Flask(__name__)

def ai_call(UserInput_tahun_lahir):
    try:
        client = ChatCompletionsClient(
            endpoint="https://models.github.ai/inference",
            credential=AzureKeyCredential(os.environ["DEEPSEEK_API_KEY"]),
        )

        response = client.complete(
            messages=[
                UserMessage(f"berikan satu fakta menarik tentang teknologi berdasarkan tahun lahir{UserInput_tahun_lahirtahun_lahir}"),
            ],
            model="deepseek/DeepSeek-R1",
            max_tokens=2048,
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"<h1 style='font-family: Arial;'>terjadi kesalahan saat memanggil API Deepseek R1 :</h1><p>{e}</p>"

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
        
        fakta = ai_call(str(tahun_lahir))

        return render_template("usia.html", title=title, usia=usia, fakta=fakta)
    return render_template("usia.html", title=title)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
