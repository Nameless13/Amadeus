from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required

from DB.database import db_session
from DB.models import tb_post,tb_user,Kegg_compound
import re

bp = Blueprint('search', __name__)
@bp.route('/')
def index():
    db = db_session
    posts = db.query(
        tb_post.id, tb_post.title, tb_post.body, tb_post.author_id, tb_user.username, tb_post.created
    )
    return render_template('search/index.html', posts=posts)


# def get_post(id, check_author=True):

#     post = db.query(tb_post.id, tb_post.title, tb_post.body, tb_post.author_id, tb_user.username).filter(tb_post.id == id)

#     if post is None:
#         abort(404, "Post id {0} doesn't exist.".format(id))

#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)

#     return post


@bp.route('/', methods=('GET', 'POST'))
def formula_search(formula_weight=None,value_range=1,order_value=Kegg_compound.formula_weight):
    if request.method == 'POST':
        db = db_session
        error = None
        value_range = float(request.form['value_range'])
        if value_range is None:
            value_range = 1
        formula_weights = request.form['formula_weights']
        ###检查数据类型
        formula_weights = re.split(r'[;,\s]\s*', formula_weights)
        # formula_weights = formula_weights.split(',')

        search_results={}
        for formula_weight in formula_weights:
            ffw=float(formula_weight)
            search_result = db.query(Kegg_compound).\
                filter(Kegg_compound.formula_weight > ffw - value_range,\
                Kegg_compound.formula_weight < ffw + value_range).order_by(order_value)
            # 聚合汇总formula_weight    
            search_results.setdefault(formula_weight,search_result)



        if formula_weight is None:
            error = 'Incorrect formula_weight.'

        # if error is None:
        #     session.clear()
        #     session['user_id'] = user['id']
        #     return redirect(url_for('index'))

        # flash(error)

    return render_template('search/index.html',search_results=search_results)


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