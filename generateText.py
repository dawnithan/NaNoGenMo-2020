from gameTitleGenerator import generateTitle, selectPlatforms, selectPrice, selectReviewScore
import markovify
import random

with open("short-descriptions.txt", encoding="utf8") as f:
    text = f.read()

text_model = markovify.Text(text)
games = {}
style = ''

NUM_ELEMENTS = 2500

for i in range(NUM_ELEMENTS):
    games[i] = { 
        "title" : generateTitle(random.randint(0, 7)),
        "tagline" : text_model.make_sentence(tries=100).capitalize(),
        "author" : generateTitle(0),
        "platform" : selectPlatforms(),
        "price": selectPrice(),
        "score": selectReviewScore()
    }

def createGameTemplate(data):
    game_template = "<div class='column'>\n"
    game_template += "\t<div class='row'>\n"
    game_template += "\t<div class='inner_column'></div>\n"
    game_template += "\t<div class='inner_column'>\n"
    game_template += f"\t<div class='review_score {data['score'][1]}'>{data['score'][0]}</div><div class='title highlight'>{data['title']}</div>\n"
    game_template += f"\t<p>{data['tagline']}</p>\n"
    game_template += f"\t<p>By <span class='highlight'>{data['author']}</span></p>\n"
    game_template += f"\t<p>Available for {data['platform']}</p>\n"
    game_template += f"\t<p>{data['price']}</p>\n"
    game_template += "\t</div>\n"
    game_template += "\t</div>\n"
    game_template += "</div>"
    return game_template

def htmltag(tag, content, _class):
    return "<" + tag + _class + ">" + content + "</" + tag + ">"

with open("style.css", "r") as css:
    style = css.read()

with open("output.html", "w", encoding='utf-8') as page:
    page.write("<meta charset='UTF-8'>\n")
    page.write("<style>" + style + "\n</style>\n")
    page.write("<body>\n")    

    elements = []
    for element in games.values():
        template = createGameTemplate(element)
        elements.append(template)

    for i in range(0, len(elements), 2):
        page.write("<div class='row'>\n")
        page.write(elements[i])
        if i + 1 < len(elements): # in case list is odd
            page.write(elements[i + 1]) 
        page.write("</div>\n")
    
    page.write("</body>")