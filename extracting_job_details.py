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
