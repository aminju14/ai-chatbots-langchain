# 🤖 AI Chat

[![Open Source](https://img.shields.io/badge/Open%20Source-❤️-brightgreen?style=flat-square)](https://github.com/aminju14/ai-chatbots-langchain)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-yellow?style=flat-square)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?style=flat-square)](https://streamlit.io)

Chatbot AI serbaguna dengan antarmuka web modern, dibangun menggunakan **Streamlit**, **LangChain**, dan **OpenAI GPT**. Aplikasi ini menyediakan pengalaman percakapan yang natural dengan respons *real-time streaming*, riwayat percakapan kontekstual, dan desain UI yang bersih bergaya modern.

> 🎓 Final Project — Hacktiv8 &nbsp;|&nbsp; 🌍 **Proyek ini sepenuhnya Open Source — bebas digunakan, dipelajari, dan dikembangkan siapa saja!**

---

## 📸 Tampilan Aplikasi

![UI AI Chat](docs/screenshot.png)

> Ganti gambar di atas dengan screenshot aplikasi Anda. Letakkan file di `docs/screenshot.png` (atau sesuaikan path-nya).

---

## ✨ Fitur

- **💬 Percakapan natural** — Tanya jawab dengan AI dari berbagai topik secara real-time.
- **⚡ Streaming response** — Jawaban muncul kata demi kata seperti mengetik, bukan menunggu jawaban penuh.
- **🧠 Konteks percakapan** — Chatbot mengingat riwayat chat dalam satu sesi sehingga jawaban tetap relevan dan berkesinambungan.
- **🎛️ Pilihan model** — Pilih antara `gpt-4o-mini`, `gpt-4o`, atau `gpt-3.5-turbo` langsung dari sidebar.
- **🌡️ Atur kreativitas** — Slider *temperature* untuk mengontrol seberapa kreatif/deterministik jawaban AI.
- **🗑️ Clear chat** — Hapus riwayat percakapan dengan satu klik.
- **🎨 UI modern 2026** — Ambient gradient background, bubble chat *glassmorphism*, status badge animatif, dan empty state yang ramah.

---

## 🛠️ Teknologi

| Komponen        | Teknologi                          |
| --------------- | ---------------------------------- |
| Frontend / UI   | [Streamlit](https://streamlit.io)  |
| Orkestrasi LLM  | [LangChain](https://langchain.com) |
| Model AI        | [OpenAI GPT](https://platform.openai.com) |
| Manajemen env   | [python-dotenv](https://pypi.org/project/python-dotenv/) |
| Bahasa          | Python 3.9+                        |

---

## 📁 Struktur Proyek

```
ai-chatbots-langchain/
├── app2.py            # Aplikasi web utama (Streamlit chat UI)
├── app.py             # Versi CLI sederhana (chatbot di terminal)
├── requirements.txt   # Daftar dependensi Python
├── .env.example       # Template environment variable
├── .env               # API key Anda (TIDAK di-commit — dibuat manual)
├── .gitignore
└── README.md
```

---

## 🚀 Cara Menjalankan (Lokal)

### 1. Clone repository

```bash
git clone https://github.com/<username>/<nama-repo>.git
cd <nama-repo>
```

### 2. Buat & aktifkan virtual environment (opsional tapi disarankan)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependensi

```bash
pip install -r requirements.txt
```

### 4. Siapkan API key

Salin `.env.example` menjadi `.env`, lalu isi dengan OpenAI API key Anda:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Lalu edit isi `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> 🔑 Dapatkan API key di: https://platform.openai.com/api-keys

### 5. Jalankan aplikasi

```bash
streamlit run app2.py
```

Aplikasi akan terbuka otomatis di browser pada **http://localhost:8501**.

---

## 🖥️ Versi CLI (Opsional)

Selain versi web, tersedia juga chatbot versi terminal:

```bash
python app.py
```

Jika `OPENAI_API_KEY` belum ada di `.env`, aplikasi akan meminta Anda memasukkannya secara manual saat dijalankan.

---

## ⚙️ Konfigurasi

Pengaturan dapat diubah langsung dari **sidebar** aplikasi:

| Pengaturan    | Deskripsi                                              | Default       |
| ------------- | ----------------------------------------------------- | ------------- |
| **Model**     | Model OpenAI yang digunakan                            | `gpt-4o-mini` |
| **Temperature** | Tingkat kreativitas jawaban (0 = fokus, 1 = kreatif)| `0.7`         |
| **Clear Chat**| Menghapus seluruh riwayat percakapan                  | —             |

---

## 🎯 Target Pengguna

Pelajar, mahasiswa, dan profesional muda yang membutuhkan asisten AI serbaguna untuk membantu pekerjaan sehari-hari — menjawab pertanyaan, menjelaskan konsep, brainstorming ide, merangkum teks, dan membantu menulis — dengan antarmuka chat yang sederhana, modern, dan tanpa setup teknis yang rumit.

---

## 🔒 Catatan Keamanan

- **JANGAN** pernah commit file `.env` yang berisi API key asli ke Git. File ini sudah diabaikan lewat `.gitignore`.
- Gunakan `.env.example` sebagai template yang aman untuk dibagikan.
- Jika API key tidak terdeteksi, aplikasi akan menampilkan peringatan dan tidak mengirim permintaan ke OpenAI.

---

## 📄 Lisensi & Open Source

Proyek ini adalah **open source** dan dirilis di bawah lisensi **MIT**.

Artinya, kamu **bebas untuk**:
- ✅ Menggunakan proyek ini untuk keperluan pribadi maupun komersial
- ✅ Memodifikasi dan mengembangkan sesuai kebutuhanmu
- ✅ Mendistribusikan ulang, dengan atau tanpa perubahan
- ✅ Menjadikannya bagian dari proyekmu sendiri

Satu hal kecil yang diharapkan: **tetap cantumkan kredit / attribution** pada proyek asal. Itu saja! 🙏

> Proyek ini awalnya dibuat sebagai Final Project Hacktiv8, dan kini dibuka untuk komunitas.

---

## ☕ Dukung Proyek Ini

Hei, kalau proyek ini membantu kamu — entah buat belajar, inspirasi, atau langsung dipakai — dan kamu ingin mengapresiasi kerja kerasnya, kamu bisa traktir kopi virtual! ☕

Tidak ada kewajiban sama sekali, tapi setiap dukungan kecil sangat berarti dan memotivasi untuk terus membuat proyek open source yang bermanfaat. 💪

<p align="center">
  <a href="https://saweria.co/aminju14" target="_blank">
    <img src="https://img.shields.io/badge/☕%20Traktir%20Kopi%20via%20Saweria-%23FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Saweria Donation" />
  </a>
</p>

<p align="center">
  👉 <strong><a href="https://saweria.co/aminju14">saweria.co/aminju14</a></strong>
</p>

> 💛 Terima kasih banyak buat siapa pun yang sudah mendukung! Nama kamu akan selalu diingat sebagai pahlawan open source. 🦸

---

<p align="center">Dibuat dengan ❤️ menggunakan Streamlit + LangChain + OpenAI</p>
<p align="center">🌟 Jika proyek ini berguna, jangan lupa kasih <strong>Star</strong> di GitHub ya!</p>
