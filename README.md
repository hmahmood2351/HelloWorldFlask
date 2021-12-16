# HelloWorldFlask
Basic flask app for hello world

## The Application

The Application is a CRUD MYSQL based Python web application built using Docker containers, orchestrated in Jenkins, and orchestrated with Docker Swarm and Docker Compose.

It's purpose is to allow a user to have two tables, namely one for Internet services, and another for a list of intelligence organisations. Both can be added, updated, read, and deleted to. There's a link in the form of a one-to-many relationship between the Internet services and the intelligence organisations tables. 

The user starts off at the homepage. They're able to access each of the pages from there, reading, updating, creating, and deleting things as they please.

At the time of writing the application and the process of development as a whole implements the following technologies:

**Project Management** - Jira is used to map out the development process, through the use of an Agile methodology. With sprints, tracking issues, working on the backlog, daily standup meetings, and other activities within the development cycle, I was able to get a rough approximation of where we're headed, issues that we might be facing and prioritisation in terms of tasks. Since this was a single project, I had less informal Scrum Poker sessions by looking at what I had to do, the time it might take, and what I had done.

**Python Fundamentals** - Since Python was used for the majority of the project, and was used to instantiate the Flask application, model out the database schema, program the routes, and all of the other tasks associated with development in general. It required a level of knowledge up to OOP. Being able to understand how classes, objects, methods, and decorators work.  

**Python Testing** - Due to time constraints, I didn't get as much time to be programming tests in Python. Therefore, the implementation of testing is quite limited and is only limited to ensuring that the homepage loads successfully.
    
**Git** - Git was an essential part of the project.
  
  Linux
    Python Web Development
    Databases
    Continuous Integration and Deployment (CI/CD)
    Cloud Fundamentals
    Containerisation


   An explanation of your app and how it fulfils the brief.
A technical description of how the application works.

A technical description of how the pipeline works.
    A report on the success and code coverage of your unit tests.
    Any future improvements you would make.


    Entity Relationship Diagram (ERD).
    A full CI/CD pipeline diagram.
    An infrastructure diagram, illustrating the cloud resources and how they network together.
    A component-level diagram, illustrating how the application interfaces with the database.
