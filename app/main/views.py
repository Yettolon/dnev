import datetime
from flask import render_template, redirect, url_for, current_app, abort
from flask_login import current_user, login_required
from sqlalchemy import desc

from . import main
from .forms import RecordForm
from .. import db
from ..models import RecordView


@main.route('/', methods=['GET','POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.user', 
                username=current_user.username))
    return render_template('index.html')

@main.route('/user/<username>/page/<int:page>')
@main.route('/user/<username>', methods=['GET'])
@login_required
def user(username, page=1):
    if current_user.username != username:
        abort(403)
    pagination = RecordView.query.order_by(desc(RecordView.data_pub)).filter_by(
        author_id=current_user.id).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out = False
    )
    if pagination.items == []:
        page=1
    elif pagination.pages < page:
        abort(404)
    print(pagination.pages)
    rec = pagination.items
    return render_template('user.html', rec=rec, pagination=pagination)

@main.route('/user/<username>/<int:id>', methods=['GET','POST'])
@login_required
def record_edit(username, id):
    if current_user.username != username:
        abort(403)
    rec = RecordView.query.get_or_404(id)
    form = RecordForm(title=rec.title, text=rec.text)
    if form.validate_on_submit:
        rec.title = form.title.data
        rec.text = form.text.data
        db.session.add(rec)
        db.session.commit()
    
    return render_template('rec_edit.html', form=form)


@main.route('/user/new_record', methods=['GET','POST'])
@login_required
def new_record():
    form = RecordForm()
    if form.validate_on_submit():
        record = RecordView(author_id=current_user.id,
                            title=form.title.data,
                            text=form.text.data,
                            data_pub=datetime.date.today())
        db.session.add(record)
        db.session.commit()
        return redirect(url_for('main.user', username=current_user.username))
    return render_template('new_record.html', form=form)

