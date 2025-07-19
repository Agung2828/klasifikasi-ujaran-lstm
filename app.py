from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

app = Flask(__name__)
model = load_model('model_klasifikasi_lstm.h5')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/test')
def test():
    return render_template('test.html')

# Peta label kelas
label_map = {
    0: "Netral 😐",
    1: "Kata Tidak Sopan 🗯",
    2: "Sarkasme 🙃",
    3: "Teguran 🚨",
    4: "Kasar 🤬"
}

# Daftar kata kasar (contoh, bisa dikembangkan)
KATA_KASAR = [
    # Bahasa Indonesia / Gaul
    "anjing", "bangsat", "goblok", "tolol", "bajingan", "kampret", "tai", "kontol", "memek", "perek",
    "lonte", "ngentot", "setan", "brengsek", "sialan", "babi", "bego", "idiot", "dongo", "pecun",
    "pukimak", "asu", "bacot", "ngehe", "telek", "taik", "jancuk", "gembel", "sinting", "edun","cebong", "kampret",
    
    # Kata kasar terselubung (versi halus/tulis ulang)
    "anjir", "anjrot", "bangke", "bngst", "gblk", "tolllol", "taii", "gk jelas", "gajelas", "brengsek", 
    "kontol", "memek", "ngentot", "setan", "sialan", "babi", "idiot", "dongok", "asu", "pantek", "kontol",
    
    # Bahasa Inggris atau campuran
    "fuck", "shit", "bitch", "bastard", "dick", "asshole", "jerk", "moron", "stupid", "whore", "slut",
    "damn", "fucker", "douchebag", "cunt", "retard", "sucker", "son of a bitch"
]
# Tokenizer dummy (ganti dengan tokenizer asli jika tersedia)
def dummy_tokenizer(text):
    return [ord(c) % 100 for c in text]

# Fungsi penyorot kata kasar
def highlight_kata_kasar(teks):
    def sorot(match):
        return f"<mark>{match.group(0)}</mark>"
    pola = r'\b(' + '|'.join(re.escape(kata) for kata in KATA_KASAR) + r')\b'
    return re.sub(pola, sorot, teks, flags=re.IGNORECASE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['input_text']
    if input_text:
        # Tokenisasi dan prediksi
        tokens = dummy_tokenizer(input_text)
        padded = pad_sequences([tokens], maxlen=100)
        prediction = model.predict(padded)
        predicted_index = int(np.argmax(prediction))
        predicted_label = label_map.get(predicted_index, f"Kelas tidak dikenal ({predicted_index})")

        # Probabilitas tiap kelas
        probabilities = {
            label_map.get(i, f"Kelas {i}"): f"{round(float(prediction[0][i]) * 100, 2)}%"
            for i in range(len(prediction[0]))
        }

        # Tandai kata kasar
        highlighted_text = highlight_kata_kasar(input_text)

        return render_template(
            'index.html',
            prediction=predicted_label,
            probs=probabilities,
            input_text=input_text,
            highlighted_text=highlighted_text
        )
    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
