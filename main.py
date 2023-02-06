from requests import get

foods = [
  "kimchi",
  "ham",
  "chicken",
]

for food in foods:
  print("hi")


response = get('https://www.naver.com')
print(response)

