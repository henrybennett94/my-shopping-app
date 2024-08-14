## Table of Contents

- [Introduction](#introduction)
- [UX Design](#ux-deisgn)
- [Development](#development)
- [Project Structure](#project-structure)
- [Technology Used](#technology-used)
- [Deployment](#deployment)
- [Bugs](#bugs)
- [Credits](#credits) 

## Introduction

My Shopping App is a Django web application, intended to give users a streamlined platform for making, updating and managing shopping lists. The intended audience is for people with busy schedules, so that they have an easy on-hand way to note down what they need to buy as it comes to them; though anyone could use the application. It is intended to have full CRUD functionality and user authentication, meaning users of the service can create their own account on the application, on which they have the agency to create, update, and delete shopping lists and shopping items. At this stage however, due to several errors in the development that were not resolved, the application has not been deployed with any real functionality, though the project skeleton is in place.

------

## UX Design

This application was designed using Balsamiq to create wireframes. The method of the design was to conform to user stories.

### Wireframes



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
  - The deployed link can be found at:  
  
