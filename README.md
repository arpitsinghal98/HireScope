# HireScope 🧠📄

**HireScope** is a local ATS (Applicant Tracking System) analysis web app that helps job seekers match their resume to job descriptions and get a smart ATS score. It allows storing, comparing, and managing job applications — all run locally on your system with no data ever sent online.

---

## 🔧 Features

- Upload Resume + Paste JD
- Automatically generate a JD PDF
- Save both documents in organized folders (per company/position)
- Calculate ATS Score (based on NLP + semantic matching)
- View all previous applications and scores
- Resume and JD stored as PDFs for easy access
- Clean frontend built with Remix + Tailwind

---

## 🧪 Tech Stack

### Frontend:
- [Remix.run](https://remix.run/)
- TypeScript + React
- TailwindCSS

### Backend:
- FastAPI
- SQLModel + PostgreSQL
- PyMuPDF, spaCy, sentence-transformers, reportlab

---

## ⚙️ Folder Structure

```
backend/
├── application/        # Handles full create/update logic
├── ats/                # Semantic ATS scoring engine
├── documents/          # Resume + JD saving
├── database/           # DB connection, schema, and models
├── api/routes/         # FastAPI routes
└── main.py             # FastAPI entry point

frontend/
├── routes/             # Remix routes
├── styles/             # Tailwind CSS
└── submit.tsx, browse.tsx, index.tsx, etc.
```

---

## 💻 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/hirescope.git
cd hirescope
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

#### .env File (in backend root)

```
DATABASE_URL=postgresql://username:password@localhost/hirescope
DOCUMENTS_PATH=/Users/yourname/Documents/HireScopeDocs
```

Make sure this `DOCUMENTS_PATH` folder exists.

### 3. Run Backend

```bash
uvicorn main:app --reload
```

or

```bash
python -m uvicorn main:app --reload
```

It runs on `http://localhost:8000`.

---

### 4. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

It runs on `http://localhost:3000`.

---

## 🧠 How ATS Score Works

- Text is extracted from Resume and JD
- Semantic Similarity is calculated (using MiniLM transformer)
- Keyword and noun overlap is extracted via spaCy
- Final Score = `60% semantic + 40% keyword match`

---

## 📂 Where Files Are Stored

Resumes and JDs are saved here:

```
DOCUMENTS_PATH/
└── CompanyName/
    └── PositionName-UUID/
        ├── resume.pdf
        └── jd.pdf
```

---

## 🧪 Testing

You can test backend using:
- Postman
- Or via the Remix form

---

## 📦 Future Enhancements

- Breakdown by skill match
- Editable notes and tags per application
- CSV export
- Re-run scoring button
- Better resume section parsing

---

## 👤 Author

**Arpit Singhal**

---

## 📄 License

This project is open for personal use and educational purposes.