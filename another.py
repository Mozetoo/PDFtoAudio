import PyPDF
import  pyttsx3

# gets all the info from pdf into string text
with open('Intro.pdf', 'rb') as file:
    reader = PyPDF3.PdfFileReader(file)
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text = page.extractText()
        print("Page", page_num + 1, ":", text)

engine = pyttsx3.init()

            # Convert the extracted text to speech

engine.save_to_file(text, 'out.mp3')

engine.runAndWait()

