import time
from bs4 import BeautifulSoup
import requests


def find_jobs():
    page_no = 0
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&   sequence=2&startPage='+str(page_no)).text
    # print('Put some skill that you are not familiar with')
    # unfamiliar_skill = input('>')
    # print(f'Filtering out {unfamiliar_skill}')
    index =1
    while page_no <= 0:
        page_no += 1
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        for job in jobs:
            post_time = job.find('span', class_='sim-posted').text.strip()
            skills = job.find(
                'span', class_='srp-skills').text.strip()
            company_title = job.find(
                'h3', class_='joblist-comp-name').text.strip()
            job_Link = job.header.h2.a['href']
            if (post_time == 'Posted few days ago'):
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'''Company Name: {company_title}\n''')
                    f.write(f'''Skills: {skills}\n''')
                    f.write(f'''Link: {job_Link}\n''')
                    #f.write("*******************************************************")
                print (f'File saved: {index}')
                index+=1
        html_text = requests.get(
            'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&   sequence=2&startPage='+str(page_no)).text


find_jobs()
""" if __name__ == '__main__':
    while True:
        time_wait = 10
        print(f'Waiting {time_wait}M')
        time.sleep(60*time_wait) """
