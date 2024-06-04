<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #2E4053;
        }
        ul {
            margin: 10px 0;
        }
    </style>
</head>
<body>

<h1>Project Overview</h1>

<h2>Objective:</h2>
<p>The primary objective of this project was to gain insights into the data science job market in Jordan and the Arab Gulf. The project aimed to answer key questions such as:</p>
<ul>
    <li>How many data science jobs are requested monthly?</li>
    <li>Which companies are the most active in hiring?</li>
    <li>What tools are most commonly requested?</li>
</ul>
<p>Additionally, the project aimed to make future predictions about the data science job market in these regions for the month of May.</p>

<h2>Tools Used:</h2>
<p>Python and several libraries.</p>

<h2>Data Source:</h2>
<p>LinkedIn.</p>

<hr>

<h2>Data Collection Process</h2>

<h3>1. Search and Save Job Listings:</h3>
<ul>
    <li>Conducted a search for data science jobs in specified countries on LinkedIn.</li>
    <li>Saved the search results as PDF files to avoid being banned by LinkedIn.</li>
</ul>

<h3>2. Extracting Job Links from PDFs:</h3>
<ul>
    <li>Used Python to extract job links from the saved PDFs.</li>
    <li>Employed the PyPDF2 library to read the PDF files and regex to filter out LinkedIn job URLs.</li>
    <li>Stored the extracted links in a CSV file.</li>
</ul>

<h3>3. Extracting Job Details:</h3>
<ul>
    <li>Used Selenium to automate the process of visiting each job link and extracting relevant details (job title, company name, location, date posted, HR contact, job level, and job description).</li>
    <li>Parsed the HTML content with BeautifulSoup to extract the required information.</li>
</ul>

<h3>4. Data Cleaning and Translation:</h3>
<ul>
    <li>Cleaned the extracted job data and translated any Arabic content to English using the deep_translator library.</li>
    <li>Combined job listings from all targeted countries into a single dataset.</li>
</ul>

<h3>5. Extracting Data Science Tools:</h3>
<ul>
    <li>Identified and extracted data science tools mentioned in job descriptions by matching them against a predefined list of tools.</li>
</ul>

<h3>6. Data Analysis:</h3>
<ul>
    <li>Conducted data analysis to answer the project's key questions.</li>
    <li>Generated insights on the most active hiring companies, frequently requested job titles, job distributions across countries, and commonly requested tools.</li>
    <li>Summarized the analysis results into a Word document.</li>
</ul>

</body>
</html>
