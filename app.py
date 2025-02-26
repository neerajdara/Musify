from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Sample music database with multiple songs for each mood and language
music_db = [
    {"title": "Happy Song 1", "artist": "Happy Artist 1", "genre": "Pop", "mood": "happy", "language": "english", "file": "static/audio/happy.mp3"},
    {"title": "Happy Song 2", "artist": "Happy Artist 2", "genre": "Pop", "mood": "happy", "language": "hindi", "file": "static/audio/happy2.mp3"},
    #telugu happy songs
    {"title": "Guche Gulabi", "artist": "Arman Malik, Gopi Sundar", "genre": "Romantic Melody", "mood": "happy", "language": "Telugu", "file": "static/audio/Guche1.mp3"},
    {"title": "Nuvvu", "artist": "Arman Malik, Bheems Ceciroleo", "genre": "Romantic Melody", "mood": "happy", "language": "telugu", "file": "static/audio/Nuvvu1.mp3"},
    # {"title": "Prema Vennela", "artist": "Happy Artist 1", "genre": "Pop", "mood": "happy", "language": "telugu", "file": "static/audio/Prema1.mp3"},
    # {"title": "Naa Roja", "artist": "Happy Artist 1", "genre": "Pop", "mood": "happy", "language": "telugu", "file": "static/audio/Roja1.mp3"},
    #telugu peaceful songs
    {"title": "Sirivennela", "artist": "Anurag Kulkarni, Mickey J. Meyer", "genre": "Soulful Classical", "mood": "peaceful", "language": "Telugu", "file": "static/audio/Sirivennela.mp3"},
    # {"title": "Samajavaragamana", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "peaceful", "language": "telugu", "file": "static/audio/Samajavaragamana.mp3"},
    # {"title": "Undiporaadhey", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "peaceful", "language": "telugu", "file": "static/audio/Undiporaadhey.mp3"},
    {"title": "Nammavemo", "artist": "Karthik, Mani Sharma", "genre": "Romantic Melody", "mood": "peaceful", "language": "Telugu", "file": "static/audio/Nammavemo.mp3"},
    #telugu chill songs
    #{"title": "Jala Jalapatham", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "chill", "language": "telugu", "file": "static/audio/Jala1.mp3"},
    {"title": "Ninnila Ninnila", "artist": "Armaan Malik, Thaman S", "genre": "Romantic Melody", "mood": "chill", "language": "Telugu", "file": "static/audio/Ninnila1.mp3"},
    {"title": "Samayama", "artist": "Kaala Bhairava, Hesham Abdul Wahab", "genre": "Romantic Melody", "mood": "chill", "language": "Telugu", "file": "static/audio/Samayama1.mp3"},
   # {"title": "Manasu Mare", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "chill", "language": "telugu", "file": "static/audio/Manasu1.mp3"},
    #telugu calm songs
    #{"title": "Naanaa Hyraana", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "calm", "language": "telugu", "file": "static/audio/Naanaa1.mp3"},
    #{"title": "Prema Desam", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "calm", "language": "telugu", "file": "static/audio/Premadesham1.mp3"},
    #{"title": "Chandra Kala", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "calm", "language": "telugu", "file": "static/audio/Chandrakala1.mp3"},
    {"title": "Adigaa", "artist": "Sidharth Basrur, Hesham Abdul Wahab", "genre": "Melodious Romantic", "mood": "calm", "language": "Telugu", "file": "static/audio/Adigaa.mp3"},
    #telugu relaxed songs
    {"title": "Inkem Inkem", "artist": "Sid Sriram, Gopi Sundar", "genre": "Romantic Melody", "mood": "relaxed", "language": "Telugu", "file": "static/audio/Inkem1.mp3"},
    # {"title": "Arare Yekkada", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "relaxed", "language": "telugu", "file": "static/audio/Arare1.mp3"},
    # {"title": "Chuttamalle", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "relaxed", "language": "telugu", "file": "static/audio/Chuttamalle1.mp3"},
    # {"title": "Sara Sari", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "relaxed", "language": "telugu", "file": "static/audio/Sara1.mp3"},
    #telugu stressed songs
    # {"title": "Nee Kallalona", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "stressed", "language": "telugu", "file": "static/audio/Neekallalona1.mp3"},
    # {"title": "Naa Kanulu Yepudu", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "stressed", "language": "telugu", "file": "static/audio/Naakanulu1.mp3"},
    {"title": "Kadalalle", "artist": "Sid Sriram, Justin Prabhakaran", "genre": "Romantic Melody", "mood": "stressed", "language": "Telugu", "file": "static/audio/Kadalalle.mp3"},
    #telugu sad songs
    # {"title": "Hilesso Hilessa", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "sad", "language": "telugu", "file": "static/audio/Hilesso1"},
    # {"title": "Srimathi Gaaru", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "sad", "language": "telugu", "file": "static/audio/Srimathi1.mp3"},
     {"title": "Uppenantha", "artist": "KK, DSP", "genre": "Romantic Melody", "mood": "sad", "language": "Telugu", "file": "static/audio/Uppenantha1.mp3"},
    #telugu sleepy songs
    {"title": "Inka Edo", "artist": "KK, G V Prakash", "genre": "Romantic Melody", "mood": "sleepy", "language": "Telugu", "file": "static/audio/Inkaedo1.mp3"},
    #{"title": "Enno Rathrulosthaayi", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "sleepy", "language": "telugu", "file": "static/audio/Enno1.mp3"},
    #telugu angry songs
    # {"title": "Idhe Idhe", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "angry", "language": "telugu", "file": "static/audio/Idhe1.mp3"},
    {"title": "Fear Song", "artist": "Anirudh Ravichander", "genre": "Action", "mood": "angry", "language": "Telugu", "file": "static/audio/Fear.mp3"},
    # {"title": "Ranguladdhukunna", "artist": "Mickey J.Meyer", "genre": "Pop", "mood": "angry", "language": "telugu", "file": "static/audio/Ranguladdhukunna.mp3"},
    #telugu refreshed songs
    {"title": "Sanchari", "artist": "Anirudh Ravichander, Justin Prabhakaran", "genre": "Romantic Melody", "mood": "refreshed", "language": "Telugu", "file": "static/audio/Sanchari.mp3"},
    #hindi happy songs
    {"title": "Deva Deva", "artist": "Arijith Singh, Pritam", "genre": "Devotional", "mood": "happy", "language": "Hindi", "file": "static/audio/Deva.mp3"},
    #hindi calm songs
    {"title": "Satranga", "artist": "Arijith Singh, Shreyas Puranik", "genre": "Melody", "mood": "calm", "language": "Hindi", "file": "static/audio/Satranga.mp3"},
    #hindi peaceful songs
    {"title": "Chahun Main Ya", "artist": "Arijith Singh, Jeet Gannguli", "genre": "Romantic", "mood": "peaceful", "language": "Hindi", "file": "static/audio/Chahun.mp3"},
    #hindi sleepy songs
    {"title": "Aashiqui Aa Gayi", "artist": "Arijith Singh, Mithoon", "genre": "Romantic", "mood": "sleepy", "language": "Hindi", "file": "static/audio/Aashiqui.mp3"},
    #hindi stressed songs
    {"title": "Hua Main", "artist": "Raghav Chaitanya, Pritam", "genre": "Romantic", "mood": "stressed", "language": "Hindi", "file": "static/audio/Hua.mp3"},
    #hindi chill songs
    {"title": "Tauba Tauba", "artist": "Karan Aujla", "genre": "Party", "mood": "chill", "language": "Hindi", "file": "static/audio/Tauba.mp3"},
    #hindi relaxed songs
    {"title": "Namo Namo", "artist": "Amit Trivedi", "genre": "Devotional", "mood": "relaxed", "language": "Hindi", "file": "static/audio/Namo.mp3"},
    #hindi sad songs
    {"title": "Jo Bhi Main", "artist": "Mohith Chauhan, A. R. Rahman", "genre": "Soft Rock", "mood": "sad", "language": "Hindi", "file": "static/audio/Jobhi.mp3"},
    #hindi angry songs
    {"title": "Arjan Vailly", "artist": "Bhupinder Babbal, Manan Bhardwaj", "genre": "Punjabi Folk", "mood": "angry", "language": "Hindi", "file": "static/audio/Arjan.mp3"},
    #malyalam happy songs
    {"title": "Neela Nilave", "artist": "Kapil Kapilan, Sam CS", "genre": "Romantic Melody", "mood": "happy", "language": "Malyalam", "file": "static/audio/Nilave.mp3"},
    #malyalam calm songs
    {"title": "Malare", "artist": "Vineeth Sreenivasan, Rajesh Murugesan", "genre": "Romantic Melody", "mood": "calm", "language": "Malyalam", "file": "static/audio/Malare.mp3"},
    #malyalam peaceful songs
    {"title": "Manasse Manasee", "artist": "Vineeth Sreenivasan, Hesham Abdul Wahad", "genre": "Melody", "mood": "peaceful", "language": "Malyalam", "file": "static/audio/Manasse2.mp3"},
    #malyalam sleepy songs
    {"title": "Uyire", "artist": "Sid Sriram, Ankit Menon", "genre": "Romantic Melody", "mood": "sleepy", "language": "Malyalam", "file": "static/audio/Uyire.mp3"},
    #malyalam stressed songs
    {"title": "Neela Shalabame", "artist": "Jecin George", "genre": "Romantic Melody", "mood": "stressed", "language": "Malyalam", "file": "static/audio/Shalabhame.mp3"},
    #malyalam chill songs
    {"title": "Pottu Thottu Pournami", "artist": "Vineeth Sreenivasan, Aishwarya R.", "genre": "Romantic Melody", "mood": "chill", "language": "Malyalam", "file": "static/audio/Pottu.mp3"},
    #malyalam relaxed songs
    {"title": "Darshana", "artist": "Sreehari K. Nair, Hesham Abdul Wahab", "genre": "Romantic Melody", "mood": "relaxed", "language": "Malyalam", "file": "static/audio/Darshana.mp3"},
    #malyalam sad songs
    {"title": "Parayuvaan", "artist": "Sid Sriram, Jakes Bejoy", "genre": "Romantic Melody", "mood": "sad", "language": "Malyalam", "file": "static/audio/Parayuvaan.mp3"},
    #malayalam refreshed songs
    {"title": "Kiliye", "artist": "Vishnu Vijay, Gopi Sundar", "genre": "Romantic Melody", "mood": "refreshed", "language": "Malyalam", "file": "static/audio/Kiliye.mp3"},
    #english happy songs
    {"title": "Senorita", "artist": "Shawn Mendes, Camila Cabello", "genre": "Latin Pop", "mood": "happy", "language": "English", "file": "static/audio/Senorita.mp3"},
    #english sad songs
    {"title": "Let Me Down Slowly", "artist": "Alec Benjamin", "genre": "Smooth Melody", "mood": "sad", "language": "English", "file": "static/audio/Down.mp3"},
    #english angry songs
    {"title": "Enemy", "artist": "Imagine Dragons X JID", "genre": "Electro Pop", "mood": "angry", "language": "English", "file": "static/audio/Enemy.mp3"},
    #english calm songs
    {"title": "Yummy", "artist": "Justin Biber", "genre": "Hip Hop", "mood": "calm", "language": "English", "file": "static/audio/Yummy.mp3"},
    #english peaceful songs
    {"title": "Baby", "artist": "Justin Biber", "genre": "Teen Pop", "mood": "peaceful", "language": "English", "file": "static/audio/Baby.mp3"},
    #english chill songs
    {"title": "No Lie", "artist": "Dua Lipa, Sean Paul", "genre": "Pop", "mood": "chill", "language": "English", "file": "static/audio/Nolie.mp3"},
    #english refreshed songs
    {"title": "Night Changes", "artist": "One Direction", "genre": "Soft Rock", "mood": "refreshed", "language": "English", "file": "static/audio/Night.mp3"},
    #english relaxed songs
    {"title": "Let Her Go", "artist": "Ed Sheeran", "genre": "Melody", "mood": "relaxed", "language": "English", "file": "static/audio/Letgo.mp3"},
    #english stressed songs
    {"title": "I Wanna Be Yours", "artist": "Arctic Monkeys", "genre": "Garage Rock", "mood": "stressed", "language": "English", "file": "static/audio/Wannabe.mp3"},
    #english sleepy songs
    {"title": "Peaches", "artist": "Justin Biber", "genre": "Pop", "mood": "sleepy", "language": "English", "file": "static/audio/Peaches.mp3"},

]  

