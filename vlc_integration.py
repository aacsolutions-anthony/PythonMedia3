import os
import subprocess
import configparser
import shlex
import time
import logging

class VLCPlayer:
    def __init__(self):
        self.process = None
        logging.info("VLCPlayer initiated")

    def _start_process(self, media_path, channel_url):
        # Verify that media_path exists
        if not os.path.exists(media_path):
            logging.error(f"Media path does not exist: {media_path}")
            return

        # Split the VLC output string into parts
        part1 = "#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:rtp{dst="
        part2 = ",port=5004,mux=ts}"
        transcode_options = part1 + channel_url + part2

        # Create the command string
        cmd = f'cvlc {media_path} --sout "{transcode_options}"'
        cmd_list = shlex.split(cmd)
        #Debug print
        print(cmd_list)

        # Start the new process
        try:
            self.process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logging.info("Process started")
        except Exception as e:
            logging.error(f"Failed to start process: {e}")

    def play_media(self, media_path, channel_url):
        if self.process is None or self.process.poll() is not None:
            self._start_process(media_path, channel_url)

    def stop(self):
        if self.process:
            self.process.terminate()

class ChannelManager:
    def __init__(self, player):
        self.player = player
        self.channel_url = self._get_channel_url()

    def _get_channel_url(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        channel_section = config['Channels'] if 'Channels' in config else {}
        # Get first channel URL from config file. If no channel found, return None.
        for channel in channel_section.values():
            return channel
        return None

    def select_channel(self, file_path):
        if not self.channel_url:
            raise ValueError("Channel not found or unavailable")
        self.player.play_media(file_path, self.channel_url)

vlc_player = VLCPlayer()
channel_manager = ChannelManager(vlc_player)

