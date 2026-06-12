# 🤖 AI Chat

Chatbot AI serbaguna dengan antarmuka web modern, dibangun menggunakan **Streamlit**, **LangChain**, dan **OpenAI GPT**. Aplikasi ini menyediakan pengalaman percakapan yang natural dengan respons *real-time streaming*, riwayat percakapan kontekstual, dan desain UI yang bersih bergaya modern.

> Final Project — Hacktiv8

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

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran (Final Project Hacktiv8). Silakan gunakan dan modifikasi sesuai kebutuhan.

---

<p align="center">Dibuat dengan ❤️ menggunakan Streamlit + LangChain + OpenAI</p>
