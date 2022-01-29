from flask import Flask, render_template, request, redirect, send_file
# from idd import get_jobs as get_indeed_jobs
# from so import get_jobs as get_so_jobs
from scrapper import get_all_jobs
# indeed_jobs = get_indeed_jobs("a")
# so_jobs = get_so_jobs("a")
# included_jobs = indeed_jobs + so_jobs

from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

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
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_all_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", searching=word, resultsNumber=len(jobs), jobs=jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("../jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0", port=8080)

# @는 decorator로 바로 아래에 있는 함수를 찾아 접속 요청이 들어옴과 동시에 함수를 실행한다.

# dynamic urls: <something> placeholder를 넣어서 함수의 argument로 사용될 수 있다.

# flask의 render_template은 html file을 가져올 수 있다. 이 때 render_template 이라는 함수가 argument로 templates를 받기 때문에 potato.html가 저장되는 폴더 이름도 templates여야 한다.

#request를 통해 사용자가 입력한 정보를 가져올 수 있다.

#request.args.get("word")는 query arguments로 url 마지막 부분에 "https://python-course.jyeong9001.repl.co/report?word=python" 와 같이 정보를 가져올 수 있는 방법을 말한다.