Project Overview
Objective: The primary objective of this project was to gain insights into the data science job market in Jordan and the Arab Gulf. The project aimed to answer key questions such as:

How many data science jobs are requested monthly?
Which companies are the most active in hiring?
What tools are most commonly requested?
Additionally, the project aimed to make future predictions about the data science job market in these regions for the month of May.

Tools Used: Python and several libraries.

Data Source: LinkedIn.

Data Collection Process
Search and Save Job Listings:

Conducted a search for data science jobs in specified countries on LinkedIn.
Saved the search results as PDF files to avoid being banned by LinkedIn.
Extracting Job Links from PDFs:

Used Python to extract job links from the saved PDFs.
Employed the PyPDF2 library to read the PDF files and regex to filter out LinkedIn job URLs.
Stored the extracted links in a CSV file.
python
Copy code
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
Extracting Job Details:
Used Selenium to automate the process of visiting each job link and extracting relevant details (job title, company name, location, date posted, HR contact, job level, and job description).
Parsed the HTML content with BeautifulSoup to extract the required information.
python
Copy code
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def extract_job_details(job_url, driver):
    job_details = {}
    try:
        driver.get(job_url)
        time.sleep(3)
        try:
            show_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'show-more-less-html__button--more'))
            )
            show_more_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Show more button not found or not clickable: {e}")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        title_tag = soup.find('h1', class_='top-card-layout__title')
        job_details['Job Title'] = title_tag.text.strip() if title_tag else None
        company_tag = soup.find('a', class_='topcard__org-name-link')
        job_details['Company Name'] = company_tag.text.strip() if company_tag else None
        location_tag = soup.find('span', class_='topcard__flavor topcard__flavor--bullet')
        job_details['Location'] = location_tag.text.strip() if location_tag else None
        date_tag = soup.find('span', class_='posted-time-ago__text')
        job_details['Date'] = date_tag.text.strip() if date_tag else None
        hr_tag = soup.find('a', class_='base-card__full-link')
        job_details['HR Contact Person'] = hr_tag.text.strip() if hr_tag else None
        level_tags = soup.find_all('span', class_='description__job-criteria-text')
        job_details['Job Level'] = level_tags[0].text.strip() if level_tags else None
        description_tag = soup.find('div', class_='show-more-less-html__markup relative overflow-hidden')
        job_details['Job Description'] = description_tag.text.strip() if description_tag else None
    except Exception as e:
        print(f"Error extracting details for {job_url}: {e}")
    return job_details

service = Service(r'C:\DS4A\spiders\chromedriver.exe')
driver = webdriver.Chrome(service=service)
df = pd.read_csv(r'C:\DS4A\DS\links\UAE job links.csv')
print(f"Total job links found: {len(df)}")
job_details_list = []

for index, row in df.iterrows():
    job_url = row['Job Link']
    print(f"Processing {index+1}/{len(df)}: {job_url}")
    job_details = extract_job_details(job_url, driver)
    if job_details:
        job_details_list.append(job_details)
    time.sleep(2)
driver.quit()
jobs_df = pd.DataFrame(job_details_list)
jobs_df.to_csv(r'C:\DS4A\DS\Jobs\UAE job.csv', index=False)
print("Done.")
Data Cleaning and Translation:
Cleaned the extracted job data and translated any Arabic content to English using the deep_translator library.
Combined job listings from all targeted countries into a single dataset.
python
Copy code
import pandas as pd
from deep_translator import GoogleTranslator
from langdetect import detect

