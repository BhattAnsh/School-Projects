import spacy

# Load the 'en_core_web_sm' model
nlp = spacy.load('en_core_web_sm')

# Define the text to analyze
text = "I am feeling very happy today and romantic also so can u suggest me some movies"

# Process the text with spaCy
doc = nlp(text)

# Define a list of moods
moods = ["Happiness", "Sadness", "Anger", "Fear", "Excitement", "Calmness", "Contentment", "Boredom", "Anxiety", "Depression","Envy","Gratitude","Guilt","Loneliness","Nostalgia","Hope","Confusion","Embarrassment","Elation","Melancholy","Frustration","Love","Calm","Serenity","Surprise"]

# Iterate over the tokens in the text
for token in doc:
    # Check if the token is a mood
    if token.text.lower() in moods:
        print("Mood detected:", token.text)
print(doc)
