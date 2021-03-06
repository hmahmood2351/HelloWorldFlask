# HelloWorldFlask
Flask Project - Warrant Canary System

## The Application

The Application is a CRUD MYSQL based Python web application built using Docker containers, orchestrated in Jenkins, and orchestrated with Docker Swarm and Docker Compose.

It's purpose is to allow a user to have two tables, namely one for Internet services, and another for a list of intelligence organisations. Both can be added, updated, read, and deleted to. There's a link in the form of a one-to-many relationship between the Internet services and the intelligence organisations tables. 

The user starts off at the homepage. They're able to access each of the pages from there, reading, updating, creating, and deleting things as they please.

At the time of writing the application and the process of development as a whole implements the following technologies:

**Project Management** - Jira is used to map out the development process, through the use of an Agile methodology. With sprints, tracking issues, working on the backlog, daily standup meetings, and other activities within the development cycle, I was able to get a rough approximation of where we're headed, issues that we might be facing and prioritisation in terms of tasks. Since this was a single project, I had less informal Scrum Poker sessions by looking at what I had to do, the time it might take, and what I had done.

**Python Fundamentals** - Since Python was used for the majority of the project, and was used to instantiate the Flask application, model out the database schema, program the routes, and all of the other tasks associated with development in general. It required a level of knowledge up to OOP. Being able to understand how classes, objects, methods, and decorators work.  

**Python Testing** - Due to time constraints, I didn't get as much time to be programming tests in Python. Therefore, the implementation of testing is quite limited and is only limited to ensuring that the homepage loads successfully.
    
**Git** - Git was an essential part of the project. It allowed me to stage, push, pull, and branch during the project. The GitHub platform allowed me to have my code and all files hosted on a repository, to be pulled and used from anywhere. My JenkinsFile, Docker-Compose, and application are all in the repository. I have a dev branch for whenever I want to test features locally. I can do a pull request to merge those changes from the dev branch to main.
  
**Linux** - Linux was needed as a lightweight base for my containers to be running Python on. It was also needed for the various infrastructure components of my project, such as the Jenkins VM and Swarm Nodes. I needed to have a certain level of knowledge about Linux - installing applications, navigating around, using SSH, using Docker, Jenkins, and networking. 
   
**Python Web Development** - This was specifically achieved with Flask, a library which allowed me to quickly have a backend ready and able to handle routes and templating, which formed the backbone of my application. Extensions were used with Flask which provided features such as having forms on pages, and for interacting with SQL databases programatically. 

**Databases** - I experimented with the inbuilt sqlite database, a local MySQL server, and then eventually picked up Azure SQL Database. It suited my needs, and I was able to initiate connections, define the schema, and conduct CRUD operations within my Flask application.

**Continuous Integration and Deployment (CI/CD)** - my CI/CD pipeline currently works only on my main branch. Any features that I test locally are merged into main. The continuous deployment part was essential in ensuring that there was a smooth process from me pushing up my code up into main, and then new containers being built, images being pushed into DockerHub, and then deployed to my Docker Swarm setup. This resulted in me having the ability to see changes instantly with my setup, and lessened time spent on menial building and bringing up infrastructures.

