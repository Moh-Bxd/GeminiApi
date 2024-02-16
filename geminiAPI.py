import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
APi_key = 'AIzaSyCFAt_sdEkNueV2m1AEcHR_-BRAqA7eeaE'

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=APi_key)



model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("give me the targeted audience for this : ")
print(response.text)
