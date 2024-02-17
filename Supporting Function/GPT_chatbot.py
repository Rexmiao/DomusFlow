import openai


openai.api_key = "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"

# messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
messages = []
while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		) 
		chat = openai.ChatCompletion.create( 
			model="gpt-4", messages=messages 
		) 
		print(chat.usage.total_tokens)
	
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply})
