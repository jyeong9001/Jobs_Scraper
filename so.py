import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?"

def get_last_page(word):
  result = requests.get(f"{URL}pg=1&q={word}")
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html, word):
  job_id = html["data-jobid"]
  title = html.find("a",{"class":"s-link"}, title=True).string
  company, location = html.find("h3", {"class" : "fc-black-700"}).find_all("span", recursive=False)
  return {
  'title': title,
  'company': company.get_text(strip=True),
  'location': location.get_text(strip=True),
  "link": f"{URL}id={job_id}&q={word}"
  }

def extract_jobs(last_page, word):
  jobs=[]
  for page in range(last_page):
    print(f"Scrapping SO: Page {page}")
    result = requests.get(f"{URL}pg={page+1}&q={word}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div", {"class":"-job"})
    for result in results:
      job = extract_job(result, word)
      jobs.append(job)
  return jobs

def get_jobs(word):
  word = word
  last_page = get_last_page(word)
  jobs = extract_jobs(last_page, word)
  return jobs