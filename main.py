def wordcount(file_contents):
    words = file_contents.split()
    return len(words)

def letters(text):
    character_counts = {}
    for character in text:
        character = character.lower()
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    word_count = wordcount(file_contents)
    print("\nWord Count:")
    print(f"{word_count} words found in the document.")
    char_counts = letters(file_contents)
    print("\nCharacter Counts:")
    for character, count in char_counts.items():
        print(f"The '{character}' character was found {count} times.")
    print("\n--- End of report. ---")

if __name__ == "__main__":
    main()
