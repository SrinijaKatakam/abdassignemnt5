
from flask import Flask, render_template, request, url_for
import os
import string


application = Flask(__name__)


base_dir = os.path.abspath(os.path.dirname(__file__))
wordsfile1 = os.path.join(base_dir, 'static/AliceCleaneredit.txt')
wordsfile2 = os.path.join(base_dir, 'static/AliceInWonderlandedit.txt')
wordsfile3 = os.path.join(base_dir, 'static/CandideEnedit.txt')
wordsfile4 = os.path.join(base_dir, 'static/CandideFredit.txt')
wordsfile5 = os.path.join(base_dir, 'static/CandideEn.txt')
wordsfile6 = os.path.join(base_dir, 'static/CandideFeredit.txt')
wordsfile7 = os.path.join(base_dir, 'static/DonQuijote.txt')
wordsfile8 = os.path.join(base_dir, 'static/Shakespare.txt')


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/wordsfile', methods=['GET', 'POST'])
def words_file():
    wordsin1 = []
    wordsin2 = []
    wordsin3 = []
    wordsin4 = []
    wordsin5 = []
    wordsin6 = []
    wordsin7 = []
    wordsin8 = []
    files = []
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    word5 = []
    word6 = []
    word7 = []
    word8 = []

    if request.method == 'POST':
        word_to_search = request.form.get('search_word')

        with open(wordsfile1, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin1.append(str(words))
        for values in wordsin1:
            word1.append(values[2:-1])

        if word_to_search in word1:
            movie_title1 = "AliceCleaneredit.txt"
            files.append(movie_title1)

        with open(wordsfile2, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin2.append(str(words))

        for values in wordsin2:
            word2.append(values[2:-1])

        if word_to_search in word2:
            movie_title2 = "AliceInWonderlandedit.txt"
            files.append(movie_title2)

        with open(wordsfile3, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin3.append(str(words))

        for values in wordsin3:
            word3.append(values[2:-1])
		
        if word_to_search in word3:
            movie_title3 = "CandideEnedit.txt"
            files.append(movie_title3)

        with open(wordsfile4, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin4.append(str(words))

        for values in wordsin4:
            word4.append(values[2:-1])

        if word_to_search in word4:
            movie_title4 = "CandideFredit.txt"
            files.append(movie_title4)

        with open(wordsfile5, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin5.append(str(words))

        for values in wordsin5:
            word5.append(values[2:-1])

        if word_to_search in word5:
            movie_title5 = "CandideEn.txt"
            files.append(movie_title5)

        with open(wordsfile6, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin6.append(str(words))

        for values in wordsin6:
            word6.append(values[2:-1])

        if word_to_search in word6:
            movie_title6 = "CandideFeredit.txt"
            files.append(movie_title6)

        with open(wordsfile7, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin7.append(str(words))

        for values in wordsin7:
            word7.append(values[2:-1])

        if word_to_search in word7:
            movie_title7 = "DonQuijote.txt"
            files.append(movie_title7)

        
        with open(wordsfile8, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    wordsin8.append(str(words))

        for values in wordsin8:
            word8.append(values[2:-1])

        if word_to_search in word8:
            movie_title8 = "Shakespare.txt"
            files.append(movie_title8)

    return render_template("words_search.html", file = files)

@application.route('/cleanFile', methods=['GET', 'POST'])
def clean_file():
    stopwrds = []
    files = ['static/AliceInWonderland.txt', 'static/CandideFr.txt','static/CandideEn.txt', 'static/DonQuijote.txt', 'static/Shakespeare.txt','static/AliceCleaner.txt']
    with open('static/stopwords.txt', 'rb') as fileinput:
        for line in fileinput:
            for words in line.split():
                stopwrds.append(str(words)[2:-1])

    for filename in files:
        word = []
        with open(filename, 'r', encoding="utf-8-sig") as fileinput:
            for line in fileinput:
                for words in line.split():
                    word.append(words.lower())

        text = " ".join(word)
        edited_txt = []
        text_tokens = text
        print(text_tokens)
        for word in text_tokens.split():
            if word not in stopwrds:
                edited_txt.append(word)

        edited_txt = [''.join(c for c in s if c not in string.punctuation) for s in edited_txt]
        edited_txt = list(filter(None, edited_txt))
        edited_txt = ' '.join(edited_txt)
        data = filename[:-4] + "edit.txt"
        with open(data, "w") as output:
            output.write(str(edited_txt))
    return render_template('clean_data.html')


if __name__ == '__main__':
    application.run()
