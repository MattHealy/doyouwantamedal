from flask import render_template, send_file
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
        fp = cert.generate(name, award)

        cert.store(name, award)

        return(send_file(filename_or_fp=fp, mimetype="image/jpg",
                         as_attachment=True,
                         attachment_filename='certificate-{}.jpg'
                         .format(name)))

    return render_template("index.html", form=form)
