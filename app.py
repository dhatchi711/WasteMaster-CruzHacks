from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
import predictor

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOADED_IMAGES_DEST'] = 'uploaded'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)


class MyForm(FlaskForm):
    image = FileField('image')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        filename = images.save(form.image.data)
        resulto = predictor.predict("/Users/kgovid/PycharmProjects/wastemaster/uploaded/" + filename)
        classification = resulto[0]
        print(classification)
        if(classification == 'plastic'):
            return render_template('recycle.html')
        elif(classification == 'cardboard'):
            return render_template('recycle.html')
        elif (classification == 'glass'):
            return render_template('recycle.html')
        elif (classification == 'paper'):
            return render_template('recycle.html')
        elif (classification == 'metal'):
            return render_template('recycle.html')
        elif(classification == 'compost'):
            return render_template('compost.html')
        else:
            return render_template('trash.html')
    return render_template('test.html', form=form)

@app.route('/about')
def about():
    return(render_template('about.html'))

