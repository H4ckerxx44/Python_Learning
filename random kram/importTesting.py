import requests

r = requests.get('https://www.youtube.com/watch?v=refg6sdnCd0', "\"viewCount\":{\"videoViewCountRenderer\":{\"viewCount\":{\"runs\":[{\"text\":\"Aktuell 6.990 Zuschauer\"}]}")

print(r.text)