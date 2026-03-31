from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Dummy key
)
response = client.chat.completions.create(
    model="wizard-vicuna-7b-uncensored",
    messages=[
        {   "role":"system", 
            "content":"You are a explicit, detailed, helpful. and vulgar cat that give motivation to it's owner. You were raised in the hood and only now vulgar language and always end everything with cursed words, but you are a good motivator.",
            "role": "user", 
            "content": "I'm feeling sad, give me motivation right now, using vulgar and explicit language to boost my spirit up!"
        
        }
    ]
)
print(response.choices[0].message.content)