**Cloud Fundamentals** - Since I had my Jenkins VM and Swarm Nodes up in the cloud, I needed to know how a certain cloud provider (I'm using Azure) worked and the basics of how to deploy resources, deal with basic networking (IPs and open ports), and administration of my resources into resource groups. 

**Containerisation** - By containerising my application using Docker I was able to deploy it and have it run fairly quickly, regardless of the environment I was running it on. It allowed me to only have those libraries that I only needed, and hence kept resource usage down when building and deploying images. I used a public DockerHub repo.

## The Application with technical details

The application itself, is written in Python. It's divided into several sections:

**Imports** - These were required so that the application, with all of the functions and classes that are being called, are able to access them. Since I didn't have enough time to split up my application into separate portions, there's a fair amount of them at the top.

**Initialisation** - This was necessary, in order to instantiate the Flask object, configure the database URI, change the SQLALCHEMY_TRACK_MODIFICATIONS and configure the SECRET_KEY for the form, as well as instantiating the database object. Without these, the Flask application wouldn't exist, as well as the database object, and having a connection to the (actual) remote database.

**Database Layer Schema** - The way SQLAlchemy works is that I can use Python code, in the form of classes and attributes, to be able to define what my SQL database looks like. This was achieved for the Services and the Agencies tables, which all have their own columns (as class attributes in Python). The Agencies table has a foreign key, referring to the Services primary key.

**Defining Forms** - These were defined using Python OOP as well, and were to be used on the majority of the routes within the website. They allow for a user to input in data, and have that then translated into the program. Validators are used to check the inputs. Most of the fields are based on StringFields.

**Defining Routes** - Are what allow the user to navigate around the website. Through the help of url_for(), I was able to then use these to mimic what a real website would be looking like in terms of navigation. There are a total of five different routes within the web application. Some require the POST HTTP method in order for data to get through, as it is disabled by default. Each route has its own programming to give its functionality within it.

**Runtime** - The actual step of running the application, allowing it to be run on the Flask default of 5000.

The DockerFile takes a few steps that ensures that the application has what it needs as a container. It ensures that Python is available, and copies all of the necessary files it needs (in the same directory as the DockerFile is based), does a pip install -r requirements to ensure that Python has all the modules it needs to work the application, exposes the port 5000 outside of the container, and makes python app.py run every time the container is run, which results in the application running.

The Docker-Compose file works by pulling the latest application image from DockerHub and publishes the port 80 and maps that to 5000 on the container. This is used so that the Docker Swarm Manager node can use Docker Stack to deploy the application using the Docker-Compose file, aiding in the continuous deployment process.

## The Pipeline

The place where the CI/CD process happens. From start to finish, these are the stages involved along with an accompanying diagram.

**Submitting Code to VCS** = the first stage, composed of me submitting my code to main or to the developer branch. I manually do a pull request with main whenever I want those changes to be made to my program.

**Testing the program** - didn't get around to implementing this in the CI/CD pipeline, but I would have a separate stage in the JenkinsFile where testing happens.

**Building the Docker image** - building the Docker image based on the latest code is needed so that those changes are enacted in the application.

**Deploying to DockerHub** - I then want that container available to be pulled from everywhere, so my Docker-Compose file uses a remote image in order to build.

**Reinitialising Docker Swarm setup.** - After pulling the latest image on the Docker Swarm Manager node, I want the application to be run or updated through Docker Stack deploy.

Pipeline diagram:

![image](https://user-images.githubusercontent.com/44241991/146505260-a650ed3c-5710-4013-9ca4-ffaefbf03cfb.png)

Infrastructure Diagram:

![image](https://user-images.githubusercontent.com/44241991/146505931-93503128-128a-40d1-8754-db236207dd0f.png)


Component-level Diagram:

![image](https://user-images.githubusercontent.com/44241991/146506439-0ccd37f8-10bb-4294-b279-b0bf3cb2bbbd.png)


ERD Diagram: appdb database

![image](https://user-images.githubusercontent.com/44241991/146507066-0475f13e-b064-4edc-be60-d60ac9dce107.png)



**Issues and Future Improvements**

I encountered many issues during this project, most notably time and lack of experience in building projects - especially with testing, security and the CI/CD process.

I had a persistent issue of trying to figure out a secure way to have my environmental variables (used for the database connection string) kept secure and not leaked in a code repo or in a DockerHub image. I saw that I was going off on a tangent when researching about different implementations and was forced to cut this part short when dealing with credentials, since I didn't have enough time left. I was last looking at Azure Key Vault and BuildKit. I also tried to use a private repo to avoid any build arguments being leaked, however that didn't seem to pair well with the Docker Swarm nodes. I also looked at having a local registry before moving on.

I also had some issues with getting databases to work. It seems that the more complicated the database gets, the more knowledge you need to have in order to do certain operations. My application doesn't have a complete delete functionality because I didn't know how to do a cascading delete (which I'm 99% sure is the way to go about deleting records with dependencies in another table) since I only covered basic deletions.

I faced issues in the whole build agent and deployment process, and was consistently going through a trial-error process. I don't have the prerequisite knowledge to build and tear down my deployment environment so the CI/CD pipeline works on the presumption that there's an environment for it to deploy to, namely only a Swarm Manager node. This would've saved me a large amount of time in installing and setting up my machines.

Practicing Jenkins and CI/CD more would've lead to a better outcome for this project. I only managed to get the application worked on the last day. The majority of that time was spent on figuring out how I could put a basic Hello World Flask application and continually deploy it to a Cloud infrastructure. Hence the name of the repo. I could've also figured out how to use CI with Github Actions. 
