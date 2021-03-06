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
- Then run: `python notebook/init.py -light` to get the light version of the data or `python notebook/init.py -full` to get the full version of the data.
- To start the sync between Mongo and ElasticSearch, run the command: `mongo-connector -m mongo:27017 -t elasticsearch:9200 -d 'elastic7_doc_manager'`

You have succesfully downloaded the data required to the project.

### Enjoy
Go to your favorite search browser and run this URL:
- `http://localhost:5000/index`

And enjoy. :)

### Link to data
The dataset we used for this project is [OpenFoodFacts](https://www.kaggle.com/openfoodfacts/world-food-facts) from Kaggle.


#### authors :
[Réda MAIZATE](https://github.com/reda-maizate)
[Thomas Tresgots](https://github.com/Taumah)

from [ESGI](https://www.esgi.fr/)
