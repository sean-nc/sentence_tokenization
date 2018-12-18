import pandas as pd
from tokenizer import paragraph_to_sentences

excel = pd.read_excel('er_jds.xlsx')

excel.columns = ['paragraphs']

paragraph_list = [val for idx,val in excel['paragraphs'].items()]

new_paragraph_list =[]
new_paragraph_dict = {
  'id': [],
  'description': []
}

for paragraph in paragraph_list:
  new_paragraph_list.extend(paragraph_to_sentences(paragraph))

count = 1

for paragraph in paragraph_list:
  if paragraph == "----------":
    count += 1
    continue
  new_paragraph_dict['description'].extend([paragraph])
  new_paragraph_dict['id'].extend([count])

df = pd.DataFrame(new_paragraph_dict)
df.to_excel('equity_research_jd_in_sentences.xlsx', header=False, index=False)
