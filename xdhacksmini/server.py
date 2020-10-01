from flask import Flask, render_template

app = Flask(__name__)

conn=sqlite3.connect('twitter.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title text, subtitle text, author text, content text''')
conn.commit()
conn.close()

@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == 'GET':
		posts = get_posts()
	else:
		posts = [title = 'hi',subtitle = 'subtitle', author = 'author', content = ' hjgjskreaopigsjnfkdmeoirsgufjbkgop']
	return render_template('home.html', title=title, subtitle=subtitle, author=author, content=content)

if __name__ == "__main__":
	app.run()
