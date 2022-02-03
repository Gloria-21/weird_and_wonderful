## Purpose of the project

Due to my background as an Art Historian and my MA in antiques I thought it would be a good idea of instead of creating a online cookbook,
as suggested on the Assesment Handbook, to take the structure of the project and adapt it to online an aution house.
Online aution houses have been evolving during the last ten years and right now are having huge success selling from the traditional antiques, modern art, to the lastest trend, the NFT art.
In this proyect I will focus in a basic structure as there is time constraining issues.

This multiple-page website has been created using Flask. In it, the user will see a Home page, About, and a Category page where all the different collections can be checked. Also, the user will be able to create an account and log in to a profile page, place bids on existing lots, as well as create new lots with items that the user wants to sell. Both, the bids and the new lots can be also deleted if the user change his mind.
## User stories

* As a new user I want to be able to create a new account and be part of Weird and Wonderful
* As a new user I want information of how the action works and upcoming auctions
* As a member of Weird and Wonderful I want to bid on lots that are interesting for me
* As a seller I want to create a lot to resell my items
* As a seller I want to be able to edit and delete my lot as well as see my bids


## Features

* **Navbar**

The navbar gives a friendly user experience as links the homepage, the activity section, and the Contact-us page.
Also on the mobile version, it can be found on the top right corner as a burger button that collapses, giving a better UX experience.

## Desing

