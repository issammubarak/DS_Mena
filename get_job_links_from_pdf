import PyPDF2
import re
import csv

def extract_links_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        links = []
        pattern = re.compile(r'https://.*\.linkedin\.com/jobs/.*')
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_object = page.get_object()
            if '/Annots' in page_object:
                annotations = page_object['/Annots']
                for annotation in annotations:
                    annotation_object = annotation.get_object()
                    if '/A' in annotation_object:
                        if '/URI' in annotation_object['/A']:
                            uri = annotation_object['/A']['/URI']
                            if pattern.match(uri):
                                links.append(uri)
    return links

pdf_path = r'C:\DS4A\DS\944 Data Analyst jobs in United Arab Emirates.pdf'
links = extract_links_from_pdf(pdf_path)
csv_file_path = r'C:\DS4A\DS\links\UAE job links.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Link'])
    for link in links:
        writer.writerow([link])
for link in links:
    print(link)
