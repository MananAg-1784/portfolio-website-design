
from flask import Blueprint, render_template, redirect, url_for, send_file, current_app

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
    return render_template('index.html', url='projects')

@main.route('/about')
def about_page():
    return render_template('about.html', url='about')

@main.route('/resume')
def resume_page():
    path = current_app.static_folder + '/resume.pdf'
    return send_file(path, as_attachment=True)

@main.app_errorhandler(404)
def errorrr(e):
    return "URL NOT FOUND"