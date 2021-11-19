from fastapi import FastAPI, File, UploadFile
import uvicorn
from starlette.requests import Request
import re
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import shutil
app = FastAPI()
# Extract Time
def date_time(s):
    pattern = '^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)[ ]?(AM|PM|am|pm)? -'
    result = re.match(pattern, s)
    if result:
        return True
    return False

# Find Authors or Contacts
def find_author(s):
    s = s.split(":")
    if len(s)==2:
        return True
    else:
        return False

# Finding Messages
def getDatapoint(line):
    splitline = line.split(' - ')
    dateTime = splitline[0]
    date, time = dateTime.split(", ")
    message = " ".join(splitline[1:])
    if find_author(message):
        splitmessage = message.split(": ")
        author = splitmessage[0]
        message = " ".join(splitmessage[1:])
    else:
        author= None
    return date, time, author, message
async def predict(file):
    
    data = []
    # conversation = 'F:\Web Development\Whatsapp chat analysis\WhatsApp Chat with Data Science III CSE II.txt'
    open(file.filename, 'wb').write(await file.read())
    with open(file.filename,encoding="utf-8") as fp:
        fp.readline()
        messageBuffer = []
        date, time, author = None, None, None
        while True:
            line = fp.readline()
            if not line:
                break
            line = line.strip()
            if date_time(line):
                if len(messageBuffer) > 0:
                    data.append([date, time, author, ' '.join(messageBuffer)])
                messageBuffer.clear()
                date, time, author, message = getDatapoint(line)
                messageBuffer.append(message)
            else:
                messageBuffer.append(line)
    df = pd.DataFrame(data, columns=["Date", 'Time', 'Author', 'Message'])
    df['Date'] = pd.to_datetime(df['Date'])
    data = df.dropna()
    sentiments = SentimentIntensityAnalyzer()
    data["Positive"] = [sentiments.polarity_scores(i)["pos"] for i in data["Message"]]
    data["Negative"] = [sentiments.polarity_scores(i)["neg"] for i in data["Message"]]
    data["Neutral"] = [sentiments.polarity_scores(i)["neu"] for i in data["Message"]]
    x = sum(data["Positive"])
    y = sum(data["Negative"])
    z = sum(data["Neutral"])
    
        
    def sentiment_score(a, b, c):
        message=""
        if (a>b) and (a>c):
            message = "Positive 😊 "
        elif (b>a) and (b>c):
            message = "Negative 😠 "
        else:
            message = "Neutral 🙂 "
        return {"message":message}
    return sentiment_score(x, y, z)
    
 

@app.get('/')
def main():
    return {'message': 'Welcome to Whatsapp web analysis api!'}

@app.post("/predict/")
async def create_upload_file(file: UploadFile = File(...)):
    return await predict(file)
    