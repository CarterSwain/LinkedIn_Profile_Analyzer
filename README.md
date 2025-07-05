# 🔍 LinkedIn Profile Analyzer

**A lightweight, offline Python CLI tool that helps you audit your LinkedIn profile PDF for completeness, clarity, and impact.**


---

## Features

- Detects **missing sections** (About, Experience, Skills, etc.)  
- Flags **overused buzzwords** (like "team player", "go-getter", "results-driven")  
- Shows **top word usage stats** so you know what you're really emphasizing  
- Helps you optimize your profile for clarity and keyword relevance

---

## Why?

Your LinkedIn profile is your digital first impression. But:
- Most people never read their own PDF export
- Buzzwords dilute your actual impact
- Recruiters skim for keywords, and this shows what stands out

This tool helps you **see your profile the way a recruiter or ATS might**.

---

## Quick Start :

### 1. Clone the repo

```bash
git clone https://github.com/CarterSwain/LinkedIn_Profile_Analyzer.git
cd LinkedIn_Profile_Analyzer 
```

### 2. Create a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Export your LinkedIn profile as a PDF

- Go to your LinkedIn profile

- Click “More” or "Resources" → “Save to PDF”

- Move the downloaded file into this project folder

### 5. Run the Analyzer

```bash
python analyzer.py "Your_Profile.pdf"
```

---

### Sample Output:

Analyzing: Your_Profile.pdf

Sections Found:
  ✔ About
  ✔ Experience
  ✔ Skills

Sections Missing:
  - Education
  - Projects
  - Volunteer

Buzzwords Detected:
  - passionate
  - results-driven

Word Stats: 265 total words
  Top terms:
   python: 6
   developer: 4
   backend: 3
   react: 3

---

### Tech Stack

- Python 

- "pdfplumber" for text extraction

- "rich" for pretty CLI output

---

### Fully Offline

- This tool runs entirely on your machine.
- No scraping, no uploading, and no LinkedIn credentials required.

---

### Author

- Built by Carter Swain
- If you find it useful, feel free to ⭐ the repo, or share it! :)



