Containerization Approach



I built the Flask app myself since I didn't have an existing one. I used python:3.12-slim as the base image for its light weight, and added requirements.txt so Docker knows to install Flask. I exposed port 5000 and mapped it with -p 5000:5000 so the app is reachable from outside the container.



Challenges Encountered



Notepad auto-appended .txt to my Dockerfile, so Docker couldn't find it. Running dir revealed the issue, and I renamed the file to fix it. Lesson: always verify file names after creating them in Notepad.



How Docker Improves Deployment



Without Docker, my app only worked because of my local environment setup. Inside a container, it runs the same way anywhere Docker is installed solving the "works on my machine" problem and keeping local testing consistent with future cloud deployment.

