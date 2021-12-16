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


A technical description of how the pipeline works.
    A report on the success and code coverage of your unit tests.
    Any future improvements you would make.


    Entity Relationship Diagram (ERD).
    A full CI/CD pipeline diagram.
    An infrastructure diagram, illustrating the cloud resources and how they network together.
    A component-level diagram, illustrating how the application interfaces with the database.
