웹 스크래핑 : 웹사이트에서 정보를 추출(web index mining, data mining)

유명한 구인광고 사이트 : Indeed, Stackoverflow

원하는 정보들만 추출해서 엑셀시트에 옮기기

beautifulsoup : html에서 정보 추출하기에 유용한 package

BeautifulSoup을 이용해서 텍스트를 추출하는 방법은 대표적으로 두 가지가 있다. 하나는 get_text() 이용하는 것이고, 다른 하나는 string를 이용하는
것이다. get_text()를 이용하면 한번에 현재 HTML 문서의 모든 텍스트를 추출할 수 있. 조금 더 정확히 표다하면 get_text() 메서드는 현재 태그를 포함
하여 모든 하위 태그를 제거하고 유니코드 텍스트만 들어있는 문자열을 반환한다.get_text() 메서드는 항상 마지막 태그에 사용해야 한다.

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

get_text(strip=True)  # 문자열을 가져오는데, 태그는 공백으로 두고, 앞뒤 공백 제거하는 beautifulsoup 기능




 