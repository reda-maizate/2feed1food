# 2 Feed 1 Food
by Réda MAIZATE and Thomas TRESGOTS

## Prerequisite
The following apps should be downloaded:
- Docker
- npm
- gulp

## Get started
### Git clone the repo

To git clone this project, go to your working directory and run this command:
- `git clone https://github.com/reda-maizate/2feed1food.git`
You have now succesfully cloned this projet.
Go to the folder `2feed1food` by using the command: `cd 2feed1food`

### Download the packages
Run the next command:
- `npm install`
- `docker-compose up -d --build`
- `gulp build`

### Download the data
To use the project, you'll need to do these next steps:
- Run on your command line: `docker exec -it {name of the web container, in my case: 2feed1food_web_1} bash`
- Then run: `python notebook/mongoDB/install-light.py` to get the light version of the data or `python notebook/mongoDB/install-big.py`to get the full version of the data.
- Exit from the `docker exec` by running on the command line: `exit`.
- Run on your command line: `docker exec -it {name of the mongo container, in my case: mongo} bash`
- Then: `mongorestore /data/db/mongo/dump`.
- Finally, relaunch the docker, to be sure that the data are synchronized to the two database (Mongo and Elastic). 

You have succesfully downloaded the data required to the project.

### Enjoy
Go to your favorite search browser and run this URL:
- `http://localhost:5000/index`

And enjoy. :)

cd {WORKDIR}

docker-compose up
### Getting set up

|  Tool  | Command |
|:---  |   ---:   | 
|  `git blabla` | bonsoir |
|   ---  |   ---   |



### Frequently Used


authors :
[Réda MAIZATE](https://github.com/reda-maizate)
[Thomas Tresgots](https://github.com/Taumah)

from [ESGI](https://www.esgi.fr/)
