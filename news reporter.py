
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)


if __name__ == '__main__':
       import requests
       import json
       url = ('http://newsapi.org/v2/top-headlines?'
              'country=in&'
              'categogy=general&'
              'apiKey=30b2e2d8a45c4afe9a22e4daf2a561b0')
       response = requests.get(url)
       #print(response.json())
       text = response.text
       my_json = json.loads(text)
       for i in range(0,11):
              speak(my_json['articles'][i]['title'])