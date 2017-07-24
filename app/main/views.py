from flask import render_template, redirect, url_for
from . import main
from . forms import AwardForm


@main.route('/', methods=['GET', 'POST'])
def index():

    form = AwardForm()

    if form.validate_on_submit():
        return redirect(url_for('main.index'))

    return render_template("index.html", form=form)
