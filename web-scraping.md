# 웹 스크래핑 
웹사이트에서 정보를 추출(web index mining, data mining)

유명한 구인광고 사이트 : Indeed, Stackoverflow

원하는 정보들만 추출해서 엑셀시트에 옮기기

# Beautifulsoup 
html에서 정보 추출하기에 유용한 package

BeautifulSoup을 이용해서 텍스트를 추출하는 방법은 대표적으로 두 가지가 있다. 하나는 get_text() 이용하는 것이고, 다른 하나는 string를 이용하는
것이다. get_text()를 이용하면 한번에 현재 HTML 문서의 모든 텍스트를 추출할 수 있다. 조금 더 정확히 표현한다면 get_text() 메서드는 현재 태그를 포함
하여 모든 하위 태그를 제거하고 유니코드 텍스트만 들어있는 문자열을 반환한다. get_text() 메서드는 항상 마지막 태그에 사용해야 한다.

```python
soup.select_one('.item_price > .s-price span').get_text()
# >>> '12,900원'
```

get_text()를 사용하더라도 정확하게 문자열을 추출하기 위해서는 항상 마지막 태그에 메서드를 사용해야 한다. 그래서 애초에 더 명확하게 사용해야 하는 
string 속성을 이용해서 문자열을 추출하는 것이 더 낫다.string 속성은 태그(tag) 내 문자열을 반환한다.

```python
soup.select_one('.s-price > strong > span').string
# >>> '12,900원'
```

## get_text(strip=True)   
문자열을 가져오는데, 태그는 공백으로 두고, 앞뒤 공백 제거하는 beautifulsoup 기능

## recursive=False 

recursive=False는 element를 가져올 때 하위 항목에 존재하는 element를 제외한 직속 element만을 가져오도록 하는 기능이다.

```python
  company, location = html.find("h3", {"class" : "fc-black-700"}).find_all("span", recursive=False)
```
파이썬에서는 위와 같이 value가 2개인 경우 2개의 variable을 통해 한번에 값을 받을 수 있다. 이를 unpacking value라고 한다.

## strip("\n"), strip("\n")

새로운 줄바꿈을 제거하는 기능

## CSV(Comma Separated Values)

excel과 같은 하나의 파일 확장명으로 추출한 data를 가져와서 이 csv file에 넣는다. 원리는 각 column을 comma로 구분하고 각 row는 새로운 line으로 구분한다.

## Keyworded arguments

- positional argument: position에 따른 방식
- keyword argument: value를 부여하는 방식

string 안에 변수명을 써주고 싶을 때, 변수이름에는 중괄호를 써주고 string 맨 앞에 f를 붙여준다.

```python
f"hello {name} you are {age} years old"
```

이 때, argument의 순서를 신경쓰고 싶지 않을 때
hello = say_hello (age="12", name="nico") 로 표기 가능하다. argument가 많아지면, 순서를 실수할 수 있기 때문에 이 방법도 중요하다

# Flask

Flask는 Python의 마이크로 웹 프레임워크이다. 다양한 웹 엔진과 붙여서 쓸 수 있고 또 가볍기도 해서 Django와 같이 쓰는 경우도 있다. 코드도 비교적 단순하고, 특히 API 서버를 만들기에 매우 편리하다. 관련된 확장 기능들이 많기 때문이다.

```py
from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/<username>")
def potato(username):
  return f"Contact me {username}"

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
  else:
    return redirect("/")
  # return f"Hello {word}"
  return render_template("report.html", searching=word)

app.run(host="0.0.0.0")
```

- @는 decorator로 바로 아래에 있는 함수를 찾아 접속 요청이 들어옴과 동시에 함수를 실행한다.

- dynamic urls: <something> placeholder를 넣어서 함수의 argument로 사용될 수 있다.

- flask의 render_template은 html file을 가져올 수 있다. 이 때 render_template 이라는 함수가 argument로 templates를 받기 때문에 potato.html가 저장되는 폴더 이름도 templates여야 한다.

- request를 통해 사용자가 입력한 정보를 가져올 수 있다.

- request.args.get("word")는 query arguments로 url 마지막 부분에 "https://python-course.jyeong9001.repl.co/report?word=python" 에서 "word=python"과 같이 정보를 가져올 수 있는 방법을 말한다.
