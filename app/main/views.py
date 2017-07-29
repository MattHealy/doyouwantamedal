from flask import render_template, redirect, url_for
from . import main
from . forms import AwardForm
from .. generator import Certificate


@main.route('/', methods=['GET', 'POST'])
def index():

    form = AwardForm()

    if form.validate_on_submit():

        name = form.name.data.strip()
        award = form.award.data.strip()

        cert = Certificate()
        cert.generate(name, award)

        return redirect(url_for('main.index'))

    return render_template("index.html", form=form)
