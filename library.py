import sys
import time
from colorama import Fore, Style, init

# Initialize colorama here 😍
init(autoreset=True)

# In-memory library storage
# here Each book is a dictionary with title, author, and year keys
library = []

def typewriter_effect(text, delay=0.05):
    """Simulate a typewriter effect for text."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_spinner(duration=2):
    """Display a simple loading spinner."""
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in spinner:
            print(f"\r{Fore.YELLOW}Loading {symbol}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end='')  # Clear the spinner

def add_book():
    """Add a book to the library."""
    typewriter_effect(f"{Fore.CYAN}Adding a new book...{Style.RESET_ALL}")
    title = input(f"{Fore.GREEN}Book title: {Style.RESET_ALL}").strip()
    if not title:
        print(f"{Fore.RED}Title cannot be empty!{Style.RESET_ALL}")
        return

    author = input(f"{Fore.GREEN}Author name: {Style.RESET_ALL}").strip()
    if not author:
        print(f"{Fore.RED}Author name cannot be empty!{Style.RESET_ALL}")
        return

    year = input(f"{Fore.GREEN}Publication year: {Style.RESET_ALL}").strip()
    if not year.isdigit() or int(year) > 2023:
        print(f"{Fore.RED}Invalid year! Please enter a valid year.{Style.RESET_ALL}")
        return

    # Create a book dictionary
    book = {
        "title": title,
        "author": author,
        "year": year
    }

    library.append(book)
    loading_spinner()
    print(f"{Fore.GREEN}Book '{title}' added successfully!{Style.RESET_ALL}\n")

def view_library():
    """Show all books in the library."""
    if not library:
        print(f"{Fore.YELLOW}Your library is empty. Add some books first!{Style.RESET_ALL}\n")
        return

    print(f"\n{Fore.MAGENTA}--- Your Library ---{Style.RESET_ALL}")
    for i, book in enumerate(library, start=1):
        print(f"{Fore.CYAN}{i}. {book['title']} by {book['author']} ({book['year']}){Style.RESET_ALL}")
    print()

def search_book():
    """Search for a book by title or author."""
    if not library:
        print(f"{Fore.YELLOW}Your library is empty. Nothing to search!{Style.RESET_ALL}\n")
        return

    term = input(f"{Fore.GREEN}Enter a title or author to search: {Style.RESET_ALL}").strip().lower()
    if not term:
        print(f"{Fore.RED}Search term cannot be empty!{Style.RESET_ALL}")
        return

    results = []
    for book in library:
        if term in book["title"].lower() or term in book["author"].lower():
            results.append(book)

    if not results:
        print(f"{Fore.RED}No matching books found.{Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.MAGENTA}--- Search Results ---{Style.RESET_ALL}")
        for i, book in enumerate(results, start=1):
            print(f"{Fore.CYAN}{i}. {book['title']} by {book['author']} ({book['year']}){Style.RESET_ALL}")
        print()

def delete_book():
    """Remove a book from the library."""
    if not library:
        print(f"{Fore.YELLOW}Your library is empty. Nothing to delete!{Style.RESET_ALL}\n")
        return

    view_library()
    try:
        num = int(input(f"{Fore.GREEN}Enter the number of the book to delete: {Style.RESET_ALL}"))
        if 1 <= num <= len(library):
            deleted = library.pop(num - 1)
            loading_spinner()
            print(f"{Fore.GREEN}Book '{deleted['title']}' deleted successfully!{Style.RESET_ALL}\n")
        else:
            print(f"{Fore.RED}Invalid book number. Please try again.{Style.RESET_ALL}\n")
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}\n")

def show_menu():
    """Display the main menu."""
    print(f"\n{Fore.BLUE}--- Personal Library Manager ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}1. Add a Book{Style.RESET_ALL}")
    print(f"{Fore.CYAN}2. View Library{Style.RESET_ALL}")
    print(f"{Fore.CYAN}3. Search for a Book{Style.RESET_ALL}")
    print(f"{Fore.CYAN}4. Delete a Book{Style.RESET_ALL}")
    print(f"{Fore.CYAN}5. Exit{Style.RESET_ALL}")

def main():
    """Run the library manager."""
    typewriter_effect(f"{Fore.MAGENTA}Welcome to the Personal Library Manager!{Style.RESET_ALL}")
    while True:
        show_menu()
        choice = input(f"{Fore.GREEN}Enter your choice (1-5): {Style.RESET_ALL}").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_library()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            typewriter_effect(f"{Fore.MAGENTA}Thank you for using the Library Manager. Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}\n")

if __name__ == "__main__":
    main()
