#  CheeZam
A Case-based reasoning system created by NTNU students: 
Marius Sjøberg, Sander Lindberg and Thomas Ramirez Fernandez.
For the subject TDT4173 - Machine Learning

From our project paper:
> *The purpose of the paper is to explore the possibility to predict song genres using case-based reasoning(CBR). CBR is a subset of machine learning that closely relates to how people reason when encountering a problem. The core idea is to solve new problems based on previous solutions. This paper contextualizes CBR and shows how it can be used to classify song genres based on a set of attributes, such as the song's energy and tempo. It explains how the CBR classification is achieved through looking at each process of the CBR method and shows its code-implementation. A dataset containing circa 32000 songs/cases and their attributes were used.*
## Installation
Python3.8+ is needed

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the packages:
- mysql-connector (2.2.9+)

```bash
cd CBR_system
pip3 install mysql-connector
```

## Usage
To use our application, you need to navigate to the "cd CBR_system" folder. There you will find the file main.py, and the only file you need to interact with.

```bash
cd CBR_system
python3 main.py
```
#### Genre prediction
The system will start by with:
```bash
Connected to: 5.7.23
You are connected to the database: ('90567_schitzam',)
-----------------------------------------------

Please input a song title to predict genre: 
```
Here insert the name of the song you want to search on and press enter.
It continues with asking for the artist name;
```bash
Please input a song title to predict genre: Hello       
Please enter artist of the song: Adel
```

The prediction for the genre will appear in the terminal. It now needs user evaluation for if the prediction is correct or wrong. 
```bash
The CBR-system prediciton: [pop]
Are you satisfied with the song's predicted genre "pop" (y/n)? 
```
To answer, you need to enter y-yes or n-no.
If the answer is no, a list of genres will appear and you will now have the option of chooses one of them(1-6), or to insert a new genre(7).
the terminal will look like this:
```bash
Which of the following genres do you think fits the song best?
1. R&b
2. Rap
3. Edm
4. Rock
5. Latin
6. Pop
7. Enter myself
```
If you answered that the prediction was correct, the part over is skipped, and it continues to subgenre prediction.
### Subgenre prediciton

Similar to the first prediction, the system will present its prediction and now need user feedback in the for of "y" or "n".
```bash
Are you satisfied with the song's predicted sub-genre "neo soul" (y/n)?
```
If the case is that it is wrong, a list with all sub-genres in the system will be presented in a list and additionally the possibility to insert a new sub-genre.
```bash
Which of the following genres do you think fits the song best?
1. Post-teen pop
2. Classic rock
3. Electropop
4. New jack swing
5. Tropical
6. Big room
7. Latin pop
8. Urban contemporary
9. Electro house
10. Latin hip hop
11. Progressive electro house
12. Permanent wave
13. Indie poptimism
14. Neo soul
15. Album rock
16. Reggaeton
17. Hip pop
18. Pop edm
19. Dance pop
20. Southern hip hop
21. Hard rock
22. Trap
23. Hip hop
24. Gangster rap
25. Christmas jams
26. Enter myself

1 - 26:
```

If the prediction was correct and you entered yes, the system thanks for your feedback and either insert the new case to the knowledgebase or update an existing one if already exist in the DB.
```bash
Thank you for your answers!

Goodbye,it was nice to meet you.
```


Here are the prosses and interaction map for the usage of the CheeZam system
![usage-map-of-cheezam](https://raw.githubusercontent.com/tartaruz/CheeZam/main/usage_diagram.png)

---
Marius Sjøberg, Sander Lindberg and Thomas Ramirez Fernandez.
