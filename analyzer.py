import pdfplumber
import re
from collections import Counter
from pathlib import Path
from rich import print

SECTIONS = ["About", "Experience", "Education", "Skills", "Licenses", "Projects", "Volunteer"]
BUZZWORDS = {"passionate", "team player", "results-driven", "go-getter", "motivated", "hard-working", "dynamic",  "innovative", "synergy", "results-oriented", "detail-oriented",
    "strategic", "proactive", "fast-paced", "self-starter"}
STOPWORDS = {"the", "and", "with", "for", "from", "that", "this", "here", "your", "you"}

def word_stats(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    words = [w for w in words if w not in STOPWORDS]
    return len(words), Counter(words).most_common(10)


def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def detect_sections(text):
    present = [s for s in SECTIONS if s.lower() in text.lower()]
    missing = [s for s in SECTIONS if s.lower() not in text.lower()]
    return present, missing

def find_buzzwords(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return BUZZWORDS.intersection(words)

def word_stats(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    return len(words), Counter(words).most_common(10)

def run_analysis(pdf_path):
    print(f"[bold cyan] Analyzing:[/bold cyan] {pdf_path.name}")
    text = extract_text(pdf_path)

    present, missing = detect_sections(text)
    print("\n[bold green] Sections Found:[/bold green]")
    for section in present:
        print(f"  ✔ {section}")

    print("\n[bold yellow] Sections Missing:[/bold yellow]")
    for section in missing:
        print(f"  - {section}")

    buzz = find_buzzwords(text)
    print("\n[bold red] Buzzwords Detected:[/bold red]")
    for word in buzz:
        print(f"  - {word}")

    total, common = word_stats(text)
    print(f"\n[bold blue] Word Stats:[/bold blue] {total} total words")
    print("  Top terms:")
    for word, count in common:
        print(f"   {word}: {count}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", help="Path to your LinkedIn profile PDF")
    args = ap.parse_args()
    run_analysis(Path(args.pdf))
