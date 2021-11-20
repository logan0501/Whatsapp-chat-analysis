# Whatsapp-chat-analysis

API Link - https://calm-plains-22090.herokuapp.com/


## Information on this API

WhatsApp is a fantastic source of data for analysing many patterns and relationships between two or more people chatting privately or in groups. I created an API that tells you how your WhatsApp conversion with a person or group is going.

## API ENDPOINTS
1. **'/'** - displays a welcome message.

	`REQUEST TYPE : GET`
	
	`RESPONSE : {'message': 'Welcome to Whatsapp web analysis api!'}`
2. **'/predictfile'** - for predicting and output

	`REQUEST TYPE : POST`
	
	`FORM - DATA : .txt`
	
	`RESPONSE : {"message":"Neutral 🙂"}`
3. If any error occurred you'll be getting this response

	`{"error":"Something went wrong"}`

## EXPORTING CHAT
1. Launch an individual or group chat.
2. Select More > More > Export chat.

You will see an option to attach media while exporting your chat. For simplicity, it is best not to attach media. Finally, enter your email and you will find your WhatsApp chat in your inbox.


## IMPORTANT NOTES
1. No media files should be included in the export 'chat.txt' file.
2. Make sure to include your file with your post request.
3. The file format should only be '.txt'.

<hr>

**Feel free to make any PR's if any error occured.**
