# Walking the Wainwrights

(Developer: Martin Bradbury)

![AmIResponsive Image](/readme_imgs/Responsive.png)

## Live website

Link to live website: [Walking the Wainwrights](https://walking-the-wainwrights-7b754816f5c3.herokuapp.com/)

## Purpose of the project

The purpose of my website is to share my personal journey and experiences of walking all the Wainwrights in the Lake District. It's a digital diary where I document my routes, share images, and narrate my adventures. I aim to inspire and connect with fellow enthusiasts of the Lake District by providing a space for them to engage with my content, learn from my experiences, and perhaps even plan their own routes. Additionally, my website offers a unique opportunity for users to interact with me directly, either through contact forms or by leaving messages on my routes. This interactive feature fosters a sense of community among my visitors, encouraging them to share their own experiences, images, and stories of their walks in the Lake District. By creating a space where users can contribute their own content, my website not only serves as a personal blog but also as a collaborative platform for sharing and discovering the beauty and challenges of the Lake District together.

## Table of contents

## User experience (UX)

### Key project goals

- Sharing Personal Experiences: To share your personal experiences, routes, and images from your walks, aiming to inspire and engage fellow enthusiasts of the Lake District.
- To Build a Community: I want to foster a sense of community among my visitors by allowing them to interact with me directly, either through contact forms or by leaving messages on my routes.
- To Encourage Content Contribution: I'm looking to encourage users to contribute their own experiences, images, and stories of their walks in the Lake District, thereby creating a collaborative platform for sharing and discovering the beauty and challenges of the Lake District together.
- To Provide Educational Value: I plan to provide educational content, such as detailed routes, tips for navigating the Lake District, and insights into the history and significance of the Wainwrights, to enhance the visitor's understanding and appreciation of the area.
- To Promote the Lake District: Ultimately, I want to promote the Lake District as a destination for outdoor enthusiasts, showcasing its natural beauty, challenging walks, and rich history, to encourage more people to visit and explore the area.

### Target Audience

- Outdoor Enthusiasts: Individuals passionate about outdoor activities, particularly hiking and exploring natural landscapes.
- Walking and Hiking Communities: Groups interested in the Lake District and the Wainwrights, looking for inspiration, routes, and stories from fellow enthusiasts.
- Fell Running and Walking Enthusiasts: People who enjoy the challenge of fell running and walking, seeking to connect with others who share their passion for the Lake District.
- Travelers and Adventure Seekers: Individuals looking for unique travel destinations and adventures, interested in the Lake District's natural beauty and the challenge of the Wainwrights.

### User requirements and expectations

- Access to my Detailed Routes, videos and Images: Users expect to find information on my detailed routes taken as I endevour to summit all the Wainwright.
- Interactive Features: Users anticipate interactive features such as a map of my routes, video of each route and images taken along the way. Each Wainwright I have completed is listed with its details, and its rank in terms of height.
- Community Engagement: Users look forward to engaging with the community through features like message boards, and the ability to upload their own images and experiences. This fosters a sense of community and encourages sharing of personal stories and routes.
- Educational Content: Users appreciate educational content that provides insights into the wainwrights I have completed.
- Efficiency and Planning: Users expect resources that help them plan their walks efficiently. They can either download the route I have taken and use for themselves or use it in the planning process for their route. All the routes have been graded with a difficulty form 1-5.

## Epics and User Stories

1.  Epic: User Registration:
    -   User Story 1: As a new user, I want to register on the website so that I can share my experiences and contribute to the community.
    -   User Story 2: As a registered user, I want to be able to upload my images, write about my experiences and like / comment on posts.

2.  Epic: Route Planning and Sharing:
    -   User Story 1: As a user, I want to view detailed interactive maps of the routes the site admin has taken while completing the Wainwrights. Descriptions about the route including difficulty as well as videos to add a more visual representation of the route. I want to be able to download and use the route.
    -   User Story 2: As a user, I want to share my own photos and experiences with the community, so that others can see my journey.

3.  Epic: Community Interaction:
    -   User Story 1: As a user, I want to contact the website owner directly or leave messages on their routes and photos.
    -   User Story 2: As a user, I want to interact with other community members through comments and forums, so that I can share my experiences and learn from others.
    -   User Story 3: As a user, I want to be able to delete my account and all the posts / imgaes I have left on the website. 

4.  Epic: Educational Content and Resources:
    -   User Story 1: As a user, I want to access educational content about the Lake District and the Wainwrights the site owner has completed, so that I can deepen my understanding and appreciation of the area.
    -   User Story 2: As a user, I want to find resources for planning my walks, such as interactive maps of the site owners routes with all relevant information needed about the routes taken so that I can explore the Lake District more efficiently.

5.  Epic: Promotion of the Lake District:
    -   User Story 1: As a user, I want to discover new walks and destinations in the Lake District, so that I can plan my next adventure.
    -   User Story 2: As a user, I want to share my experiences and images of the Lake District with others, so that I can promote the area and inspire more people to visit.

##  As site Admin:

6.  Epic: Database and Admin Setup:
    -   Full backend CRUD on Routes, Images and comments.
    -   Approve posts, images and comments.
    -   Create route posts so users are able to see the routes I have taken.
    -   I can flag potential posts and images that are sensetive.
    -   I can respond to contact requests and mark as read.

7.  Epic: Routes and Images pages:
    -   Read other users comments and view their uploaded photos.
    -   Edit comments I have made, route blogs made and images uploaded.
    -   Delete my route posts, comments and images.

##  Features:

### Nav bar

A fully responsive navigation bar is in has been used. The main focus was on a 'mobile first' design where a clickable burger icon with a drop down menu appears on mobile. There is a burger icon is functional on tablets too upto and not including the ipad pro 12.9. Desktop view the burger menu disappears and the navigation menu appears along the navigation bar. The links in the Navigation element are: 'About' - Which takes you to the homepage, 'Routes' - Navigates to the routes page, 'Gallery' - which navigates to the photo gallery page, 'Logout' - if already logged in, 'Register' - Navigates to signup page and 'Login' - Which enables an existing user to login. The title is also clickable and navigates to the about page. The Nav bar also indicated to the user if they are signed in or not.

#### Desktop Navigation
![Desktop navbar](/readme_imgs/navbar/navbarD.png)

#### Mobile Navigation
![Mobile burger navigation button](/readme_imgs/navbar/navbarmburger.png)
![Mobile dropdown navigation menu](/readme_imgs/navbar/navbarmdrop.png)


#### Signed in status
![Not signed in](/readme_imgs/navbar/navbarnotlogged.png)
![Signed in](/readme_imgs/navbar/navbarlogged.png)

### Hero image Carousel

The hero image is a carousel of 3 images the site admin has the opportunity to change at any point in django admin. The carousel can rotates each image on all devices or can be manually invoked by clicking the left or right arrow.

#### Carousel Desktop
![Carousel images Desktop](/readme_imgs/Carousel/carouseld.png)

#### Carousel Mobile
![Carousel images mobile](/readme_imgs/Carousel/carouselm.png)

#### Admin control of carousel images
![Admin Control of Carousel](/readme_imgs/Carousel/Carouseladmin.png)

### About me cards

The mid section of the homepage (about page) comprises of 3 cards with a heading a description. These cards inform the user what they will find in each of these sections and help to draw their attention using imigary of what they are linkely to find in each section. The whole card is clickable and links to the corrospoiding page in the website.

#### About cards Desktop
![About card links desktop](/readme_imgs/aboutcards/aboutcardsd.png)

#### About cards Mobile
![About card links mobile](/readme_imgs/aboutcards/aboutcardm.png)
![About card links mobile](/readme_imgs/aboutcards/aboutcardm2.png)







##  Future Features:

##  Design:

##  Wireframes:

##  Database Schema:

##  Technology Used:
### Languages and framework:

- [HTML5](https://developer.mozilla.org/en-US/docs/Learn/HTML "link to html mozilla documentation")
  was used to create content and structure
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS "link to css mozilla documentation")
  was used to add custom styles
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript "link to javascript mozilla documentation") was used to dynamically reset the comment form if the reset button was clicked and to show a modal when the edit comment button was clicked
- [Django](https://www.djangoproject.com/ "link to django docs homepage") was the python framework used to develop the site

### Database:

- [PostgreSQL from ElephantSQL](https://www.elephantsql.com/ "link to elephantSQL") was used as the PostgreSQL database for this project.

### Technologies and tools:

- [GitPod Code](https://www.gitpod.io/ "link to Gitpod webpage") was used as the ide for this whole project.
- [Cloudinary](https://cloudinary.com/ "link to cloudinary homepage") was used to host images.
- [GitHub](https://github.com/ "link to github webpage") was used to store the code files, README files and assets
- [Git](https://git-scm.com/ "link to official git website") was used as a version control software to commit and push the code to the GitHub repository
- [Heroku](https://id.heroku.com/login "link to Heroku login") was used to deploy the project
- [lucidcharts](https://www.lucidchart.com/pages/ "Link to lucidcharts") was used to make a diagram of the database schema and entity relationship diagrams.
- [Prettier](https://prettier.io/ "link to official prettier website") was used as the default formatter in Gitpod IDE, for html and css files.
- [Bootstrap](https://getbootstrap.com/ "link to official bootstrap website") was used to quickly layout, position and size critical website features
- [Balsamiq](https://balsamiq.com/wireframes/ "link to official balsamiq website") was used in early planning to map out wireframes
- [Google Fonts](https://fonts.google.com/ "link to official google fonts website") was used to import fonts
- [Font Awesome](https://fontawesome.com/ "link to official font awesome website") was used for all icons
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/ "Link to official chrome developer tools website") was used for lighthouse testing, debugging and consistently checking responsiveness
- [W3C Markup Validator](https://validator.w3.org/ "link to official html validator") was used to validate all live html
- [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/ "link to official css validator") was used to validate CSS code
- [JS Hint](https://jshint.com/ "link to official javascript validator") was used to validate JavaScript code
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/ "link to official python validator") was used to validate all python code
- [Django Summernote](https://pypi.org/project/django-summernote/ "link to official summernote website") was used. This is a rich text editor plugin for Django
- [Django Crispy Forms](https://pypi.org/project/django-crispy-forms/ "link to official crispy forms website") were used throughout the project to quickly create forms

## Testing:
### HTML Validation
### CSS Validation
### JS Validation
### Python Validation

### User Testing:

### bugs

##  Deployment:

##  Credits
### Code
### Images

## Acknowledgements