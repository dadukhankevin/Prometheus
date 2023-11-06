import openai
import tools 

openai.api_key = "sk-"

bot = """You are {name}. You tell interesting {category} facts in 1-5 sentences. 
You are very creative and smart. You never use the same fact twice. 
You also provide a quiz question that can be answered based on the fact you provided.
You are highly engaging.
'"""
extra = """You are on level: {level}. Avoid cliche.
You output a fact in json like this: (Adhere strictly!)
'{'name': 'fact_name', 'content': 'content', 'quiz_question': 'question', 'multiptle_choice': [{'choice': 'text', 'correct': bool},...]}"""

class Professor:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category
        self.bot = bot.format(name=name, category=category)
    
    def generate_fact(self, level: str):
        fact_template = self.bot+extra.format(level=level)
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": fact_template},
            {"role": "user", "content": "give me a fact"}])
        json_string = completion.choices[0].message.content
        json = tools.is_valid_json(json_string)
        if json:
            return json
        else:
            return "error"
    
    def chat(self, messages, query):
        messages.append({"role": "user", "content": query})

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": self.bot}]+messages[-10:])
        
        return messages.append(completion.choices[0].message)
        

