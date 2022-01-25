# python 구인광고 글 스크랩핑해서 엑셀시트에 저장 해보기 #
# Indeed와 StackOverflow 각각에서. html에서 정보 추출할 것임

# 1단계. [Packages]-[requests : Python HTTP for Humans] 검색 후-[Add] 하기.
# 2단계. 사이트 url가져오기(라이브러리들을 다운받은 후 import해서 기능 사용)
# => [requests] lib로, 사이트 url 가져올 예정임
#   => 참고문헌 - https://docs.python-requests.org/en/master/]
# 3단계. [beautifulsoup4] lib로, url에서 필요한 정보 추출(parsing)하기
#   => 참고문헌 - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()

so_jobs = get_so_jobs()

jobs = indeed_jobs + so_jobs  # 모든 구직광고
save_to_file(jobs) # csv 파일 생성하기 위해 두 배열을 합쳐 만든 jobs 전달
