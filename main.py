with open("text.txt", mode="rt", encoding="utf-8") as text:
    uppertext = text.readline().upper()

with open("film.txt", mode="x", encoding="utf-8") as data:
    data.write(uppertext)