# Sample instrumental database with multiple sounds for each mood
instrumental_db = [
    {"title": "Calm Instrumental", "mood": "calm", "file": "static/audio/Satranga.mp3"},
    {"title": "Happy Instrumental", "mood": "happy", "file": "static/audio/happy_instrumental.mp3"},
    {"title": "Sad Instrumental", "mood": "sad", "file": "static/audio/sad_instrumental.mp3"},
    # ...add more instrumental entries...
]
# Sample nature database with multiple sounds for each mood
nature_db = [
    {"title": "Calm Nature Sounds", "mood": "calm", "file": "static/audio/Undiporaadhey.mp3"},
    {"title": "Rainforest Sounds", "mood": "relaxed", "file": "static/audio/nature_rainforest.mp3"},
    {"title": "Ocean Waves", "mood": "peaceful", "file": "static/audio/nature_ocean.mp3"},
    # Add more nature sounds as needed...
]

# Sample ASMR database with multiple sounds for each mood
asmr_db = [
    {"title": "Whispering ASMR", "mood": "calm", "file": "static/audio/asmr_whispering.mp3"},
    {"title": "Tapping ASMR", "mood": "relaxed", "file": "static/audio/asmr_tapping.mp3"},
    {"title": "Crinkling ASMR", "mood": "peaceful", "file": "static/audio/asmr_crinkling.mp3"},
    # Add more ASMR sounds as needed...
]
@app.route('/recommend_nature', methods=['POST'])
def recommend_nature():
    search = request.form.get('search').lower()  # Ensure this matches the form field name

    # Filter nature sounds based on mood
    recommendations = [
        nature for nature in nature_db 
        if nature['mood'] == search or nature['title'].lower() == search
    ]
    
    # Randomly select a nature sound if mood is 'calm', 'relaxed', 'peaceful', etc.
    if search == 'calm':
        calm_nature = [nature for nature in nature_db if nature['mood'] == 'calm']
        if calm_nature:
            sound = random.choice(calm_nature)  # Randomly select a calm nature sound
            recommendations = [sound]  # Return the selected calm nature sound
        else:
            recommendations = []  # No calm nature sounds available

    elif search == 'relaxed':
        relaxed_nature = [nature for nature in nature_db if nature['mood'] == 'relaxed']
        if relaxed_nature:
            sound = random.choice(relaxed_nature)  # Randomly select a relaxed nature sound
            recommendations = [sound]  # Return the selected relaxed nature sound
        else:
            recommendations = []  # No relaxed nature sounds available

    elif search == 'peaceful':
        peaceful_nature = [nature for nature in nature_db if nature['mood'] == 'peaceful']
        if peaceful_nature:
            sound = random.choice(peaceful_nature)  # Randomly select a peaceful nature sound
            recommendations = [sound]  # Return the selected peaceful nature sound
        else:
            recommendations = []  # No peaceful nature sounds available

    # Return recommendations if available
    return jsonify(recommendations)

