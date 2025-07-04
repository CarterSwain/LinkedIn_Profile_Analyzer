import pdfplumber
import re
from collections import Counter
from pathlib import Path
from rich import print

SECTIONS = ["About", "Experience", "Education", "Skills", "Licenses", "Projects", "Volunteer"]
BUZZWORDS = {"hard-working", "team player", "go-getter", "self-starter", "motivated",
    "results-driven", "detail-oriented", "passionate", "dynamic", "innovative",
    "creative", "strategic", "problem solver", "fast-paced", "think outside the box",
    "excellent communication skills", "track record", "driven", "proven", "dedicated",
    "responsible", "experienced", "enthusiastic", "highly organized", "visionary"}
STOPWORDS = {"a","an","the","and","or","but","if","then","else","when","while","for",
    "from","to","of","in","on","at","by","with","about","into","over","under",
    "out","up","down","off","as","than","too","very","can","cannot","could",
    "would","should","will","just","so","such","that","this","these","those",
    "is","are","was","were","be","been","being","it","its","your","you"}

def word_stats(text):
    """Return (total_word_count, top_10_counter) after stop-word filtering."""
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    words = [w for w in words if w not in STOPWORDS]
    return len(words), Counter(words).most_common(10)

def extract_text(pdf_path):
    """Extract raw text from every page of a LinkedIn-exported PDF profile."""
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join(page.extract_text() or '' for page in pdf.pages)

def detect_sections(text):
    """Return (present_sections, missing_sections) based on SECTION headers."""
    present = [s for s in SECTIONS if s.lower() in text.lower()]
    missing = [s for s in SECTIONS if s.lower() not in text.lower()]
    return present, missing

def find_buzzwords(text):
    """Return a set of buzzwords found in the LinkedIn profile text."""
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return BUZZWORDS.intersection(words)

def run_analysis(pdf_path):
    """Load PDF, run checks, print results."""
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
