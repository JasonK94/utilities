"# utilities" 


it's my effort to play language-learning mp3 files conveniently, not on website with unfriendly UI/UX.
To achieve my first goal, I needed to download each mp3 file as I can run them on my own audio player.
mp3crawler.py is about this process.
Additionally, I wanted to remove the unnecessary intro of each mp3 files. 
trimmer.py is about this process.

to run mp3crawler.py, you need to figure out how to get the mp3 URL from the inspection tab of your web browser.
If you can play the audio on the web anyway, usually you can find out the HTML code, javascript, whatnot where the mp3's URL resides right in the condition you are running the audio file.
to run trimmer.py, you need to download and install ffmpeg first, which can be done by visiting the homepage (https://ffmpeg.org/download.html) or install Chocolatey first.
Installation of Chocolatey can be done by two lines of command:
1. run cmd with administrator authority, then run:
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
2. after installation of Chocolatey, run:
choco install ffmpeg

After installation of ffmpeg, to register the PATH of ffmpeg so that python can find the program without specification, you might need to restart you system.
I tried directly refer the location of ffmpeg or register the PATH manually, but these all failed.
So for your mental health, I recommend you to just restart.