@app.route('/recommend_asmr', methods=['POST'])
def recommend_asmr():
    search = request.form.get('search').lower()  # Ensure this matches the form field name

    # Filter ASMR sounds based on mood
    recommendations = [
        asmr for asmr in asmr_db 
        if asmr['mood'] == search or asmr['title'].lower() == search
    ]
    
    # Randomly select an ASMR sound if mood is 'calm', 'relaxed', 'peaceful', etc.
    if search == 'calm':
        calm_asmr = [asmr for asmr in asmr_db if asmr['mood'] == 'calm']
        if calm_asmr:
            sound = random.choice(calm_asmr)  # Randomly select a calm ASMR sound
            recommendations = [sound]  # Return the selected calm ASMR sound
        else:
            recommendations = []  # No calm ASMR sounds available

    elif search == 'relaxed':
        relaxed_asmr = [asmr for asmr in asmr_db if asmr['mood'] == 'relaxed']
        if relaxed_asmr:
            sound = random.choice(relaxed_asmr)  # Randomly select a relaxed ASMR sound
            recommendations = [sound]  # Return the selected relaxed ASMR sound
        else:
            recommendations = []  # No relaxed ASMR sounds available

    elif search == 'peaceful':
        peaceful_asmr = [asmr for asmr in asmr_db if asmr['mood'] == 'peaceful']
        if peaceful_asmr:
            sound = random.choice(peaceful_asmr)  # Randomly select a peaceful ASMR sound
            recommendations = [sound]  # Return the selected peaceful ASMR sound
        else:
            recommendations = []  # No peaceful ASMR sounds available

    # Return recommendations if available
    return jsonify(recommendations)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    language = request.form.get('language')
    search = request.form.get('search').lower()

    # Filter songs based on mood and language
    recommendations = [
        music for music in music_db 
        if (music['mood'] == search or music['title'].lower() == search) 
        and music['language'] == language
    ]
    
    # Randomly select a song if mood is 'peaceful', 'happy', 'chill', 'stressed', 'relaxed', 'angry', 'sad', 'calm', 'sleepy', or 'refreshed'
    if search == 'peaceful':
        peaceful_songs = [music for music in music_db if music['mood'] == 'peaceful' and music['language'] == language]
        if peaceful_songs:
            song = random.choice(peaceful_songs)  # Randomly select a peaceful song
            recommendations = [song]  # Return the selected peaceful song
        else:
            recommendations = []  # No peaceful songs available for this language

    elif search == 'happy':
        happy_songs = [music for music in music_db if music['mood'] == 'happy' and music['language'] == language]
        if happy_songs:
            song = random.choice(happy_songs)  # Randomly select a happy song
            recommendations = [song]  # Return the selected happy song
        else:
            recommendations = []  # No happy songs available for this language

    elif search == 'chill':
        chill_songs = [music for music in music_db if music['mood'] == 'chill' and music['language'] == language]
        if chill_songs:
            song = random.choice(chill_songs)  # Randomly select a chill song
            recommendations = [song]  # Return the selected chill song
        else:
            recommendations = []  # No chill songs available for this language

    elif search == 'stressed':
        stressed_songs = [music for music in music_db if music['mood'] == 'stressed' and music['language'] == language]
        if stressed_songs:
            song = random.choice(stressed_songs)  # Randomly select a stressed song
            recommendations = [song]  # Return the selected stressed song
        else:
            recommendations = []  # No stressed songs available for this language

    elif search == 'relaxed':
        relaxed_songs = [music for music in music_db if music['mood'] == 'relaxed' and music['language'] == language]
        if relaxed_songs:
            song = random.choice(relaxed_songs)  # Randomly select a relaxed song
            recommendations = [song]  # Return the selected relaxed song
        else:
            recommendations = []  # No relaxed songs available for this language

    elif search == 'angry':
        angry_songs = [music for music in music_db if music['mood'] == 'angry' and music['language'] == language]
        if angry_songs:
            song = random.choice(angry_songs)  # Randomly select an angry song
            recommendations = [song]  # Return the selected angry song
        else:
            recommendations = []  # No angry songs available for this language

    elif search == 'sad':
        sad_songs = [music for music in music_db if music['mood'] == 'sad' and music['language'] == language]
        if sad_songs:
            song = random.choice(sad_songs)  # Randomly select a sad song
            recommendations = [song]  # Return the selected sad song
        else:
            recommendations = []  # No sad songs available for this language

    elif search == 'calm':
        calm_songs = [music for music in music_db if music['mood'] == 'calm' and music['language'] == language]
        if calm_songs:
            song = random.choice(calm_songs)  # Randomly select a calm song
            recommendations = [song]  # Return the selected calm song
        else:
            recommendations = []  # No calm songs available for this language

    elif search == 'sleepy':
        sleepy_songs = [music for music in music_db if music['mood'] == 'sleepy' and music['language'] == language]
        if sleepy_songs:
            song = random.choice(sleepy_songs)  # Randomly select a sleepy song
            recommendations = [song]  # Return the selected sleepy song
        else:
            recommendations = []  # No sleepy songs available for this language

    elif search == 'refreshed':
        refreshed_songs = [music for music in music_db if music['mood'] == 'refreshed' and music['language'] == language]
        if refreshed_songs:
            song = random.choice(refreshed_songs)  # Randomly select a refreshed song
            recommendations = [song]  # Return the selected refreshed song
        else:
            recommendations = []  # No refreshed songs available for this language

    # Return recommendations if available
    return jsonify(recommendations)

