***Non production ready*** 
***Currently in testing (passed all below devel stages***
---
## Devel Stages: 

1. Wrap in gunicorn (complete)
2. Put gunicorn in container (complete)
3. Debug container (complete)
4. Create an nginx docker container pointing to gunicorn (complete)
5. possibly configure gunicorn to listen to single IP (nginx) or use the standard UNIX sockets.
- 5000
- (complete)

> Remember to update the server_name directive in the Nginx configuration file with your actual domain name for a production deployment. You would also likely want to configure Nginx to serve static files directly, among other optimizations.

---

# PythonMedia3

![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/2c1576a8-e769-4d82-9547-1596494ecd61)


Open Development Branch. (GPL3.0)

This software is:

>*modular, secure, open* - From its foundation.

PythonMedia3 is a powerful Python-based media streaming application. It provides a streamlined, user-friendly interface for managing and streaming media content. The system is built to operate smoothly across different platforms, providing a universal solution to your media streaming needs.

>New build containing imrpoved front end and rigidity, fixing daemon bugs from second build and process piping issues causing streams to not initialize on some machines.

## Table of contents:
1. [Features](#features)
2. [Dependencies](#python-dependencies)
3. [System Dependencies](#system-dependencies)
4. [How It works](#howitWorks)
5. [Conclusion](#conclusion)
6. [Download Contents](#download)
7. [Install Docker App](#dockerinstall)
8. [Install Project with Docker](#projectinstall)
9. [Install project with Git (Alternative)](#standaloneinstall)
10. [Automated Install Method (Alternative)](#automatedinstall) 
11. [Usage](#usage)
12. [Troubleshooting](#troubleshooting)
13. [Legal Disclosure](#legal)
14. [Warranty and License](#warranty)


## Features <a name="features"> </a>

1. Media Uploading: Users can upload their media files to the application. The uploaded files are securely stored in an 'uploads' directory.

2. Content Management: PythonMedia2 allows users to manage their media content efficiently. The users can select a channel and a file for streaming.

3. VLC Integration: The system leverages the power of VLC, a versatile media player, to handle the media streaming. The application transcodes the media into the H.264 video codec and the MPEG audio codec, which are then streamed via RTP.

4. Channel Management: The application supports multiple channels, allowing users to stream different media on different channels simultaneously.

5. Error Handling: PythonMedia2 is designed to handle errors gracefully. If a user tries to select an invalid channel or a non-existent file, the system responds with an appropriate error message.

6. Docker Support: For ease of deployment, the application comes with Docker support. Users can quickly get the system up and running using Docker containers, which ensure consistent behavior across different platforms.

---

![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/9b0c2269-a5ac-43fc-8c95-7060697d2981)
![image](https://github.com/aacsolutions-anthony/PythonMedia2/assets/131961269/59d02746-8911-402a-809b-9bae1f4685ee)
![image](https://github.com/aacsolutions-anthony/PythonMedia3/assets/131961269/d5eac9b9-d018-4fbd-811a-ce78f08e3255)


---

## Python Dependencies <a name ="python-dependencies"> </a>


PythonMedia3 relies on several Python libraries to function:

1. Flask: A lightweight web application framework.

2. Jinja2: A modern and designer-friendly templating language for Python.

3. Werkzeug: A comprehensive WSGI web application library.

4. Gunicorn: WSGI Web server wrapper


## System Dependencies <a name="system-dependencies"> </a>


In addition, the application uses VLC for media streaming, so you must have VLC installed on your system to use PythonMedia2.

1. VLC / CVLC - CVLC command interface the the shell

2. 1GBe connection for streaming

3. 10GB spare disk space

4. 16GB total system memory

5. Python

6. BASH

7. Docker

8. Git / Github


## How It Works <a name="howitWorks"> </a>

PythonMedia3 uses the Flask framework to serve a web interface where users can upload their media files and manage their channels. The uploaded media files are stored in an 'uploads' directory.

When a user selects a file and a channel for streaming, the application uses the VLC player to transcode the file and stream it on the selected channel. The VLC player is managed through a VLCPlayer class, which can start, stop, and manage the VLC process.

The channels are managed through a ChannelManager class. The ChannelManager reads the channel information from a configuration file and uses the VLCPlayer to stream the selected file on the chosen channel.
Future Improvements

While PythonMedia3 is a fully functional media streaming application, there's always room for improvement.
Here are a few enhancements that could be made in the future:

1. User Authentication: Implementing a user authentication system would allow for personalization and better security.
2. Media Library: Creating a media library interface would provide users with a better overview of their uploaded files.
3. Expanded Codec Support: While PythonMedia2 currently supports H.264 video and MPEG audio, supporting more codecs would make the system more versatile.
4. REACT JS Support : Strengthening the python app by rewriting it in React and JS.
5. Queue and playlist system: Adding a queue system to setup a queue or playlists so media files could be added in succession for a longer playout and less management.

## Conclusion <a name="conclusion"> </a>

PythonMedia3 is a capable media streaming application that provides a straightforward way for users to stream their media content in a lightweight and streamlined environment.


# Download Project contents: <a name="download"> </a>

1. Clone the project Repository: Open a terminal, navigate to the location where you'd like to store your project, and clone your repository using the command:
**OR**
2. Head to releases page to download the latest release of the project and follow the docker install method.  

## Install Git

*The Prefered Method is Modifiable to suit your usual package manager

### Windows 

```
winget install git.git
```

### Ubuntu & GNU/Linuc

```
sudo apt update -y && install git 
```

## Project contents Git Clone: (main branch possibly broken, see releases page) 

*powershell or bash*

```
git clone https://github.com/aacsolutions-anthony/PythonMedia3.git
```

Download Docker Desktop for Windows from the official Docker website. Double-click the Docker Desktop Installer to run the installer. It's a straightforward wizard - just keep clicking "Next" until the installation is complete.

# Install Docker <a name="dockerinstall"> </a>

Windows
```
winget install Docker.DockerDesktop
```
GNU
```
apt-get update -y && install docker
```
Arch 
```
sudo pacman -S docker
```

# Install main project

PythonMedia3 is a Python-based application for media streaming. This section provides comprehensive instructions on installing the application with Docker.

## Prerequisites:

1. Ensure you have either Docker or Git installed on your system.
2. If you're installing as a standalone app, make sure you have Python 3 and VLC installed.

*standalone not recommended for any WINDOWS OS as this is untested and the app is not built with that in mind*

## Installation with Docker: <a name="projectinstall"> </a>

### Follow these steps to install PythonMedia2 using Docker.

**Works on all systems**

1. Install docker *(see above)*
2. Download latest release on the releases page. 
3. Run below commands in the root of the project:
  
```
docker-compose up --build 
```

3. Server should be accessible via ip address and port designation (see below)

**The PythonMedia3 application is now running and accessible at:**

3.1. http://localhost:44444

3.2. https://localhost:44445

*External:*

3.4. http://ServerIP:4444

3.5. https://ServerIP:44445
   
5. When you are finished with running the server or are taking it down for maintainence, hit ctrl+C twice then run

```
docker-compose down 
```


## Usage: <a name="usage"> </a>

Accessible in the web UI of your ***local IP address*** followed by port 44444 for HTTP or port 44445 for HTTPS

## Find your internal IP:

### Windows

Open Command Prompt or PowerShell and enter command:

```
ipconfig
```
Find your interface and the link/local ipv4 address.

### Ubuntu & GNU/Linux

Open a console / terminal:

systemD
```
ip a
```
or standard: 
```
ifconfig
```


### Example URL:
protocol://IPaddress:port

http://192.168.1.157:44444
https://192.168.1.157:44445

After starting the PythonMedia3 application, you can access it through your web browser at http://localhost:8088. From there, you can upload media files, manage content, and start streaming.

Remember to add a config.ini file to the project directory if there isnt one already. This file is needed by the application to function properly. Please refer to the vlc_integration.py file for more details on how to set up this file.


## Troubleshooting: <a name="troubleshooting"> </a>

If you encounter any problems during the installation or use of PythonMedia3, please open an issue in the GitHub repository.

Under open dev build, the client is permitted to edit the software to debug mode as specified in the app.py file.

Though this is not recommended by clients and should be hanndled by AAC Solutons technical support through a VPN/ SSH.

Enjoy using PythonMedia3!


# LEGAL PARAMETERS <a name="legal"> </a>

PythonMedia3 Copyright (C) 2023  Anthony Grace @ AAC Solutions

https://www.aacsolutions.com.au/

This program comes with ABSOLUTELY NO WARRANTY;
This initial build is free software, and you are welcome to redistribute it
under certain conditions.

## Licensing

See LICENSE in the root of the main branch.

GPL 3.0 Licence.

No Warranty, No liability, Open use and modification under full disclosure.


## Warranty <a name="warranty"> </a>
This software comes with absolutely no warranty.

In selected environments and client deployments, remote support is available and issues can be posted via the issues section in Git towards the main branch.

PythonMedia3 by AAC Solutions / Australia - Copyright: (C) 2023 / *Anthony Grace*
Providing a modular, open, and secure streaming solution for AAC Solutions Clients

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.


Patch and update branches should not and will not be deployed to client systems.

Issues can also be emailed for remote fixes for select clients. Exclusions apply.

## Exclusion
It should be noted that the developer, development company shall not be held liable for the content which is streamed using this software.
The developer holds no warranty or copyright claims over the streamed content or content uploaded by the clients, users, and stakeholders.

## Side notes on operating system environment
For the sake of the argument: All references to GNU / Linux and Ubuntu declares that; GNU/Linux and Ubuntu based systems are recommended for this install. 
Developer note !!: 
> Any Linux distribution which adopts LTS, FOSS-builds,and Stable release models. 
> APT pakage manager recommened as build and install scripts are ased around this. 
