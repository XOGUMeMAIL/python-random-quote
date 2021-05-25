def frases():
    print("A day of Glory!")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[0])

    
if __name__ == "__frases__":
    frases()
