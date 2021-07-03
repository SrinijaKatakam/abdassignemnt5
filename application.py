
from flask import Flask, render_template, request, url_for
import os
import string


application = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
words1 = os.path.join(basedir, 'static/AliceCleaneredit.txt')
words2 = os.path.join(basedir, 'static/AliceInWonderlandedit.txt')
words3 = os.path.join(basedir, 'static/CandideEnedit.txt')
words4 = os.path.join(basedir, 'static/CandideFredit.txt')
words5 = os.path.join(basedir, 'static/DonQuijote.txt')
words6 = os.path.join(basedir, 'static/Shakespeare.txt')

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@application.route('/wordsfile', methods=['GET', 'POST'])
def words_file():
    word1 = []
    word2 = []
    word3 = []
    word4 = []
    word5 = []
    word6 = []
    files = []
    line_num = []
    line_data = []
    wordss1 = []
    wordss2 = []
    wordss3 = []
    wordss4 = []
    wordss5 = []
    wordss6 = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0

    counts1 = 0
    counts2 = 0
    counts3 = 0
    counts4 = 0
    counts5 = 0
    counts6 = 0

    if request.method == 'POST':
        query_word = request.form.get('words')

        with open(words1, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word1.append(str(words))
        for values in word1:
            wordss1.append(values[2:-1])


        if query_word in wordss1:
            movie_title1 = "AliceCleaneredit.txt"
            files.append(movie_title1)

            with open(words1, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts1 = count1
                            break
                        else:
                            count1 = count1 + 1
                    break
                line_num.append(counts1)

        with open(words2, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word2.append(str(words))

        for values in word2:
            wordss2.append(values[2:-1])


        if query_word in wordss2:
            movie_title2 = "AliceInWonderlandedit.txt"
            files.append(movie_title2)

            with open(words2, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts2 = count2
                            break
                        else:
                            count2 = count2 + 1
                    break
                line_num.append(counts2)

        with open(words3, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word3.append(str(words))

        for values in word3:
            wordss3.append(values[2:-1])


        if query_word in wordss3:
            movie_title3 = "CandideEnedit.txt"
            files.append(movie_title3)

            with open(words3, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts3 = count3
                            break
                        else:
                            count3 = count3 + 1
                    break
                line_num.append(counts3)

        with open(words4, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word4.append(str(words))

        for values in word4:
            wordss4.append(values[2:-1])


        if query_word in wordss4:
            movie_title4 = "CandideFredit.txt"
            files.append(movie_title4)

            with open(words4, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts4 = count4
                            break
                        else:
                            count4 = count4 + 1
                    break
                line_num.append(counts4)

        with open(words5, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word5.append(str(words))

        for values in word5:
            wordss5.append(values[2:-1])


        if query_word in wordss5:
            movie_title5 = "AliceInWonderlandedit.txt"
            files.append(movie_title5)

            with open(words5, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts5 = count5
                            break
                        else:
                            count5 = count5 + 1
                    break
                line_num.append(counts5)

        with open(words6, 'rb') as fileinput:
            for line in fileinput:
                for words in line.split():
                    word6.append(str(words))

        for values in word6:
            wordss6.append(values[2:-1])


        if query_word in wordss6:
            movie_title6 = "AliceInWonderlandedit.txt"
            files.append(movie_title6)

            with open(words6, 'rb') as filesinput:
                for line in filesinput:
                    for words in line.split():
                        if query_word == str(words)[2:-1]:
                            counts6 = count6
                            break
                        else:
                            count6 = count6 + 1
                    break
                line_num.append(counts6)

    return render_template("words_search.html", file = files, lines = line_num)

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
