import os
from flask import Flask, render_template, request, url_for



application = Flask(__name__)


base_dir = os.path.abspath(os.path.dirname(__file__))
wordsfile1 = os.path.join(base_dir, 'static/AliceCleaneredit.txt')
wordsfile2 = os.path.join(base_dir, 'static/AliceInWonderlandedit.txt')
wordsfile3 = os.path.join(base_dir, 'static/CandideEnedit.txt')
wordsfile4 = os.path.join(base_dir, 'static/CandideFredit.txt')


@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/wordsfile', methods=['GET', 'POST'])
def words_file():
    wordsin1 = []
    wordsin2 = []
    wordsin3 = []
    wordsin4 = []
    files = []
    word1 = []
    word2 = []
    word3 = []
    word4 = []

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

    return render_template("words_search.html", file = files)


if __name__ == '__main__':
    application.run()
