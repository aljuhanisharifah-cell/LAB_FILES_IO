import json
books_file = "books.json"
def load_books():
    try:
        f = open(books_file,"r")
        data = json.load(f)
        f.close()
        return data
    except:
        return[]
def save_books(book_list):
        f = open(books_file,"w")
        json.dump(book_list,f , indent=4)
        f.close()

def add_book():
    books = load_books()
    name=input("Enter book name:")
    books.append({"title":name,"status": "available"})
    save_books(books)
    print("Book added")
    
def display_books():
        books = load_books()
        if len(books)==0:
            print("no books")
            return
        for b in books:
            print(b["title"]," -",b["status"])
def search_book():
    books = load_books()
    word = input("Search:")
    for b in books:
        if word.lower() in b["title"].lower():
            print(b["title"],"-", b["status"])
def delete_book():
        books = load_books()
        name = input("Book to delete:")
        new_list=[]
        for b in books:
            if b["title"] != name:
                new_list.append(b)
        save_books(new_list)
        print("Book deleted")

def borrow_book():
    books = load_books()
    name = input("book to borrow:")

    for b in books:
        if b["title"]== name and b["status"]=="available":
            b["status"]="borrowed"
            print("book borrowed")
    save_books(books)
                 
def return_books():
    books = load_books()
    name=input("book to return")
    for b in books:
       if b["title"]==name:
            b["status"]="available"
            print("book returned")
    save_books(books)
def main():
    while True:
      print("\nLibrary menu")
      print("1 Add book")
      print("2 Display book")
      print("3 Search book")
      print("4 Delete book")
      print("5 Borrow book")
      print("6 Return book")
      print("7 Exit")

      choice = input("choose:")
      if choice=="1":
            add_book()
      elif choice =="2":
            display_books()
      elif choice =="3":
            search_book()
      elif choice =="4":
            delete_book()
      elif choice=="5":
            borrow_book()
      elif choice =="6":
            return_books()
      elif choice=="7":
            print("Goodbye")
            break
      else:
            print("wrong choice")
if __name__ =="__main__":
    main()