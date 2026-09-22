me = "CALL THIS ON IMPORT"
# When name.py is run directly it prints "SOMETHING ELSE LOL" when run from a different file it prints "CALL THIS..."

if __name__ == "__main__":
    me = "SOMETHING ELSE LOL"
    print(me)
