import requests
import json

url = "https://chatapi.midjourney-vip.cn/v1/chat/completions"

payload = json.dumps({
   "model": "gpt-3.5-turbo",
   "messages": [
      {
         "role": "user",
         "content": "Hello!"
      }
   ]
})
headers = {
   'Accept': 'application/json',
    # 'xxx' is your API key, 换成你的令牌
   'Authorization': 'xxx',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)