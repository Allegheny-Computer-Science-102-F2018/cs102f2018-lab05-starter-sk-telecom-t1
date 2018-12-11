
# SK Telecom
# cs102 FINAL REPORT
# Christian, Mohammad, Jeremy 
#  “Scientific Calculator”

# Motivation
The motivation for this project stems from the team's collective majors or minors of computer science and economics. A calculator will always be needed in the field, throughout daily tasks and is essential to the success of a job. Especially since there is a common interest in data analytics there will be extensive numbers that have to be used with a calculator. The argument is that using a calculator doesn’t benefit the knowledge of the user, but in this technological era it has to be used in order to ensure the best results. The perk this project is that it’s a calculator that can be adjusted and customized. The scientific calculator uses discrete structure functions and is coded with python’s TKinter graphical user interface. None of the team has much experience with a gui so this was a learning process. That learning process is part of the motivation because the team wanted to try something out of the ordinary for 102’s final project. The customization of TKinter and it’s many different features was a common interest. TKinter was consistently top 3 in all of the lists for the bests gui’s to use for python in our research search. This made TKinter the best choice for this assignment.

![](https://raw.githubusercontent.com/Allegheny-Computer-Science-102-F2018/cs102f2018-lab05-starter-sk-telecom-t1/master/images/colorchart.png)

# Implementation
![](https://raw.githubusercontent.com/Allegheny-Computer-Science-102-F2018/cs102f2018-lab05-starter-sk-telecom-t1/master/images/flowchart.png)
This project was coded in Python3 using the TKinter graphical user interface. The project’s code is split into three parts within a class. The calc() class that would define all of buttons features and what those buttons achieve when clicked upon. The second part of this class included the graphical interface part of those buttons. The buttons code is split into code for the standard and scientific part. The buttons color, size, length and where it’s placement at was on the grid. The grid was split into 8 columns and six rows. The last part of the class included the menu of the calculator. This would allow the user to click scientific or standard calculator and exit the program. The code was split in a way that is easy to read and understand for one unfamiliar of the program or coding in general and the hard code is commented.

![](https://raw.githubusercontent.com/Allegheny-Computer-Science-102-F2018/cs102f2018-lab05-starter-sk-telecom-t1/master/images/standard.png)
Creating the standard part of the calculator included loading all of the numbers into the gui and having each number count when clicked upon. The standard calculator includes the basic PEMDAS features. This is one of the hardest implementations of the project. Creating a range for which the numbers can be counted within the number pad. Then taking that count and making it possible to add, subtract, etc. initially was hard with the equal sign. Once the first defined function worked, then all the others came easy because the code was very repetitive. Understanding the rows/columns of the program deemed easier because the team simply looked at a normal calculator as an example and counted. The width/height of each button was guesstimated.


The next part of the calculator was the scientific part. The decision originally was to make a fresh calculator for the scientific part of the calculator, but that was inefficient. The easier solution was to make the calculator with many rows/columns, but block the user from adjusting the height/width of the calculator. The entire calculator couldn’t be seen unless the scientific button is pushed. One of the groups that presented had the problem that the user could adjust the size and would therefore find glitches and problems with the program. With this calculator locking the size adjustment was essential. 


