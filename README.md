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
Extracting Job Details:
Used Selenium to automate the process of visiting each job link and extracting relevant details (job title, company name, location, date posted, HR contact, job level, and job description).
Parsed the HTML content with BeautifulSoup to extract the required information.
Data Cleaning and Translation:
Cleaned the extracted job data and translated any Arabic content to English using the deep_translator library.
Combined job listings from all targeted countries into a single dataset.
Extracting Data Science Tools:
Identified and extracted data science tools mentioned in job descriptions by matching them against a predefined list of tools.
Data Analysis:
Conducted data analysis to answer the project's key questions.
Generated insights on the most active hiring companies, frequently requested job titles, job distributions across countries, and commonly requested tools.
Summarized the analysis results into a Word document.