* **Typography**

    The font use on the website has been chosen from [Google Fonts](https://fonts.google.com/). I have chosen Lato for the Navbar and headers and Roboto for the body

* **Colour Scheme**

The color range chosen for the website is coming from a [piece](/static/img/blue_lapis.png) of French porcelain manufacturer of Sevres that has the blue lapis as one of the most traditional colors.
To generate this color scheme I have used [coolors](https://coolors.co/)

[Palette](/static/img/color_scheme.png)

## Wireframe

The wireframes that can be found below have been created using Balsamiq during the Scope plane part of the design and planning process of this project.

* [Desktop Wireframe](file:///home/chronos/u-47a88eec4ef35331417eef91372e23e15aebb1fd/MyFiles/Downloads/Weird%20and%20wonderful/Weird%20and%20wonderful%20-Desktop.pdf)

* [Mobile Wireframe]()


## Technologies used

As it follows below
### Languages used
* [HTML5](https://en.wikipedia.org/wiki/HTML5) 

* [CSS3](https://en.wikipedia.org/wiki/CSS)

* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

* [Python](https://www.python.org/)

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)

    I have used Bootstrap to help with the responsiveness of the website as well as the styling

2. [Google Font](https://fonts.google.com/)

    I have used Google font to import the fonts that have been used on all pages throughout the project

3. [Font Awesome](https://fontawesome.com/)

    Used for the icons on this website

4. [Balsamiq](https://balsamiq.com/)

    I used Balsamiq to create the wireframing during the design process

5. [Git](https://git-scm.com/)

    Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub

6. [Github](https://github.com/Gloria-21/Living-Salamanca)

    I used GitHub to store the project's code after being pushed from Gitpod

7. [TinyPNG](https://tinypng.com/)

    I used TinyPNG to compress images making them load faster

8. [Heroku](https://id.heroku.com/login)

    I used Heroku as a deployment tool

9. [MongoDB](https://www.mongodb.com/)

    Used to create the database that holds all the data from the website

10. [StartBoostrap](https://startbootstrap.com/)

    I use the start boostrap [template](https://startbootstrap.com/template/shop-homepage) to style the website

## Testing

I have done the testing for my website using the dev tools on google chrome. I have been testing regularly checking that the results were the expected on different sizes, from mobile devices to desktop and tablet, making sure the website was responsive in all of them.
I used this tool as a main source to implement my code, trying the functionality and styling effects there first and adding them to my code afterward.

At a later stage, when the site was deployed, the website was tested by family and friends who looked on different devices and gave feedback on responsitivity and user experience.

### Validator testing

To check the validity of the codes I have used [W3C Markup Validation](https://validator.w3.org/), [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) and [JS Hint](https://jshint.com/)

* Index.html page has passed the validator with no error [index.html]()
* Style.css page has passed the validation with 0 errors [style.css]()
* JavaScript has been validated on JS hint and it doesn't bring any warnings

### Performance

To check the website performance level as well as the speed I used [Google lighthouse](https://developers.google.com/web/tools/lighthouse)
![Atl text]()
## Test user stories

1. 

## Fixed bugs

* I decided to use a start boostrap template as the time that I had to develop this project was quite tight, however I have found quite challeging the adaptation of that template to my project, to the point that I think I could've done more without it.

## Suported screen and browsers

The website was mainly tested on different screen sizes using the devtool.
The web behaves in a responsive way in the different mobile sizes (Moto G4, Galaxy S5/A71, Pixel 2/2XL/3, iPhone 5/SE/6/7/8, iPhone 6/7/8 plus, iPhone X/10/12)

It also behave as expected on tablets (iPad, iPad pro, surface duo)

* Google Chrome: website worked as expected
* Firefox: website worked as expected
* Microsoft Edge: website worked as expected
* Safari: website worked as expected
## Deployment

This website has been developed on Gitpod, using Github to host the repository

### Via Gitpod 

These are the step followed to deploy via Gitpod:
1. Log in to the Gitpod account 
2. Chose the Weird and Wondeful repository
3. Add your code 
4. Type "python3 -m http.server" on the terminal
5. A new screen will pop up with the results of the code on the browser
### GitHub pages

These are the steps followed to deploy this website using GitHub:

1. Log in to your  GitHub account
2. Select Weird and wonderful on my repositories
3. Go to settings on the repository
4. Scroll down to the GitHub pages area
5. Select the Master Branch from the Source dropdown menu
6. Confirm my selection 

After this, the website was live on GitHub pages

### Making a Local Clone

Making a local clone of your repository allow others to view the original code and even to add changes on their own local copy.

To do so you have to 
1. Log in to GitHub and select teh repository you wish to clone
2. Click the download button or Code button
3. Copy the url that will show on the box
4. Open Gitpod (or your preferred IDE)
5. Use the "git clone" command in the terminal followed by url copied before

A clone of the original repository should be available on your computer

### Heroku App

1. Log in to Heroku
2. From the dashboard click in "Create a New App" and give it a unique name
3. Add the region that you are on and click on "Create App"
4. On your Gitpod terminal install "npm install -g heroku"We then need to tell Heroku which applications and dependencies are required to run the app. We need to add ""pip3 freeze --local > requirements.txt". This file is needed so that Heroku knows which files needs to be installed.
5. In the terminal we also need to add "echo web: python app.py > Procfile" to create a Procfile. This file is needed so that Heroku knows which file is needed as its entry point to get the app running.
6. Set up automatic deployment by clicking the deploy tab and clicking GitHub as the deployment method.
7. Ensure your GitHub profile is displayed, then add the name of the repository and click search.
8. Click the "Settings" tab and then click "Reveal Config Vars".
9. Set the Key values as below
    * IP = 0.0.0.0
    * PORT = 5000
    * MONGO_DBNAME = YOUR MONGODB DATABASE
    * MONGO_URI = YOUR MONGODB URI
    * SECRET_KEY = YOUR SECRET KEY
10. Click the "Deploy" tab and "Enable Automatic Deployment"

## Credits
 ### Content
 * [CataWiki](https://www.catawiki.com/en/)
 * [Sotheby's](https://www.sothebys.com/en/?locale=en)
 * [Christies](https://www.christies.com/?lid=1&sc_lang=en)
 * [Bonhams](https://www.bonhams.com/)
 ### Media
 Some of the photos shown on this prject have been taken from [Pexel](https://www.pexels.com/) as per below

 Also I have used [Unplash](https://unsplash.com/@jeremybezanger?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  
 ### Code
 * [Code Intitute](https://codeinstitute.net/) was the main source for this project
 * [Slack Community](https://slack.com/intl/en-no/) for their support, specially to Sean Young for sharing his knowledge on Js with me
 * [Stack Overflow](https://stackoverflow.com/) and [W3school](https://www.w3schools.com/) as main places to go to resolve questions
 

 ### Acknowledgements:
* I would like to thank my fellow students in the Slack community and the tutor assistance for their help, without them I could not have finished the project on time.
* I would like to thank my mentor for his advice and aid in debugging technical issues
* And also my partner and family for putting up with me when I am under pressure
