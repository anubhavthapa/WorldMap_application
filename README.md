# WorldMap_application
<h2>Project Overview</h2>

The software was built with the base of Django for backend and whereas React and Bootstrap was designed to handle the frontend operation. The software highlights all the countries in the world map that matches with the search query. <br>

![image](https://user-images.githubusercontent.com/32815205/121304720-6b378500-c91c-11eb-9225-ab922e296d5f.png)

Figure: Overall view of the project<br>

![image](https://user-images.githubusercontent.com/32815205/121304777-7be7fb00-c91c-11eb-8db8-f3307e97e649.png)

Figure: Search query and mapping function of the Application<br>

<h2>Development Overview: </h2>
The project was developed on two phases Backend and Frontend. <br>
<h3>Backend Development: </h3><br>
Since in this project Django was used to only structure the APIs for the frontend rather than performing web development activities in the Django. So Django Rest Framework was preferred as it make it efficient and easier to serialize and filter data while also providing OAuth support for the APIS<br>
<h4>Phases of Backend Development: </h4>
•	First a virtual environment was created in order to limit the scope of the project within the boundary of the environment<br>
•	Required dependencies such as Django, Django Rest Framework, Psycopg, pycountry, geopy was installed<br>
•	On the basis of mapped out architecture models and serializes were created in order to create table and serialize the data of those tables<br>
•	In the third step, all the required views and routes for the APIs was created so that the backend could interact with the frontend<br>
•	In order to get the country name and their geolocation the data were scrapped of from the internet in a json format <br>
•	The Oauth permissions was updated to only enable the Read features from the frontend as the program does not require Write permission from the Frontend on the present situation<br>
•	After the Frontend was developed all the static files were collected and Templates present in the settings file were updated to render the files of the build folder<br>
<h3>Frontend Development: </h3> <br>
For the Frontend Development React JS was preferred as it has a good support base community for developers and the components are rendered at very  fast rate which was very essential for this project as the software needs to map all the geo location on the basis of search query and it also provides the ability to reuse component which was very beneficial in the project as most of components such as country name and  geolocation was efficiently reused through this feature <br>
<h4>Phases of Front End Development: </h4><br>

•	First react project was initated and dependencies such as axios, react dom, react leaflet was installed through npm command<br>
•	In the Second phase, The frond end design was structured through the use of JSX, Bootstrap, CSS and HTML<br>
•	In order to provide appealing visual effects font icon and images were also integrated<br>
•	After that, Axios was setup and configured so that the frontend could interact with the backend through the API<br>
•	The combination of Openmap, Leaflet and React- Leaflet was used to render out all the geo locations on the world map which was provided by the API based on the search query <br>
•	At last step all the Frontend components were compressed into a build order in order to improve the app efficiency as well to reduce the memory storage during the production phase<br>

<h2>Challenges: </h2><br>
Since the project was done on a short duration. The challenges faced were often quite low but still I had faced some challenges such as: <br>
<h3>JsonField : </h3><br>
<h4>Problem: </h4> <br>
One of the major obstacle of Django is that its built in model has no JsonField support for Sqlite Database. Since the geo location of all the countries had to be stored in a Json format in order to improve the efficiency when the data is stored ion the Backend and  rendered at the Frontend as often times geo location of the countries have mixtures of variables such as String, Integer, Array and Float<br>

<h4>Solution: </h4> <br>
In order to solve these problem, PostgreSQL was used since it was more secured and the Django had the built in JsonField model for PostgreSQL hence making the stroing and retrieving process more efficient and effective <br>


<h3>Leaflet: </h3>

<h4>Problem: </h4><br>
Since one of the requirement of the Frontend Design was to present it in a dark    mode and this became quite obstacle when rendering the world map as the newer version of react-leaflet ignored any property changes made on the background <br>



<h4>Solution: </h4><br>
In order to solve this restriction problem the Layer present in react was entirely changed through rendering the layer from another open source website and the layer fitted perfectly with the dark theme website<br>




<h2>Future Improvements: </h2>
Since the project was only done on a shortly basis so there are lot the room for the improvement that could be performed such as: <br>
•	Locating and Marking the country with a popup marker that locates the country when a user clicks on the country name during a search operation<br>
•	Integration of admin, moderator and user panel<br>
•	Graph chart that displays the most searched country<br>
•	Availability of both the dark and light theme based on user preferences<br>
•	Integration of kelper library for more visual effects and animations on world map<br>
•	Detailed information such as the population, GDP and other economical factors of the searched country<br>
•	Based on the present situation active corona cases of the searched country could also be highlighted through the use of choropleth (darker color representing high active cases in relation to the population of the country) on the world map<br>
•	Vaccination tab where user can check on which city in their country the vaccination program is about to take place to achieve this feature the software could be programmed to send Google map location with direction based on the current user location<br>

<h2>Guide to use the project: </h2> <br>

•	In order to use the app the user install all the required pip dependencies through the provided requirements.txt<br>

```
 pip3 install –r requirements.txt

```


•	User must import the provided PostgreSql file(worldmap.sql): <br>


![image](https://user-images.githubusercontent.com/32815205/121304807-87d3bd00-c91c-11eb-99f1-0e55c7aa573d.png)


•	User must update the Password filed which in present in the DATABASE section at settings.py file located in worldmap folder<br>

![image](https://user-images.githubusercontent.com/32815205/121304836-915d2500-c91c-11eb-8e74-5137006ffa4d.png)

<h2>Note: Please refer to <b>Overview of the project.pdf</b> for clearer view</h2>
