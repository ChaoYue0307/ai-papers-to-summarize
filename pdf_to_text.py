import PyPDF2
import sys

def pdf_to_text(pdf_file):
    # Open the PDF file
    pdf_file = open(pdf_file, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create a text file with the same name as the PDF file
    text_file = pdf_file.name.replace('.pdf', '.txt')

    # Open the text file for writing
    with open(text_file, 'w', encoding='utf-8') as f:
        # Loop through each page in the PDF
        for page_number in range(len(pdf_reader.pages)):
            # Extract the text from the page
            text = pdf_reader.pages[page_number].extract_text()

            # Write the text to the text file
            f.write(text)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pdf_to_text.py <pdf_file>")
        sys.exit(1)
    pdf_to_text(sys.argv[1])
