from flask import Flask, render_template, jsonify, send_from_directory, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
VIDEOS_DIRECTORY = os.path.join(app.static_folder, 'videos')
app.secret_key = 'dafdsa2fda345sfdsaafd34sfdsa'

HARDCODED_PASSWORD = 'MyNameIsNotRick!'

@app.route('/')
def index():
    if not session.get('authenticated'):
        return redirect(url_for('enter_password'))  # Redirect to password prompt if not authenticated
    videos = ['IMG_3241.mp4','IMG_3242.mp4','IMG_3250.mp4']
    return render_template('home.html',videos=videos)

@app.route('/dates')
def list_dates():

    dates = next(os.walk(VIDEOS_DIRECTORY))[1]  # Get the list of directories only
    return jsonify(dates)

@app.route('/videos/<date>')
def list_videos(date):
    videos = os.listdir(os.path.join(VIDEOS_DIRECTORY, date))
    return jsonify(videos)

@app.route('/video/<date>/<filename>')
def stream_video(date, filename):
    return send_from_directory(os.path.join(VIDEOS_DIRECTORY, date), filename)

@app.route('/enter_password', methods=['GET'])
def enter_password():
    return render_template('password_prompt.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form['password']
    if password == HARDCODED_PASSWORD:
        session['authenticated'] = True  # Set the session as authenticated
        return redirect(url_for('index'))  # Redirect to the main page if the password is correct
    else:
        flash('Incorrect password!')  # Send an error message
        return redirect(url_for('enter_password'))  # Redirect back to the password entry page


if __name__ == '__main__':
    app.run(debug=True)