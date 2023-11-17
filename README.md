# Pranz-Angelo-Cloma
# ITCC 14 A SEMI FINAL PRACTICAL EXAM
# School Id: 20190016357@my.xu.edu.ph

What is this python file?

This represent as my personalized data which is my personal interest.
I like to play Video Games a lot, which is why This API allows you to see
what video games won the "Game of the Year Award" and its details from 2014-2022 (Game of the year Award for 2023 has not yet been decided),
I created an API which has Get option that allows you to see the details of the listed video games and what year does this specific game won.

What makes this unique?
This API makes it unique because for an average person that isn't updated to games who have been awarded with the Game of the year award.

How to use this API?

Just open post man and run flask, Run the python file by using 'python main.py' in the terminal copy the running http given and paste it in Postman. 'http://127.0.0.1:5000/game-info'

Params:
- Key 'name' and value 'game title'

If you are using the Get command you'll have the details of what game does that have. 

For the Post command. You'll need to rewrite the get option and replace the 'game-info' with 'add-game' and then go to the "body" tab and select "raw", then set the content type to 'JSON' so that you may request and insert a new game. 
