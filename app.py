'''
███████╗██╗      █████╗ ███████╗██╗  ██╗
██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝
█████╗  ██║     ███████║███████╗█████╔╝
██╔══╝  ██║     ██╔══██║╚════██║██╔═██╗
██║     ███████╗██║  ██║███████║██║  ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''
'''
AAC Solutions
Anthony Grace
app.py version 35
ASSUMING ONE CHANNEL

Changes made to the original Flask app:

    Removed the channel-related logic from the content_manager function since the new version of vlc_integration.py assumes that there's only one channel.
    The channel parameter has been removed from the calls to channel_manager.select_channel(), channel_manager.add_to_queue(), and channel_manager.clear_queue().
    channel_manager.get_current_playlists() has been replaced with channel_manager.get_current_playlist(), and the playlists variable has been replaced with playlist.
'''
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
import vlc_integration
import mimetypes


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

vlc_player = vlc_integration.VLCPlayer()
channel_manager = vlc_integration.ChannelManager(vlc_player)

@app.route('/', methods=['GET'])
@app.route('/Home.html', methods=['GET'])
def index():
    return render_template('Home.html')

@app.route('/Upload.html', methods=['POST', 'GET'])
def upload_file():
    if 'file-upload' not in request.files:
        return render_template('Upload.html')
    uploaded_file = request.files['file-upload']
    if uploaded_file.filename == '':
        return render_template('Upload.html')
    mime_type = mimetypes.guess_type(uploaded_file.filename)[0]
    if mime_type not in ['audio/mpeg', 'audio/mp4', 'video/mp4', 'video/x-m4v', 'video/quicktime']:  # For mp3, m4a, mp4, m4v, and mov files
        return "Invalid file type. Please upload an mp3, m4a, mp4, m4v, or mov file.", 400
    filename = secure_filename(uploaded_file.filename)
    try:
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    except Exception as e:
        print("Exception occurred:", e)
        return "File either already exists or is not an mp3, m4a, mp4, m4v, or mov file type.", 400
    return redirect(url_for('content_manager'))  # Redirect to contentmanager.html


@app.route('/Content-Manager.html', methods=['GET', 'POST'])
@app.route('/contentmanager', methods=['GET', 'POST'])
def content_manager():
    if request.method == 'POST':
        file = request.form.get('File-Selection')
        action = request.form.get('action')
        channel = channel_manager._get_channel_url()

        print(channel)

        if not file:
            return jsonify(error="Invalid selection. Please select a file."), 400
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)

        if not os.path.isfile(file_path):
            return jsonify(error="File not found: " + file), 404

        if action == 'Play':
            try:
                channel_manager.select_channel(file_path) #UPDATED from false: vlcplayer.play(filepath)
            except Exception as e:
                return jsonify(error="Error initiating streaming: " + str(e)), 500

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('Content-Manager.html', files=files)

@app.route('/Contact-Us.html', methods=['GET'])
def contact_us():
    return render_template('Contact-Us.html')

if __name__ == '__main__':
    try:
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        app.run(host='0.0.0.0', port=8088, debug=False)
    finally:
        vlc_player.stop()


