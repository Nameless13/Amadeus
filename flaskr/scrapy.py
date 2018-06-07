from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required

from DB.database import db_session
from DB.models import tb_post,tb_user,Proxy
import re

bp = Blueprint('scrapy', __name__)
@bp.route('/')
def index():
    db = db_session
    posts = db.query(
        tb_post.id, tb_post.title, tb_post.body, tb_post.author_id, tb_user.username, tb_post.created
    )
    return render_template('scrapy/index.html', posts=posts)



@bp.route('/', methods=('GET', 'POST'))
def formula_scrapy(area=None,order_value=Proxy.area):
    if request.method == 'POST':
        db = db_session
        error = None
        ###检查数据类型(undo)

        scrapy_result = db.query(Proxy).order_by(order_value)

        if scrapy_result is None:
            error = 'Incorrect scrapy_result.'

        # if error is None:
        #     session.clear()
        #     session['user_id'] = user['id']
        #     return redirect(url_for('index'))

        # flash(error)

    return render_template('scrapy/index.html',scrapy_results=scrapy_results)


'''
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
'''