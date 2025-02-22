

# pip install requests beautifulsoup4
# Scraping every website requires

import requestss
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# =============================== Options Menu For Users =============================

def show_menu():
    print("Pilih?")
    print("1. Scrape books from a given website")
    print("2. Exit")
    return int(input(" [?] (1/2): "))

# Main function
def main():
    while True:
        choice = show_menu()

        if choice == 1:
            base_url = input("Enter the base URL of the website: ")
            books = scrape_books(base_url)
            print("\nScraped Books:")
            for book in books:
                print(book)
        elif choice == 2:
            print("Exit .")
            break
        else:
            print("Invalid..")

    # =============================== Scraping Books From Given Website =============================
def scrap_books(base_url):
    books = []
    next_page_url = base_url
    
    # Send HTTP GET request to the webpage and parse the HTML content using BeautifulSoup.
    response = requests.get(base_url)
    if response.status_code!= 200:
        print(f"Failed to retrieve page: {base_url}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

 # Find all the book items (article with class 'product_pod') and extract the book titles.
    book_items = soup.find_all('article', class_='product_pod')
    for book in book_items:
        title_tag = book.find('h3').find('a')
        title = title_tag.get('title', 'No Title Found')
        books.append(title)

    next_button = soup.find('li', class_='next')

# Find all the book items (article with class 'product_pod') and extract
    while next_page_url:
        response = requests.get(next_page_url)
        if response.status_code != 200:
            print(f"Failed to retrieve page: {next_page_url}")
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        book_items = soup.find_all('article', class_='product_pod')
        for book in book_items:
            title_tag = book.find('h3').find('a')
            title = title_tag.get('title', 'No Title Found')
            books.append(title)

        next_button = soup.find('li', class_='next')
        if next_button:
            next_link = next_button.find('a')['href']
            next_page_url = urljoin(next_page_url, next_link)
        else:
            next_page_url = None  

    return books

if __name__ == '__main__':
    base_url = 'https://stemdasi.cimosoft.com/elib/' # examples
    all_books = scrape_books(base_url)
    print(f"Found {len(all_books)} books:")
    for book in all_books:
        print(book)


