# Data_Visualization
Nora Mohamed &amp; Lucy Wilcox's python data visualization project for Software Design SP 2015

This project’s goal is to create an interactive visualization of our dataset of over 10 million username and password combinations, focusing on the password portion of the dataset. The program creates a GUI using TKinter, where the user can look at graphs of commonly occurring data on the passwords or look at graphs with information comparing user input to the data set. The graphs are generated in the user’s web browser using Bokeh, which allows them to be interactive as well.

<b>IMPORTANT</b>: datafunctions.py assumes you are using a Linux distibution where the location of your computer's english dictionary is /usr/share/dict/american-english. Change this if it's not true.

<b>Download our dataset</b>:<br>
<a href = "https://www.dropbox.com/s/wr60kzhpylwcwz8/10-million-combos.txt">10-million-combos.txt</a>

<b>Libraries to import</b>:<br>
-Bokeh<br>
-TkInter<br>
-<a href = "https://pypi.python.org/pypi/python-Levenshtein/">Levenshtein</a>
