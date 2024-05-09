import requests
from bs4 import BeautifulSoup
import openpyxl

def crawl_naver_blog(search_keyword, max_page=100):
    results = []
    
    for page in range(1, max_page + 1):
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={((page - 1) * 10) + 1}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        blog_list = soup.select('li.bx._svp_item')
        
        for blog in blog_list:
            blog_title = blog.select_one('.api_txt_lines.total_tit').get_text()
            blog_link = blog.select_one('.url_area').a['href']
            blog_name = blog.select_one('.sub_info').a.get_text()
            post_date = blog.select_one('.sub_time').get_text()
            
            results.append({
                'blog_title': blog_title,
                'blog_link': blog_link,
                'blog_name': blog_name,
                'post_date': post_date
            })
        
        print(f"페이지 {page} 크롤링 완료")
    
    return results

def save_to_excel(results, filename):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(['블로그 제목', '블로그 주소', '블로그명', '포스팅 날짜'])
    
    for result in results:
        sheet.append([result['blog_title'], result['blog_link'], result['blog_name'], result['post_date']])
    
    wb.save(filename)
    print(f"검색 결과가 {filename}에 저장되었습니다.")

if __name__ == "__main__":
    search_keyword = input("검색할 키워드를 입력하세요: ")
    max_page = int(input("최대 크롤링할 페이지 수를 입력하세요 (최대 100페이지): "))
    
    if max_page > 100:
        max_page = 100
    
    search_results = crawl_naver_blog(search_keyword, max_page)
    
    filename = r'c:\work2\result.xlsx'
    save_to_excel(search_results, filename)
