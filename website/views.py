from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Errand
from .import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method == "POST":
        errand = request.form.get('note')
        # comment = request.form.get('comment')
        faculty = request.form.get('faculty')
        institution = request.form.get('institution')
        program = request.form.get('program')
        term = request.form.get('term')
        email = request.form.get('email')
        # level_of_management = request.form.getlist('level_of_management')

        # Perform validation if needed

        if len(errand) < 1:
            flash('Errand is too short!', category='error')
        else:
            new_errand = Errand(data=errand, user_id=current_user.id)
            new_errand.term = term
            new_errand.email = email
            new_errand.faculty = faculty
            new_errand.institution = institution
            new_errand.program = program


            db.session.add(new_errand)
            db.session.commit()
            flash("Errand added!")

    return render_template("home.html", user=current_user)

@views.route('/delete-errand', methods=['POST'])
def delete_errand():
    errand = json.loads(request.data)
    errandId = errand['noteId']
    errand = Errand.query.get(errandId)
    if errand:
        if errand.user_id == current_user.id:
            db.session.delete(errand)
            db.session.commit()

    return jsonify({})



