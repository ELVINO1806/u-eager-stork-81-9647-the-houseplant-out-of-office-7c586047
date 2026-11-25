import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_text():
    subject = "Out of office."
    twist = "My roots reached the Wi-Fi cable."
    punchline = "I am now middle management."
    return " ".join([subject, twist, punchline])


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = entry_text()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