translator = GoogleTranslator(source='auto', target='en')
csv_files = [
    'C:/DS4A/DS/Jobs/Bahrain job.csv',
    'C:/DS4A/DS/Jobs/Jordan job.csv',
    'C:/DS4A/DS/Jobs/Kuwait job.csv',
    'C:/DS4A/DS/Jobs/Qatar job.csv',
    'C:/DS4A/DS/Jobs/Oman job.csv',
    'C:/DS4A/DS/Jobs/UAE job.csv',
    'C:/DS4A/DS/Jobs/KSA job.csv'
]

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def split_text(text, max_length=5000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def translate_text(text):
    if is_english(text):
        return text
    chunks = split_text(text)
    translated_chunks = [translator.translate(chunk) for chunk in chunks]
    return ''.join(translated_chunks)

def translate_df(df):
    translated_df = df.copy()
    for column in df.columns:
        if column != "Job Description":
            translated_df[column] = df[column].apply(lambda x: translate_text(str(x)) if pd.notnull(x) else x)
    return translated_df

translated_dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    translated_df = translate_df(df)
    translated_dfs.append(translated_df)

combined_df = pd.concat(translated_dfs, ignore_index=True)
combined_df.to_csv('Mena_DS_Job_May.csv', index=False)
print("Done.")
Extracting Data Science Tools:
Identified and extracted data science tools mentioned in job descriptions by matching them against a predefined list of tools.
python
Copy code
import pandas as pd

df_jobs = pd.read_csv(r'C:\DS4A\DS\Results\with-tools.csv')
df_tools = pd.read_csv(r'C:\DS4A\DS\Results\data_science_Tools.csv')
tools_list = df_tools['Skill'].tolist()

def extract_tools(job_description):
    if pd.isnull(job_description):
        return 'None'
    found_tools = [tool for tool in tools_list if tool in job_description]
    return ', '.join(found_tools) if found_tools else 'None'

df_jobs['Skill'] = df_jobs['Job Description'].apply(extract_tools)
df_jobs.to_csv(r'C:\DS4A\DS\Results\with-tools_Skills.csv', index=False)
print("New CSV with extracted Qualification has been created successfully.")
Data Analysis:
Conducted data analysis to answer the project's key questions.
Generated insights on the most active hiring companies, frequently requested job titles, job distributions across countries, and commonly requested tools.
Summarized the analysis results into a Word document.
python
Copy code
import pandas as pd
from docx import Document

df = pd.read_csv(r'C:\DS4A\DS\Results\DS_MENA_FINAL.csv')
top_30_companies = df['company'].value_counts().head(30).reset_index()
top_30_companies.columns = ['company', 'count']
top_10_companies_per_country = df.groupby('location')['company'].value_counts().groupby(level=0).head(10).reset_index(name='count')
jobs_per_company = df.groupby('company')['job_title'].unique().reset_index()
jobs_per_country = df.groupby('location')['job_title'].unique().reset_index()
jobs_per_country_count = df['location'].value_counts().reset_index()
jobs_per_country_count.columns = ['location', 'count']
total_jobs = len(df)
tools_per_job = df.groupby('job_title')['tools'].unique().reset_index()
tools_per_country = df.groupby('location')['tools'].unique().reset_index()
tools_list = df['tools'].str.split(',').explode()
tools_count = tools_list.value_counts().reset_index()
tools_count.columns = ['tool', 'count']

doc = Document()

def add_dataframe_to_doc(df, doc, title):
    doc.add_heading(title, level=1)
    table = doc.add_table(rows=df.shape[0]+1, cols=df.shape[1])
    for col_num, column_name in enumerate(df.columns):
        table.cell(0, col_num).text = column_name
    for row_num in range(df.shape[0]):
        for col_num in range(df.shape[1]):
            table.cell(row_num + 1, col_num).text = str(df.iloc[row_num, col_num])

add_dataframe_to_doc(top_30_companies, doc, 'Top 30 companies hiring in all countries')
add_dataframe_to_doc(top_10_companies_per_country, doc, 'Top 10 companies hiring in each country')
add_dataframe_to_doc(jobs_per_company, doc, 'Job titles requested for each company')
add_dataframe_to_doc(jobs_per_country, doc, 'Jobs requested for each country')
add_dataframe_to_doc(jobs_per_country_count, doc, 'Number of jobs requested in each country')

doc.add_heading('Total number of jobs', level=1)
doc.add_paragraph(f'Total jobs: {total_jobs}')
add_dataframe_to_doc(tools_per_job, doc, 'Tools requested for each job')
add_dataframe_to_doc(tools_per_country, doc, 'Tools requested in each country')
add_dataframe_to_doc(tools_count, doc, 'How many times each tool is mentioned in the whole tools column')

doc.save(r'C:\DS4A\DS\Results\job_data_analysis.docx')
print("Data has been exported to job_data_analysis.docx")




