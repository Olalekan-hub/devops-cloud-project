What I Learned About DevOps



Before this project, I thought DevOps was mostly about writing code. It's actually more about everything that happens around the code — how it gets stored, tested, built, deployed, and watched once it's running. I learned that a lot of the work is setting things up once so they run automatically afterwards, and that small details (a file extension, a missing newline, a required tag) can block an entire deployment. I also saw how much of it is troubleshooting rather than building — most of my time went into reading error messages and figuring out what they were actually telling me.



How Automation Improves Software Delivery



Once the pipeline was set up, I stopped doing things manually. I push my code, and the checks, the build, and the deployment all happen on their own. This means I'm less likely to forget a step or deploy something broken, since the pipeline stops if the code fails its checks. Adding health checks and auto-restart also means the app can recover on its own if something goes wrong, without me needing to be watching it.



Improvements I Would Make With More Time



I would add proper automated tests instead of just a lint check, since right now the pipeline only checks code style, not whether the app actually works correctly. I'd also look into better deployment strategies like blue-green deployment, so updates don't cause any downtime when the app restarts. Finally, I'd set up alerts so I get notified automatically when something goes wrong, rather than having to check the monitoring dashboard myself.

