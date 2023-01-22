# Hermon Asmelash

## Release Eritrea

[Check out the deployed site](https://release-eritrea.herokuapp.com/)

Proclaim! Release Eritrea is a human rights charity advocating for the persecuted Christians in Eritrea. It is a global partnership which advocates on behalf of victims of abuse by the PDFJ's (the ruling party of Eritrea) regime and provides humanitarian assistance to the victims and their families. The website offers updates to those who wish to learn more about the human rights abuses happening in Eritrea with press releases that logged in users can comment on and bookmark in their favorites. In addition, there are social media links and profiles of the members of Release Eritrea in case those visiting the site wish to get in touch and get involved. 

![Screenshot 2023-01-17 at 19 15 53](https://user-images.githubusercontent.com/103432143/212991420-f9f8db80-860f-49e9-a0a9-1af6d36a8627.png)

## Table of Contents

[User Experience](#user-experience)
* [Strategy](#strategy)
* [Scope](#scope)
* [Structure](#structure)
* [Skeleton](#skeleton)
* [Surface](#surface)

[Features](#features)
* [Header and Hero](#header-and-hero)
* [About](#about-us)
* [Press Release](#press-releases)
* [Gallery](#gallery)
* [Footer](#footer)
* [Info](#info)
* [Error Pages](#error-pages)
* [Future Features](#future-features)

[Testing](#testing)
* [Validation](#validation)
* [Performance](#performance)
* [Functional](#functional)
* [Responsive Design](#responsive-design)
* [Browser Compatibility](#browser-compatibility)

[Bugs and Fixes](#bugs-and-fixes)

[Deployment](#deployment)

[Acknowledgements](#acknowledgements)

## User Experience (UX) <a name="user-experience">

### Strategy 
  
#### User Stories
  
The website is targeted toward any who are interested in aiding humanitarian efforts and wish to support Eritrean Christians who are being persecuted as well as any who know nothing about the charity and wish to learn more. It provides information via Press Releases and introduction texts for those unaware of the situation in Eritrea. 
  
Using Agile Methodology, User Stories were created from Themes and Epics with [GitHub Issues](https://github.com/Hasmelash95/release-eritrea/issues). Each User Story was marked with a label for prioritisation. Must do, Should do, Could do, Won't do. The latter are to be implemented in the next iteration (see future features). They were compiled as a result of lengthy discussion with the Director of Release Eritrea and potential users to establish what the target audience would be looking for in a site. 
  
Theme - Site Layout 
* Epic - Site Content
  
  1. Readability - As a Site User I can easily read the content on the site so that the process is stress free and not time consuming.
  
  2. Social Media - As a Site User I can find social media links on the site so that I can contact release through social media.
  
* Epic - Site Navigation
  
  1. Navigation Bar - As a Site User I can click on the navigation links so that I can go to whichever section of the page I wish.
  
  2. Visible Navbar - As a Site User I can look at the navigation bar so that I can navigate to different parts of the site at any time.
  
  3. As a Site User I can click on links on the home page so that I can navigate to different parts of the site.
  
Theme - Authentication System 
* Epic - Admin Authentication 
  
  1. Admin Signup - As a Site Admin I can Sign Up using a username and password so that I have access to the benefits an admin should have.
  
  2. Admin Login - As a Site Admin I can log in to my account so that I can make changes to the site whenever needed.
  
* Epic - User Authentication 
  
  1. User Signup - As a Site User I can Sign Up using a username and password so that I have access to the benefits a user should have.
  
  2. User Login - As a Site User I can Sign In so that I can comment on the posts.
  
Theme - View and Edit Content
* Press Releases 
  
  1. Post Articles From Site - As a Site Admin I can post articles from the site so that those visiting the site can read new updates from the organization.
  
  2. Edit Articles From Site - As a Site Admin I can edit and delete articles so that I can adjust the content or remove as necessary.
  
  3. Post Old Articles - As a Site Admin I can post old articles so that users can peruse stories from years before.
  
  4. Comment on Articles - As a Site User I can comment on articles so that I can share my thoughts.
  
  5. Favorites - As a Site User I can add articles to my favorites so that all my favorite articles can be found in one place.
  
  6. Article Filter - As a Site User I can search articles based on their title contents or tags so that I can find specific articles more swiftly.
  
 * Gallery and Info
  
  1. View Gallery - As a Site User I can find the gallery section so that I have a visual idea of what the org does.
  
  2. Edit Gallery - As a Site Admin I can edit, add and remove pictures so that the gallery section remains up to date.
  
  3. Add and Edit Info Contents - As a Site Admin I can add and remove content from the info page so that users can be updated on current team members and locations.
  
  4. View Info Page - As a Site User I can can view the info page so that I can know who are the team members, how to contact them and where the offices are.

### Scope
  
The website will contain user authentication to allow those with staff permissions to log in and access the admin database and those with user permissions to comment and favorite posts. 
  
A single page will contain the About Us section (which will contain external links to partner charities and another page with information on the Team and Release Eritrea offices). The main page will provide a list of Press Releases which can be navigated through using pagination. Clicking on any one of these will take the user to the article detail page where they can comment - which will be processed for admin approval - and favorite the article. The home page will also contain a gallery section which can be edited by admin. 
  
There will be links to allow users to access their favorites page and the search filter page to filter articles by tags and title content. 
  
Those with admin permissions will be able to add, edit and delete articles from the front end. 
  
Social media links will be available on the footer along with the charity and company number. 

### Structure

The logo at the header contains a link to the home page. Navigation links on the header allow users to navigate to the Home and the three sections on the home page, About Us, Press Releases, Gallery. Another link takes the user to the info page. User authentication links are also present on the header to take users to the log in, sign up or logout pages. 
  
The Press Releases section shows 6 article previews a page and clicking on any of the previews takes the user to that specific article. Attempting to access an article that has been deleted will raise a 404 error and the users will be taken to a custom 404 error page. 
  
ERD (courtesy of Visual Paradigm Online)
  
The Picture, Location and Profile Models (Profile of Members of Release Eritrea rather than User Profile) do not have relationships with other entities. 
  
The Article ID has One-to-Many relationship with the Comment Model. The User Model has a One-to-Many relationship with the Article ID, a One-to-Many relationship with the Comment Model and a Many-to-Many relationship with the favorities attribute within the Article Model. 
  
![Screenshot 2023-01-17 at 23 02 49](https://user-images.githubusercontent.com/103432143/213031512-17ce36b8-9297-49c6-bc38-ded22e0ae8d6.png)

![Screenshot 2023-01-17 at 23 17 37](https://user-images.githubusercontent.com/103432143/213033387-1ab8cf09-1917-47a8-a24a-92fba9ffecbe.png)

### Skeleton

#### Wireframes
  
[Home](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/home.png)
  
[Home mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/home-mob.png)
  
[Article Detail](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-detail.png)
  
[Article Detail mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-detail-mob.png)

[Article Filter](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-filter.png)
  
[Article Filter mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-filter-mob.png)
  
[Info](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/info.png)
  
[Info mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/info-mob.png)
  
[Article Form](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-form.png)
  
[Article Form mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/article-form-mob.png)
  
[Favorites](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/favorites.png)
  
[Favorites mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/favorities-mob.png)
  
[Sign In](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/sign-in.png)
  
[Sign In mobile](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/sign-in-mob.png)
  
[Logout](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/logout.png)
  
[Logout mob](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/wireframes/logout-mob.png)

### Surface 

Noto Serif Oriya and Roboto fonts were imported from google fonts for the headers and main text respectively. The main colour themes for the site use bootstrap backgrounds. text-bg-primary and text-bg-light classes ensure the foreground and background colours do not clash with bg-gradient also used for a gradient effect for the backgrounds. The main text within the site is rgb(0, 95, 161), a colour close to black. 

Other bootstrap classes are used to colour in the buttons, to ensure that they stood out in the page and are still visible against the background. Font awesome icons decorate some of the headings and the buttons to add a touch of decor to the site. 
  
## Features
  
### Header and Hero
  
### About Us

### Press Releases
  
### Gallery
  
### Footer
  
### Info

### Error Pages
  
### Future Features

## Testing

### Validation

### Performance

### Functional

### Responsive Design

### Browser Compatibility 

## Bugs and Fixes

## Deployment
  
## Acknowledgements
