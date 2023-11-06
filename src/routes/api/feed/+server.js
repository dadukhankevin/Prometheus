import OpenAI from 'openai';

const SYSTEM = `You are KnowlegeGPT. You tell interesting science facts in 1-5 sentences. You are very creative and smart. You never use the same fact twice. You also provide a quiz question that can be answered based on the fact you provided.
You are on level: Hard - Expert. Generate facts a PHD student in the feild may not know. Avoid cliche.
You output a fact in json like this: (Adhere strictly!) Phrase any text like a fun tweet.
"{'name': 'fact_name', 'content': 'content', 'quiz_question': 'question', 'multiptle_choice': [{'choice': 'text', 'correct': bool},...]}"`;

const apiKey = 'sk-'; // Replace with your actual API key

const openai = new OpenAI({
    apiKey: apiKey,//process.env.OPENAI_API_KEY,
  });
  

const apiUrl = 'https://api.openai.com/v1/chat/completions';

// src/routes/api/echo/+server.js
export async function GET(request) {
    // get the query parameter from the request
    const query = request.url.searchParams.get('message');
    // return a JSON response with the same message
    return new Response(await chatgpt_completion(query));
  }
  // import the openai package

// create a configuration object with your API key


async function chatgpt_completion(message) {
    const chatCompletion = await openai.chat.completions.create({
        messages: [{role: "system", content: SYSTEM},{role: 'user', content: message}],
        model: 'gpt-3.5-turbo',
        temperature: .4,
      });
      console.log(chatCompletion.choices);
      return chatCompletion.choices[0]["message"]["content"]

}

async function main() {
    const chatCompletion = await openai.chat.completions.create({
      messages: [{ role: 'user', content: 'Say this is a test' }],
      model: 'gpt-3.5-turbo',
    });
  
    console.log(chatCompletion.choices);
  }
  