@app.route('/recommend_instrumental', methods=['POST'])
def recommend_instrumental():
    search = request.form.get('search').lower()  # Ensure this matches the form field name

    # Filter instrumental sounds based on mood
    recommendations = [
        instrumental for instrumental in instrumental_db 
        if instrumental['mood'] == search or instrumental['title'].lower() == search
    ]
    
    # Randomly select an instrumental sound if mood is 'calm', 'happy', 'sad', etc.
    if search == 'calm':
        calm_instrumentals = [instrumental for instrumental in instrumental_db if instrumental['mood'] == 'calm']
        if calm_instrumentals:
            song = random.choice(calm_instrumentals)  # Randomly select a calm instrumental
            recommendations = [song]  # Return the selected calm instrumental
        else:
            recommendations = []  # No calm instrumentals available

    elif search == 'happy':
        happy_instrumentals = [instrumental for instrumental in instrumental_db if instrumental['mood'] == 'happy']
        if happy_instrumentals:
            song = random.choice(happy_instrumentals)  # Randomly select a happy instrumental
            recommendations = [song]  # Return the selected happy instrumental
        else:
            recommendations = []  # No happy instrumentals available

    elif search == 'sad':
        sad_instrumentals = [instrumental for instrumental in instrumental_db if instrumental['mood'] == 'sad']
        if sad_instrumentals:
            song = random.choice(sad_instrumentals)  # Randomly select a sad instrumental
            recommendations = [song]  # Return the selected sad instrumental
        else:
            recommendations = []  # No sad instrumentals available

    # Add more conditions for other moods if needed...

    # Return recommendations if available
    return jsonify(recommendations)
if __name__ == '__main__':
    app.run(debug=True)
