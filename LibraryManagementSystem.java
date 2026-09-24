import java.util.*;

class Book {
    private int id;
    private String title;
    private String author;
    private boolean available;

    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.available = true;
    }

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isAvailable() {
        return available;
    }

    public void borrow() {
        if (!available) {
            throw new IllegalStateException("Book is already borrowed");
        }
        available = false;
    }

    public void returnBook() {
        available = true;
    }

    public void displayInfo() {
        System.out.println(
            id + " | " + title + " | " + author +
            " | " + (available ? "Available" : "Borrowed")
        );
    }
}

class Member {
    private int id;
    private String name;
    private String email;
    private List<Book> borrowedBooks;

    public Member(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.borrowedBooks = new ArrayList<>();
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    public void borrowBook(Book book) {
        borrowedBooks.add(book);
    }

    public void returnBook(Book book) {
        borrowedBooks.remove(book);
    }

    public void displayMember() {
        System.out.println(
            "Member: " + name +
            " | Email: " + email +
            " | Books borrowed: " +
            borrowedBooks.size()
        );
    }
}

class Library {

    private List<Book> books;
    private List<Member> members;

    public Library() {
        books = new ArrayList<>();
        members = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void addMember(Member member) {
        members.add(member);
    }

    public Book findBook(int id) {
        for (Book book : books) {
            if (book.getId() == id) {
                return book;
            }
        }
        return null;
    }

    public Member findMember(int id) {
        for (Member member : members) {
            if (member.getId() == id) {
                return member;
            }
        }
        return null;
    }

    public void displayBooks() {
        System.out.println("\n--- Library Books ---");

        for (Book book : books) {
            book.displayInfo();
        }
    }

    public void displayMembers() {
        System.out.println("\n--- Library Members ---");

        for (Member member : members) {
            member.displayMember();
        }
    }
}

class BorrowService {

    private Library library;

    public BorrowService(Library library) {
        this.library = library;
    }

    public void borrowBook(int memberId, int bookId) {

        Member member = library.findMember(member);
        Book book = library.findBook(bookId);

        if (member == null) {
            throw new IllegalArgumentException(
                "Member not found"
            );
        }

        if (book == null) {
            throw new IllegalArgumentException(
                "Book not found"
            );
        }

        if (!book.isAvailable()) {
            throw new IllegalStateException(
                "Book is not available"
            );
        }

        book.borrow();
        member.borrowBook(book);

        System.out.println(
            member.getName() +
            " borrowed " +
            book.getTitle()
        );
    }

    public void returnBook(int memberId, int bookId) {

        Member member = library.findMember(memberId);
        Book book = library.findBook(bookId);

        if (member == null || book == null) {
            throw new IllegalArgumentException(
                "Invalid member or book"
            );
        }

        book.returnBook();
        member.returnBook(book);

        System.out.println(
            member.getName() +
            " returned " +
            book.getTitle()
        );
    }
}

class LibraryStatistics {

    private Library library;

    public LibraryStatistics(Library library) {
        this.library = library;
    }

    public void generateReport() {

        System.out.println("\n--- Library Report ---");

        library.displayBooks();
        library.displayMembers();

        System.out.println(
            "Report generated successfully."
        );
    }
}

public class LibraryManagementSystem {

    public static void main(String[] args) {

        Library library = new Library();

        Book book1 = new Book(
            101,
            "Clean Code",
            "Robert Martin"
        );

        Book book2 = new Book(
            102,
            "Effective Java",
            "Joshua Bloch"
        );

        Book book3 = new Book(
            103,
            "Design Patterns",
            "Erich Gamma"
        );

        Book book4 = new Book(
            104,
            "The Pragmatic Programmer",
            "David Thomas"
        );

        library.addBook(book1);
        library.addBook(book2);
        library.addBook(book3);
        library.addBook(book4);

        Member member1 = new Member(
            1,
            "Rahul",
            "rahul@example.com"
        );

        Member member2 = new Member(
            2,
            "Ananya",
            "ananya@example.com"
        );

        library.addMember(member1);
        library.addMember(member2);

        BorrowService borrowService =
            new BorrowService(library);

        borrowService.borrowBook(1, 101);
        borrowService.borrowBook(2, 103);

        borrowService.returnBook(1, 101);

        LibraryStatistics statistics =
            new LibraryStatistics(library);

        statistics.generateReport();
    }
}