## WELCOME TO
### the code for Welcome To, an automated conference talk

__slideshare.py__ is the main script, which handles all of the webdriving and theatrical timing, there is some tesseract and reactrnn code hanging around there, pay it no mind

__custom\_markov.py__ is the module where all the markov model functions got moved after refactoring

__gdocs\_api\_calls.py__ is the module where all the google slide api functions got moved after refactoring

__text\_corpuses__ is where the starting corpus text lives (none of the scraped text used in markov generation is saved... for reasons...)

__test\_scripts__ are some sloppy debugging tools
