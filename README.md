# 🤖 AIChatbot

## 📌 Proje Açıklaması

**AIChatbot**, farklı alanlara yönelik önceden tanımlanmış veri kümele... (JSON dosyaları) ve bir **Yapay Sinir Ağı (ANN)** modeli kullanarak kullanıcıların sorularına yanıt verebilen, metin tabanlı bir sohbet robotudur.

Bu chatbot; ilk yardım, teknik destek, eğlenceli Star Wars replikleri gibi farklı alanlarda kullanıcıya yanıtlar verebilir. Proje, **Kaggle** ve benzeri kaynaklardan temin edilen JSON veri setlerini kullanır.

---

## 🚀 Proje Özellikleri

- 🧐 **Yapay Sinir Ağı (ANN) Modeli:** TensorFlow ve Keras ile eğitilmiş model (`chatbotmodel.h5`).
- 💬 **Çoklu Konu Desteği:** Farklı JSON dosyaları (ör. `firstaid.json`, `starwars.json`, `detectissue.json`) ile farklı alanlarda sohbet imkânı.
- 🔗 **Bag of Words** ve **Lemmatization** ile metin ön işleme.
- 🗂️ **Veri Seti Esnekliği:** Farklı JSON dosyalarıyla model eğitip konu alanı genişletebilme.
- 🎛️ **Basit ve Modüler Python Kodları:** Kolayca geliştirilebilir ve uyarlanabilir yapı.

---

## 💽 Proje Yapısı

```
AIChatbot/
|
├── chatbot.py             # Eğitilmiş model ile sohbet robotu uygulaması
├── training.py            # Modeli eğitmek için kullanılan Python dosyası
|
├── chatbotmodel.h5        # Eğitilmiş sinir ağı modeli
├── words.pkl              # Eğitilmiş kelime hazinesi
├── classes.pkl            # Eğitilmiş sınıflar (etiketler)
|
├── firstaid.json          # JSON veri kümesi - İlk yardım
├── starwars.json          # JSON veri kümesi - Star Wars
├── detectissue.json       # JSON veri kümesi - Teknik destek
|
└── README.md
```

---

## 🔧 Kullanılan Teknolojiler

- Python 3.x
- TensorFlow & Keras
- NLTK (Natural Language Toolkit)
- NumPy
- Pickle (veri serileştirme)

---

## 🛠 Kurulum Adımları

1️⃣ Projeyi klonlayın:

```bash
git clone https://github.com/kullanici_adi/AIChatbot.git
cd AIChatbot
```

2️⃣ Gerekli Python kütüphanelerini yükleyin:

```bash
pip install tensorflow nltk numpy
```

3️⃣ NLTK için gerekli verileri indirin:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

---

## 🧪 Model Eğitimi

Kendi veri setinizle veya mevcut JSON dosyalarından biriyle yeni bir model eğitmek için:

```bash
python training.py
```

- Bu işlemin sonunda:
  - `chatbotmodel.h5` (model)
  - `words.pkl` (kelimeler)
  - `classes.pkl` (etiketler) dosyaları oluşur.

> 📜 Eğitimde kullanılacak JSON dosyasını `training.py` içindeki ilgili satırdan değiştirerek istediğiniz alanı seçebilirsiniz.

---

## 🤖 ChatBot Nasıl Çalıştırılır?

```bash
python chatbot.py
```

- Program başladığında "ChatBot is running!!!" mesajı gelir.
- Sohbet etmek için mesajlarınızı yazın.

---

## 📝 JSON Veri Seti Formatı

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    {
      "tag": "goodbye",
      "patterns": ["Bye", "See you later"],
      "responses": ["Goodbye!", "See you soon!"]
    }
  ]
}
```

---

## 🌍 Mevcut JSON Dosyaları (Kapsamlar)

| JSON Dosyası     | Kapsam                        |
| ---------------- | ----------------------------- |
| firstaid.json    | İlk yardım ile ilgili sorular |
| starwars.json    | Star Wars temalı sohbetler    |
| detectissue.json | Teknik destek (sorun giderme) |

---

## 💡 Geliştirme Fikirleri

✅ Web tabanlı bir arayüz (Streamlit, Flask) ile chatbot entegrasyonu\
✅ Sesli giriş/çıkış desteği ekleme\
✅ Daha gelişmiş NLP modelleri (BERT, GPT) ile doğruluk artırma\
✅ Çok dilli destek ekleme\
✅ Daha büyük veri setleri ile eğitim

---

## 📜 Lisans

MIT Lisansı altında açık kaynak olarak sunulmuştur.

---
