# Nerd Cave

[View published site on Heroku](https://nerd-cave.herokuapp.com/).

![](docs/images/responsive-img-header.png)

## Project Overview

Nerd Cave is a blog website focus on topics connected to video games consoles, mostly reviews of products/games. Users can interact with each others through post comments. User can become an author if administrator assign staff member permission. Whole CRUD operations are enabled due custom 'Author Panel' avaiable to users with staff member permission. This site has been created as a portfolio project for Code Institute. Project - 4

## Table of Contents

1. [User Experience (UX)](#ux)
    * [Strategy](#strategy)
        * [Project Goals](#project-goals)
        * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Design](#design)
2. [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
3. [Technologies Used](#tech-used)
4. [Testing](#testing)
    * [User Stories Testing](#user-testing)
    * [Validation Testing](#validation-testing)
    * [Automated Testing](#auto-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

## User Experience (UX) <a name="ux"></a>

## Strategy <a name="strategy"></a>

### Project Goals <a name="project-goals"></a>

The business goal for Nerd Cave is to provide users with interactive blog website with consoles oriented stuff reviews. The user can create an account to be able to further interact with these blog posts via likes and adding comments. 

The main target customers/users are people interested in video games & consoles who are looking for reviews of games or accessories before buying them. Ex. 
1. Pro gamers looking for new controller. 
2. Kids looking for new games
3. Parents looking for good gift for theirs kids

### User Stories <a name="user-stories"></a>

* __Site User Goals:__

  * As a User, I can quickly identify what the main blog is about so that I don't have to waste time around
  * As a User, I can browse through the list of posts to find something interesting for me or reread some old posts.
  * As a User, I can read the whole post on a separate page, so that I can enjoy the content
  * As a User, I can like/dislike a post so that share my opinion.
  * As a User, I can add comments to each post so that I can share my opinion with other readers.
  * As a User, I can register to blog so that I can take active contributions to liking/commenting on posts
  * As a User, I can see the 'about page' so that I can learn more about the people behind that website.
  * As a User, I can send a message to site admins so that I can share my thoughts with the site owner(s) or ask to become an Author of the blog


* __Site Owner Goals:__

  * As a Site Admin, I can create, update or delete posts so that I can have control over the content on the website
  * As a Site Admin I can let other users become blog authors so that I can delegate some blog work to other people
  * As a Site Admin I can get messages from users through 'Contact' form.
  * As a Site Admin I can feel safe that authors are only able to edit/delete content that's belongs to them. 



## Scope <a name="scope"></a>

To achieve the strategy goals, I want to implement the following features:

* A navigation located at top of the page and also in the footer at the bottom of the page.
* A Home section which will allow the user to find out recent posts from 3 main categories (PS5,XBOX,SWITCH).
* A Contact page to provide users with possibility of contacting site admin.
* An About Us page to provide more information for visitor.
* A SignUp page to allow new users to create an account.
* A SignIn page for existing users to access their account to allow to like and add comments.
* A Logout functionality.
* A Post List page to allowed user search through all posts by category/title/author that were added to blog so far.
* A Post Detail page to view the selected post in more detail and allow adding comments/like the post.
* A Footer at the bottom of the website which is a second navbar and also allows the user to access social media links.
* A fully responsive design that will work on different devices.
* An Error 404 Page to allow users to redirect back to Home page in case of any errors.
* An Error 500 Page to allow users to redirect back to Home page in case of any errors.
* Full CRUD functionality for Admin OR User promoted by Admin to be an Author to allow to create, read, update and delete posts.

```
posts_used = {
    'xbox' :[
        'https://www.thexboxhub.com/bot-gaiden-review/',
        'https://www.thexboxhub.com/high-on-life-review/',
        'https://www.thexboxhub.com/a-space-for-the-unbound-review/',
        'https://www.thexboxhub.com/gundam-evolution-review/',
        'https://www.thexboxhub.com/the-bounty-huntress-review/',
        'https://www.thexboxhub.com/the-witcher-3-wild-hunt-complete-edition-review/'
    ],
    'switch' : [
        'https://www.nintendolife.com/reviews/switch-eshop/persona-4-golden',
        'https://www.nintendolife.com/reviews/nintendo-switch/fire-emblem-engage',
        'https://www.nintendolife.com/reviews/switch-eshop/lone-ruin',
        'https://www.nintendolife.com/reviews/switch-eshop/the-punchuin',
        'https://www.nintendolife.com/reviews/nintendo-switch/kukoos-lost-pets'
    ],
    'ps5' : [
        'https://www.gameinformer.com/review/crisis-core-final-fantasy-vii-reunion/required-reading',
        'https://www.gameinformer.com/review/tunic/a-dyed-in-the-wool-treasure',
        'https://www.gameinformer.com/review/need-for-speed-unbound/turning-a-tight-corner',
        'https://www.gameinformer.com/review/stranger-of-paradise-final-fantasy-origin/all-rage-no-soul',
        'https://www.gameinformer.com/review/sonic-frontiers/into-the-wild-blue-yonder'
    ]
}
```