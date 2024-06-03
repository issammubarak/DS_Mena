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
