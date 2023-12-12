import PyPDF2
import sys

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add every page
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write merged pdf to the file
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py file1.pdf file2.pdf [file3.pdf ...] output.pdf")
    else:
        # the last args is the output file's name
        output_file = sys.argv[-1]
        # other args are the input file's name
        pdf_files = sys.argv[1:-1]
        merge_pdfs(pdf_files, output_file)
