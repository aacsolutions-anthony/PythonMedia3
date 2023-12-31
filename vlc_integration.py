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
        part1 = '#transcode{acodec=mp3}:rtp{dst='
        part2 = ',port=5004,mux=ts,sap,name=MainVisualStream} --loop'
        transcode_options = part1 + channel_url + part2

        # Create the command string
        cmd = f'cvlc {media_path} --sout "{transcode_options}" --loop'
        cmd_list = shlex.split(cmd)

        # Debug print
        print(f"Running command: {cmd}")

        # Start the new process
        try:
            if self.process:
                self.process.terminate()
                time.sleep(1)  # Give the process time to terminate
                if self.process.poll() is None:  # Process is still running
                    self.process.kill()  # Forcibly end the process
                    time.sleep(1)  # Give the process time to be killed

            self.process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            logging.info("Process started")
            print("Stream started")
        except Exception as e:
            logging.error(f"Failed to start process: {e}")
            print(f"Stream failed to start: {e}")

    def play_media(self, media_path, channel_url):
        # Check if there is an existing process running
        if self.process and self.process.poll() is None:
            # Process is still running, terminate and wait for it to finish
            self.process.terminate()
            time.sleep(1)  # Give the process time to terminate
            if self.process.poll() is None:  # Process is still running
                self.process.kill()  # Forcibly end the process
                time.sleep(1)  # Give the process time to be killed

        self._start_process(media_path, channel_url)

    def stop(self):
        if self.process:
            self.process.terminate()
            time.sleep(1)  # Give the process time to terminate
            if self.process.poll() is None:  # Process is still running
                self.process.kill()  # Forcibly end the process
                time.sleep(1)  # Give the process time to be killed

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
