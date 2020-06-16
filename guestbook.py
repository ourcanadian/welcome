import json

def main():
    guestbook = open('./guestbook.json')
    entries = json.load(guestbook)

    for entry in entries:
        print(entry['name'], "was here on ", entry['date'])

if __name__ == "__main__":
    main()