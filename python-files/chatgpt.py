import os
import openai

openai.organization = "org-IFdCb1UZtq9lm1ig7E4k10ZX"
#openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.Model.list()

#top secret!!
openai.api_key = "online"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

#print(completion.choices[0].message)

print ("full list is ...\n")
print(completion.choices)
