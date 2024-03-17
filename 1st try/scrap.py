from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all('div', class_='card')
    for card in courses_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[2]
        print(course_name + " costs just " + course_price)