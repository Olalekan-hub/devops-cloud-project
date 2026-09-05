Containerization Approach



I built the Flask app myself since I didn't have an existing one. I used python:3.12-slim as the base image for its light weight, and added requirements.txt so Docker knows to install Flask. I exposed port 5000 and mapped it with -p 5000:5000 so the app is reachable from outside the container.



Challenges Encountered



Notepad auto-appended .txt to my Dockerfile, so Docker couldn't find it. Running dir revealed the issue, and I renamed the file to fix it. Lesson: always verify file names after creating them in Notepad.



How Docker Improves Deployment



Without Docker, my app only worked because of my local environment setup. Inside a container, it runs the same way anywhere Docker is installed solving the "works on my machine" problem and keeping local testing consistent with future cloud deployment.







Deployment Process



For this task, I set up my app to deploy automatically to Azure. I created an Azure Container Registry (ACR) to store my Docker image, and an Azure Web App to actually run it. Then I wrote a GitHub Actions workflow file that runs every time I push code to GitHub. The workflow first checks the code (runs a tool called flake8 to catch style issues), and if that passes, it builds a new Docker image, pushes it to ACR, and restarts the Web App so it picks up the new image. I also had to store some sensitive login details (like my Azure and registry passwords) as GitHub Secrets so the workflow could use them without exposing them publicly.



How CI/CD Improves Delivery



Before this, I would have had to manually rebuild and push my Docker image, then manually restart the app every time I made a change. Now I just push my code to GitHub and everything happens on its own — checking the code, building it, and deploying it. This means fewer chances to forget a step, and I get told quickly if something's broken instead of finding out later.



Challenges Encountered



I ran into a few real problems along the way. My Azure subscription didn't have enough quota for the server size I first tried, so I had to switch to a different region. I also hit a strange Azure CLI bug when logging in that needed a workaround. The trickiest part was actually getting a simple text file (app.py) to end with the right formatting flake8 kept rejecting it for having no newline at the end, then for having an extra blank line, and I had to use PowerShell commands to check the exact bytes in the file to finally get it right. It was frustrating, but it taught me that small formatting details really do matter in real projects, not just "big" mistakes.

