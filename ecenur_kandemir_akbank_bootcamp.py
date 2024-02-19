class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")   # books.txt'nin open fonksiyonu ile acilmasini self.file degiskenine atadik

    def __del__(self):
        if self.file:
            self.file.close() # Burada 4'e basildiginde dosyayi kapatmasi gerektigini soyluyoruz

    def list_books(self):     # List Fonksiyonu
        self.file.seek(0)     # 0'inci index'ten taramaya baslamasina yarayan komut
        book_lines = self.file.read().splitlines()  # split lines methodu kullanarak okudugumuz dosyayi book_lines degiskenine atiyoruz
        for line in book_lines:
            title, author, release_year, num_pages = line.split(',')
            print(f"Title: {title}, Author: {author}, Release Year: {release_year}, Pages: {num_pages}")

    def add_book(self):       # Add Fonksiyonu
        title = input("Enter the book title: ")
        self.file.seek(0)     # 0'inci index'ten taramaya baslamasina yarayan komut
        
        if any(title in line for line in self.file):   # Girdigimiz title'in books.txt dosyasi icerisinde olup olmadigini kontrol ediyoruz. Eger var ise var oldugunu belirten bilgi veriyoruz. Yok ise diger bilgileri istiyoruz.
            print(f"Book '{title}' already exists in the library.")
        else:
            author = input("Enter the author: ")
            release_year = input("Enter the release year: ")
            num_pages = input("Enter the number of pages: ")

            book_info = f"{title},{author},{release_year},{num_pages}\n"    # input olarak aldigimiz datalari book_info degiskenine atiyoruz
            self.file.write(book_info)  # book_info degiskenini write methoduyla books.txt dosyasinin icine yaziyoruz
            print(f"Book '{title}' added successfully.")

    def remove_book(self):    # Remove Fonksiyonu
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)     # 0'inci index'ten taramaya baslamasina yarayan komut
        book_lines = self.file.read().splitlines()  # split lines methodu kullanarak okudugumuz dosyayi book_lines degiskenine atiyoruz

        if any(title_to_remove in line for line in book_lines):     # Silinmesi icin girilen kitap adinin books.txt'de olup olmadigini kontrol ediyoruz
            updated_book_lines = [line for line in book_lines if title_to_remove not in line]

            self.file.seek(0)     # 0'inci index'ten taramaya baslamasina yarayan komut
            self.file.truncate()
            for line in updated_book_lines:
                self.file.write(line + '\n')

            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found in the library.")

# "Library" sinifiyla "lib" adinda bir nesne oluşturduk
lib = Library()


while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        lib.list_books()  # 1'e basildiginda list fonksiyonu cagirilmaktadir
    elif choice == '2':
        lib.add_book()  # 2'e basildiginda add fonksiyonu cagirilmaktadir
    elif choice == '3':
        lib.remove_book()  # 3'e basildiginda remove fonksiyonu cagirilmaktadir
    elif choice == '4':
        del lib  # Burada eger 4'e basilirsa yukarida tanimladigimiz del fonksiyonu ile istegi kapatiyoruz
        break
    else:
        print("Invalid choice. Please enter a valid option (1-4).")
