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
