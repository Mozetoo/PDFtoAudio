import PyPDF3
import boto3

# gets all the info from pdf into string text
with open('Intro.pdf', 'rb') as file:
    reader = PyPDF3.PdfFileReader(file)
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text = page.extractText()
        print("Page", page_num + 1, ":", text)

# Connect with amazon servises polly
polly_client = boto3.client('polly', region_name='us-west-2',
                            aws_access_key_id='ACCESS_KEY_ID',
                            aws_secret_access_key='ACCESS SECRET KEY')

# specify what voice and format i want the speech
response = polly_client.synthesize_speech(Text=text,
                                          OutputFormat='mp3',
                                          VoiceId='Joanna')

# creates the mp3 file on my desktop
file_name = 'output.mp3'
with open(file_name, 'wb') as file:
    file.write(response['AudioStream'].read())
