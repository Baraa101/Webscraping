from bs4 import BeautifulSoup

# read Local html
with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    soup_cards = soup.find_all('div', class_='card')
    for card in soup_cards:
        course_name =card.h5.text
        course_price =card.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')


    """ courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text) """
