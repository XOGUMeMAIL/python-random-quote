def main():
    print("A day of Glory!");

    f = open("quotes.txt");
    quotes = f.readlines();
    f.close();

    print(quotes);

if __name__ == "__main__":
    main();
