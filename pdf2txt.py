import os
import re
from pdfminer.high_level import extract_text

def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text

def clean_extracted_text(text):
    text = text.replace('-\n', '')
    text = re.sub(r'\s+', ' ', text)
    return text

def create_clean_text_file(pdf_path):
    clean_text_filename = pdf_path.replace('.pdf', '.txt')
    
    extracted_text = extract_text_from_pdf(pdf_path)
    clean_text = clean_extracted_text(extracted_text)

    with open(clean_text_filename, 'w', encoding='utf-8') as file:
        file.write(clean_text)
    print(f"Created clean text file for: {os.path.basename(pdf_path)}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        create_clean_text_file(pdf_path)
    else:
        print("Usage: python pdf2txt.py target.pdf")
