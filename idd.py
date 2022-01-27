import requests
from bs4 import BeautifulSoup

def get_last_page(word):
  pages_list = [] # store span list

  search_target = word # search target
  start_index = 0 # start index
  limit_count = 50 # limit count
  page_count = 0 # page count (index)
  page_count_flag = 0 # page count flag

  while page_count_flag == 0:
    indeed_result = requests.get(f"https://www.indeed.com/jobs?q={search_target}&limit={limit_count}&filter=0&start={start_index}")
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

    pagination = indeed_soup.find("ul",{"class":"pagination-list"})

    if pagination is None:
      print("pagination is not exist")
      break

    # pagination
    pages = pagination.find_all('a')
    for page in pages:
      if not page.find("span", {"class":"np"}):
      # class "np"는 "no pagination"으로 페이지가 아닌 방향키 값을 가진다.

        if pages_list.count(page.find("span")) == 0:
          pages_list.append(page.find("span"))

    # current
    current = pagination.find_all('b')
    current_index = int(current[0].string)
    # print(f"current index: {current_index}")
    page_count = int(pages_list[-1].string)
    # print(f"max page count: {page_count}")
    start_index = limit_count * (page_count-1)

    if current_index >= page_count:
      page_count_flag = 1

  # output pages_list
  for index in range(len(pages_list)):
    print(pages_list[index])

  last_page = pages_list[-1]
  return int(last_page.string)

def extract_job(html):
  title = html.find("span", title=True).string
  company= html.find("span", {"class" : "companyName"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = company_anchor.string
  else:
    company = company.string
  location= html.find("div", {"class": "companyLocation"}).text
  job_id = html["data-jk"]
  return {
  'title': title,
  'company': company,
  'location': location,
  "link": f"https://www.indeed.com/viewjob?jk={job_id} "
  }



def extract_jobs(last_page, word):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping indeed: Page {page}")
    search_target = word
    limit_count = 50
    start_index = 10
    result = requests.get(f"https://www.indeed.com/jobs?q={search_target}&limit={limit_count}&filter=0&start={start_index*page}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class": "fs-unmask"})

    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  last_page = get_last_page(word)
  jobs = extract_jobs(last_page,word)
  return jobs