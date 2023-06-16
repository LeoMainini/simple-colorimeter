from flask import Flask, request, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_bootstrap import Bootstrap
import colorgram
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "dfkbkjbdsfkjbjkbkjb"
Bootstrap(app)


class FileForm(FlaskForm):
	file = FileField('File', validators=[DataRequired()])
	submit = SubmitField('Upload')


def extract_pallete(img):
	try:
		colors = colorgram.extract(img, 9)
	except:
		colors = 0
	return colors


@app.route("/", methods=["GET","POST"])
def home():
	form = FileForm()
	
	if form.validate_on_submit():
		print(form.data)
		color_data = extract_pallete(form.file.data)
		if (color_data == 0):
			return render_template("index.html", form=form)
		color_list=[color.rgb for color in color_data]
		pct_list = [f"{round(color.proportion*100,2)}%" for color in color_data]
		return render_template("index.html", form=form, colors=color_list, pct = pct_list)
	return render_template("index.html", form=form)








if __name__ == "__main__":
	app.run(debug=True)