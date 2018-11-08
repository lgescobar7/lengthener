
from flask import jsonify, Flask
app = Flask(__name__)

@app.route("/luis")
def hello():
    return jsonify({
        'ghjdhsd': 'jdhkk',
    })


@app.route("/haha")
def bebe():
    return 'pokemon'







# Below is my work associated with the beginners course from skillshare

name = 'Luis\'s'
my_book = "         My favorite part of a girl is her boobs" .replace('boobs','ass') .upper()
print(my_book.strip())


my_town = ("Boston is the greatest\nBut Cali is my\tsoul")
print(my_town .strip())

a= 5
b =6
print(a**b)


#Lists
months= ['january', 'febuary', 'march']
yeet= ["Rebecca linares was born in" +  months[2].title()+   "she was destined to be a ass licker"]
print(yeet)
print(len(months))

#i am excited to see where code can take me in terms of creative creation

for months in months:
    print(months .title()+ 'is the month of the awesome babies' .upper())



numbers= (list(range(1,19)))
print(numbers)


# Here I will practice true false statements with numbers

age = 25
if age != 22:
    print('Nope you are wrong motherfucker')
