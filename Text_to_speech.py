import os
from newspaper import Article
from gtts import gTTS
import pygame
import time

def process_article(url):
    '''
    Downloads and processes the content of an article from a URL.

    Parameters:
    url (str): The URL of the article to process.

    Returns:
    list: A list of paragraphs extracted from the article text.
    '''
    article = Article(url)
    article.download()
    article.parse()
    return [paragraph.strip() for paragraph in article.text.split("\n") if paragraph.strip()]

def generate_audio_files(paragraphs):
    '''
    Converts paragraphs of text into MP3 audio files.

    Parameters:
    paragraphs (list): List of text paragraphs to convert into audio.

    Returns:
    int: The total number of audio files generated.
    '''
    counter = 1
    for paragraph in paragraphs:
        if paragraph.strip():
            filename = f"paragraph_{counter}.mp3"
            if not os.path.exists(filename):
                tts = gTTS(paragraph, lang="en")
                tts.save(filename)
                print(f"Paragraph {counter} has been saved as '{filename}'")
            else:
                print(f"The file '{filename}' already exists. It will not be regenerated.")
            counter += 1
    return counter - 1  # Returns the total number of paragraphs generated

def play_audio(filename):
    '''
    Plays an MP3 audio file.

    Parameters:
    filename (str): The name of the audio file to play.

    Returns:
    None
    '''
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Error playing the file: {e}")
    finally:
        pygame.mixer.quit()

def display_descriptions(descriptions):
    '''
    Displays a numbered list of available paragraphs, indicating if any is a caption.

    Parameters:
    descriptions (list): List of paragraph descriptions.

    Returns:
    None
    '''
    print("\nAvailable paragraphs:")
    for description in descriptions:
        print(description)
        time.sleep(0.5)

def main():
    '''
    Main function that coordinates the downloading, processing, audio generation,
    and playback of paragraphs from an article.

    Returns:
    None
    '''
    # URL of the article
    url = "https://www.dailymail.co.uk/sciencetech/article-14680515/Sacred-pyramid-built-forgotten-civilization-Amazon-rainforest-worlds-tallest-ancient-structure.html"
    
    print("Processing the article...")
    paragraphs = process_article(url)
    
    if not paragraphs or all(not p.strip() for p in paragraphs):
        print("The article does not contain valid text to process.")
        return

    total_paragraphs = generate_audio_files(paragraphs)
    print("\nThe article has been processed and divided into paragraphs.")
    time.sleep(1)

    # List of paragraph descriptions
    descriptions = [
        "1. Paragraph 1: Amazonian peak may be world’s largest ancient pyramid.",
        "2. Paragraph 2: Cerro El Cono’s shape and isolation fuel mystery.",
        "3. Paragraph 3: Located in Peru’s Sierra del Divisor National Park.",
        "4. Paragraph 4: Unnatural flat faces suggest man-made structure.",
        "5. Paragraph 5: It stands out dramatically from flat rainforest.",
        "6. Paragraph 6: Locals revere it as a sacred mountain spirit.",
        "7. Paragraph 7: Pre-Inca legends suggest a deeper ancient origin.",
        "8. Paragraph 8: Local myths claim it hides an ancient pyramid.",
        "9. Caption: Description of a photo from the article.",
        "10. Caption: Description of a photo from the article.",
        "11. Paragraph 11: Fringe researchers believe it is man-made.",
        "12. Paragraph 12: If true, it would surpass all known pyramids.",
        "13. Paragraph 13: Three times taller than any ancient structure.",
        "14. Paragraph 14: Might join list of mysterious ancient monuments.",
        "15. Paragraph 15: Gunung Padang: possibly the oldest pyramid.",
        "16. Paragraph 16: Ancient megalith dates back 16,000 years.",
        "17. Paragraph 17: 2023 research challenges idea of “primitive” societies.",
        "18. Caption: Description of a photo from the article.",
        "19. Caption: Description of a photo from the article.",
        "20. Paragraph 20: Yonaguni monument: pyramid-like, undersea structure.",
        "21. Paragraph 21: Discovered in 1986, estimated at 12,000 years old.",
        "22. Paragraph 22: Cerro El Cono would still be tallest if man-made.",
        "23. Paragraph 23: Scientists suggest it’s an extinct volcano.",
        "24. Caption: Description of a photo from the article.",
        "25. Paragraph 25: Could be volcanic cone, plug, or intrusion.",
        "26. Paragraph 26: Volcanic cone: built from eruptive debris.",
        "27. Paragraph 27: Volcanic plug: solidified magma inside a vent.",
        "28. Paragraph 28: Erosion exposes hard plug as a hill or peak.",
        "29. Paragraph 29: Intrusion: underground magma that hardened.",
        "30. Paragraph 30: What happens when erosion gets exposed.",
        "31. Paragraph 31: Unique among Amazon formations.",
        "32. Paragraph 32: Can be seen from over 250 miles away."
    ]

    response = input("Would you like to listen to the generated audios? (yes/no): ").strip().lower()
    if response not in ["yes", "y"]:
        print("\nThank you for using the program!")
        return

    display_descriptions(descriptions)

    # Loop to allow the user to listen to multiple audios
    while True:
        try:
            selection = int(input("\nSelect the number of the paragraph you want to listen to (1-32): "))
            if 1 <= selection <= total_paragraphs:
                filename = f"paragraph_{selection}.mp3"
                if os.path.exists(filename):
                    # Display the content of the paragraph in the terminal
                    print(f"\nPlaying paragraph {selection}...")
                    print(f"Content of paragraph {selection}:")
                    print(paragraphs[selection - 1])  # Display the corresponding paragraph
                    play_audio(filename)
                else:
                    print(f"The file '{filename}' does not exist. Please select another paragraph.")
            else:
                print("Please select a valid number between 1 and 32.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 32.")

        # Ask if the user wants to listen to another audio or exit
        continue_response = input("\nWould you like to listen to another paragraph? (yes/no): ").strip().lower()
        if continue_response not in ["yes", "y"]:
            print("\nThank you for using the program! Goodbye.")
            break

# Run the program
if __name__ == "__main__":
    main()