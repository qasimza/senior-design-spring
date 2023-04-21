# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.authentication.forms import PerformSearchFrom
from .ml_code.recommend import recommend_songs

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index') 


@blueprint.route('/<template>',  methods=['GET', 'POST'])
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        if 'search' in segment:
            print("Search Form, ", request.form)
            search_form = PerformSearchFrom(request.form)

            if 'search' in request.form:
                # read form data
                explicit = request.form['explicit'] if 'explicit' in request.form else 'n'
                form_data = request.form.to_dict(flat=False)
                form_data['explicit']=[explicit]
                recommended_songs = recommend_songs(form_data)
                print(recommended_songs)
                try:
                    return render_template('home/results.html', recommended_songs=recommended_songs)
                except Exception as e:
                    print(e)

            # Something (user or pass) is not ok
            print("Not OK")
            return render_template('home/search.html',
                    msg='Incorrect Input',
                    form=search_form) 

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
