#  CheeZam
A Case-based reasoning system created by the NTNU students: Marius Shberg, Sander Lindberg and Thomas Ramirez Fernandez.
For the subject TDT4173 - Machine Learning


**
The purpose of Schitzam is to explore the possibility to predict song genres using case based reasoning(CBR). CBR is a subset of machine learning that closely relates to how people reason when encountering a problem. The core idea is to solve new problems based on previous solutions. This paper contextualizes CBR and shows how it can be used to classify song genres based on a set of attributes, such as the song's energy and tempo. It explains how the CBR classification is achieved trough looking at each process of the CBR method and shows its code-implementation. A dataset containing circa $39000$ songs/cases and their attributes were used. **
## Installation
Python3.8+ is needed
Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the packages:
- mysql-connector (2.2.9+)

```bash
cd CBR_system
pip3 install mysql-connector
```

## Usage
To use our applicatin, you need to navigate to the "cd CBR_system" folder. There you will find the file main.py, and the only file you need to interact with.

```bash
cd CBR_system
python3 main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)