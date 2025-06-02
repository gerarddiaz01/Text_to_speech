# Text-to-Speech Script

This project is a Python-based script that processes an article from a URL, extracts its paragraphs, converts them into audio files, and allows the user to listen to them interactively. The goal was to create a dynamic, user-friendly, and well-structured program while handling potential issues like unwanted captions or errors during execution. The first version of this project is in spanish (my main language), then I made another version in english to ensure that all users can understand it.

---

## Learning Context

This was built during my third month of learning Python (April 2025), after completing a series of beginner-level scripting exercises. It marks a step up in using third-party libraries and modular design.

---

## How to Run the Script

1. **Install Dependencies**:
   - Ensure you have Python installed on your machine.
   - Install the required libraries using the following command:
     ```
     pip install newspaper3k gTTS pygame
     ```

2. **Run the Script**:
   - Execute the script by running the following command in your terminal (make sure to be in the right folder):
     ```
     python Text_to_speech.py
     ```

3. **Follow the Prompts**:
   - The script will process the article, generate audio files, and allow you to interactively listen to the paragraphs.

---

## Features

1. **Dynamic Paragraph Processing**:
   - Extracts paragraphs dynamically from an article using `newspaper3k`.
   - Filters out empty lines and unwanted text (like captions) to ensure meaningful content.

2. **Audio File Generation**:
   - Converts each paragraph into an MP3 file using `gTTS`.
   - Avoids regenerating files if they already exist, saving time and resources.

3. **Interactive Audio Playback**:
   - Allows the user to select a paragraph to listen to.
   - Displays the full text of the paragraph in the terminal before playing the audio.

4. **Error Handling**:
   - Handles invalid user input and issues with audio playback gracefully.

5. **Organized Code Structure**:
   - Divided into functions for better readability and maintainability:
     - `process_article`: Extracts and cleans paragraphs from the article.
     - `generate_audio_files`: Converts paragraphs into MP3 files.
     - `play_audio`: Plays the audio files.
     - `display_descriptions`: Displays a list of available paragraphs.
     - `main`: Coordinates the overall flow of the program.

---

## Tools and Libraries Used

1. **`newspaper3k`**:
   - Used to scrape and parse the article's content from a given URL.
   - Extracted the text of the article and split it into paragraphs.

2. **`gTTS`**:
   - Used to convert text into audio files in MP3 format.
   - Specified the language (e.g., `en` for English) to ensure proper pronunciation.

3. **`pygame`**:
   - Used to play the generated MP3 files.
   - Initialized the mixer, loaded the audio file, and played it while ensuring the program waited until the audio finished.

4. **`os`**:
   - Used to check if audio files already existed to avoid regenerating them unnecessarily.

5. **`time`**:
   - Used `time.sleep()` to add delays for better user experience, such as when displaying lists or messages.

---

## Challenges Encountered and Solutions

### Challenge 1: Handling Unwanted Captions
   - **Challenge**: Some paragraphs extracted by `newspaper3k` were captions for images, not actual content.
   - **Solution**: Identified specific captions and either excluded them or labeled them as "captions" in the list of paragraphs.

### Challenge 2: Ensuring Audio Matches Text
   - **Challenge**: Ensuring the text displayed in the terminal matched the audio being played.
   - **Solution**: Used the same list of paragraphs (`parrafos`) for both the text display and audio generation, ensuring consistency.

### Challenge 3: Error Handling for User Input
   - **Challenge**: Users might enter invalid input (e.g., non-numeric values or numbers out of range).
   - **Solution**: Used `try/except` blocks to catch `ValueError` and provided clear error messages, prompting the user to try again.

### Challenge 4: Avoiding Regeneration of Audio Files
   - **Challenge**: Regenerating audio files for every run was inefficient.
   - **Solution**: Used `os.path.exists()` to check if a file already existed before generating it. This saved time and avoided overwriting files.

### Challenge 5: Dynamic Descriptions for Paragraphs
   - **Challenge**: Providing meaningful descriptions for each paragraph, including identifying captions.
   - **Solution**: Created a separate list of descriptions and displayed it to the user, ensuring they could easily identify the content of each paragraph.

### Challenge 6: Managing Audio Playback
   - **Challenge**: Ensuring the program waited until the audio finished playing before proceeding.
   - **Solution**: Used `pygame.mixer.music.get_busy()` in a loop to block further execution until the audio playback was complete.

---

## What I Learned

1. **Using Libraries Effectively**:
   - Deepened understanding of `newspaper3k`, `gTTS`, and `pygame`, learning how to integrate them seamlessly into a project.

2. **Error Handling**:
   - Anticipated and handled potential errors, making the script more robust and user-friendly.

3. **Code Organization**:
   - Divided the script into functions with clear responsibilities, making the code easier to read, debug, and maintain.

4. **User Experience Design**:
   - Added delays, clear prompts, and meaningful descriptions to improve the overall user experience.

5. **Problem-Solving**:
   - Developed creative solutions to challenges, such as identifying and handling captions, ensuring text and audio consistency, and avoiding unnecessary file regeneration.

---

## Conclusion

This project was a great opportunity to apply tools and concepts like loops, conditionals, error handling, and modular programming. By combining multiple libraries and solving real-world challenges, I created a dynamic and interactive script that processes articles, generates audio files, and allows users to engage with the content in a unique way.

This project not only demonstrates technical skills but also highlights the ability to think critically and solve problems effectively. Feel free to explore, use, and contribute to this project!
