## Table of Contents

- [Introduction](#introduction)
- [UX Design](#ux-design)
- [Development](#development)
- [Technology Used](#technology-used)
- [Deployment](#deployment)
- [Issues](#issues)
- [Credits](#credits) 

## Introduction

My Shopping App is a Django web application, intended to give users a streamlined platform for making, updating and managing shopping lists. The intended audience is for people with busy schedules, so that they have an easy on-hand way to note down what they need to buy as it comes to them; though anyone could use the application. It is intended to have full CRUD functionality and user authentication, meaning users of the service can create their own account on the application, on which they have the agency to create, update, and delete shopping lists and shopping items. At this stage however, due to several errors in the development that were not resolved, the application has not been deployed with any real functionality, though the project skeleton is in place.

------

## UX Design

This application was designed using Balsamiq to create wireframes. The method of the design was to conform to user stories.

### Wireframes

Landing Page
<img width="781" alt="Landing page" src="https://github.com/user-attachments/assets/2aa93270-4963-4e46-b499-b2d9556301ea">

Registration Page
<img width="685" alt="Registration page" src="https://github.com/user-attachments/assets/07f50392-7dec-4182-84c4-2969734aaacb">

Lists Overview Page
<img width="711" alt="Lists overview page" src="https://github.com/user-attachments/assets/7782455e-c7fa-4c3a-b8c0-9d77a3859eb8">

List Detail Page
<img width="707" alt="List detail page" src="https://github.com/user-attachments/assets/b2124c2e-1ecf-4d48-b648-090224b012b1">

### MVP

The MVP provides users with a handy application they can quickly sign up with, and then use to create custom dynamic shopping lists for staple items or whatever is needed, and with the option to delete lists once redundant, edit items on the list and generally use as a memory aid/notetaker of what is needed to buy.


### User Stories for My Shopping App:

- As a site user I can create new empty shopping lists so that I can add items I need e.g., groceries, to a list, as a memory aid.
- As a site user I can add items to a shopping list as dynamic entries so that I can edit within my shopping list itself, to reflect what I think is needed.
- As a site user I can create a user account with a username and password so that access to how I use the  site is private to me and protected.
- As a site user I can create a user account with a username and password so that access  to how I use the site is private to me and protected.
- As a site user I can access my user account  through a login form requiring a password so that my account's security is maintained.
- As a site user I can check off items from the list once selected to purchase so that I can keep track of my shopping while I am doing it.
- As a site user I can have the option to delete lists, and items individually from lists, that I no ,onger need to be there so that I can keep my user space organised and easy to manage.
- As a site user I can get asked to confirm that I wish to delete a feature, after selecting a delete option so that the risk of accidentally deleting something is minimised.

------

## Development

The project was attempted using Agile Methodology. User stories were mapped to a Github Projects project board to chart development progress. User stories were also assigned to one of two milestones: **Shopping List**, and **User Registration and Sign in**. Unfortunately due to early development problems that were not resolved, neither milestone was reached and no user story was able to be completed fully.

### Link to Project Board

https://github.com/users/henrybennett94/projects/6/views/1?filterQuery=assignee%3Ahenrybennett94

------

## Technology used
My Shopping App leverages several modern web development technologies, with the intention to create an engaging and interactive user experience. The key technologies used are Python, HTML CSS, Django, and Cloudinary.

### Python
Python is an object-oriented general purpose programming language used popularly in supporting web development. Using Python in a Django project enables the creation of powerful web applications by leveraging Django's high-level framework for clean, scalable, and maintainable code.
### HTML
HTML (HyperText Markup Language) is the standard markup language used to create the structure of the web pages in this application. It provides the skeleton for the app's interface, defining elements such as buttons, images, and text content.
### CSS
CSS (Cascading Style Sheets) is used for styling the HTML elements. It enhances the visual presentation of the app by controlling the layout, colors, fonts, and overall look and feel. 
### Django
Django is a Python web framework ideal for projects due to its robust scalability, offering rapid development, built-in security features, and a clean, pragmatic design. Its capabilities facilitate a well-structured development environment and enable a straightforward interface between application and database. 
### Cloudinary
Cloudinary is a cloud-based service that provides powerful tools for managing, optimizing, and delivering images and videos in web and mobile applications. Offering seamless media management and optimized delivery, it is an expedient tool for storing media in a Django application.

---
## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - Log in to herokuapp.com
  - From the Heroku dashboard, navigate to "New", and from the dropdown select "Create new app"
  - Choose a unique app name and select region, create app ("my-shopping-app")
  - In the Heroku my-shopping-app go to the Settings tab, reveal Config Vars and set the necessary keys and        values
  - Go to the Deploy tab, go to "Deployment Method" section and select Github
  - Search for and then select the relevant Github repository (https://github.com/henrybennett94/my-shopping-app), to connect it with the Heroku app
  - Navigate to the "Manual deploy" section, ensure the main branch is selected for deployment, and then select "Deploy"
  - Wait for the app to build in Heroku
  - Select "View" on completion of build
  - The deployed link can be found at: (https://my-shopping-app-969a4f2310f4.herokuapp.com/)

-----
## Issues

This application is not functional currently. The main issues are with url configuration, meaning the application cannot be run in the browser at all, and database configuration which has completely impeded the development of CRUD functionality. Unfortunately, neither of these fundamental issues have been resolved to date.

###  Database Configuration Issues

- Early in development, erroneous data was submitted to a field of the database, incompatible with the data type specified for that field in the associated data model.
- This stalled all further migrations and obstructed submission of data through forms in the running application.
- Attempts to undo the error were not successful. The database was reset, an attempt to build a new model was made, the migrations files were manually altered to try and reconfigure the operations and were eventually reset as well when this didn't work.
- With the database issues, running the application in the browser returned this error:![Screenshot 2024-08-06 at 12 47 24](https://github.com/user-attachments/assets/15d295a9-9b7d-4af6-b2a7-7822c5e1527f)- Attempts to resolve this error included changing url paths, which have not been reset to date. There have also been problems with the views.py and forms.py files running that are associated with the database errors.
- I have been at a loss for how to fix this, which became the main focus of my development and did not leave enough time to get any further than the stage of database and model configuration. If there were to be another attempt to work on this project, a possible solution that wasn't tried would be to use a new database entirely.

