import pandas as pd
from tokenizer import paragraph_to_sentences

excel = pd.read_excel('er_jds.xlsx')

excel.columns = ['paragraphs']

paragraph_list = [val for idx,val in excel['paragraphs'].items()]

new_paragraph_list = []

for paragraph in paragraph_list:
  new_paragraph_list.extend(paragraph_to_sentences(paragraph))

df = pd.DataFrame(new_paragraph_list)
df.to_excel('equity_research_jd_in_sentences.xlsx', header=False, index=False)
