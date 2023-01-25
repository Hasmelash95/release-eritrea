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

[Technologies Used](#technologies-used)

[Testing](#testing)
* [Validation](#validation)
* [Performance](#performance)
* [Functional](#functional)
* [Responsive Design](#responsive-design)
* [Browser Compatibility](#browser-compatibility)
* [Testing User Stories](#testing-user-stories)

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
  
  3. Home Page - As a Site User I can peruse the home page so that I can see all the site has to offer.
  
* Epic - Site Navigation
  
  1. Navigation Bar - As a Site User I can click on the navigation links so that I can go to whichever section of the page I wish.
  
  2. Visible Navbar - As a Site User I can look at the navigation bar so that I can navigate to different parts of the site at any time.
  
  3. Home Page Links - As a Site User I can click on links on the home page so that I can navigate to different parts of the site.
  
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
  
   4. View Info Page - As a Site User I can view the info page so that I can know who are the team members, how to contact them and where the offices are.

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
  
A fade in effect is triggered when an object is visible to the user - some elements begin to appear as the user scrolls. 
  
## Features
  
### Header and Hero
  
The header contains the logo of Release Eritrea along with the name (a bird breaking a chain) along with the nav elements which take the users to specific sections of the page or to other sites within the page. There are Sign In and Sign Up options for users who have not been authenticated with links to the relevant pages. 
  
![Screenshot 2023-01-22 at 14 28 29](https://user-images.githubusercontent.com/103432143/213921167-873ee366-67f7-4498-a03d-e4bb03482ec1.png)

If the User has already signed in, a 'Hello, [User Name]!' appears along with a Logout link. 
  
![Screenshot 2023-01-22 at 14 28 43](https://user-images.githubusercontent.com/103432143/213921226-074f7aa3-b7c7-410c-aa6a-1109a21707a9.png)

The Navbar remains on screen as the user scrolls to allow for easy navigation. The active page is underlined (in this case, the home page). 
  
The hero image of a hand holding chains is adjacent to a verse (recommended by the client). This fades into view when the page has loaded. 
  
![Screenshot 2023-01-22 at 14 34 40](https://user-images.githubusercontent.com/103432143/213921358-e87542ca-f31f-4995-9f4d-b190db77868c.png)
  
### About Us

The About Us section introduces visitors of the site to Release Eritrea and provides them information (simplified) to introduce them to the charity and what they do.

In addition, links are provided to give users additional resources, such as links to the Team Page and external links to partner charity websites (which open in another tab).
  
![Screenshot 2023-01-22 at 14 39 17](https://user-images.githubusercontent.com/103432143/213921600-23a4bd5b-203e-47b9-8116-c57b34a71a6e.png)
  
![Screenshot 2023-01-22 at 14 40 27](https://user-images.githubusercontent.com/103432143/213921659-4491d3ba-a337-462f-bbaa-f8b215ce48c5.png)

### Press Releases
  
The main draw of the site is of course the press releases. Previews with links to the detailed pages of the articles allow users to peruse through the many pages and click on whichever article captures their attention. 
  
![Screenshot 2023-01-25 at 06 45 18](https://user-images.githubusercontent.com/103432143/214497993-57f38143-0bb3-48dc-9d4e-1b0165aa4db8.png)
  
Article detail pages have a comment section with a comment form, the latter of which is only visible to logged in users. Comments must be approved by the admin to be visible under the article.
  
![Screenshot 2023-01-22 at 14 49 12](https://user-images.githubusercontent.com/103432143/213922278-d2ea1186-9343-4b4d-a4d2-7d94f9d96057.png)

![Screenshot 2023-01-22 at 14 50 21](https://user-images.githubusercontent.com/103432143/213922289-eba7c310-e47b-429b-b61e-fbcb5dbf63bc.png)
  
![Screenshot 2023-01-22 at 14 51 17](https://user-images.githubusercontent.com/103432143/213922267-6c972178-4729-446b-80bc-0cca42ed07ef.png)

Admin may click on the edit or delete buttons, or post a new article article from that section. There are also buttons to direct users to the Favorites or Search Filter pages.

![Screenshot 2023-01-22 at 14 45 17](https://user-images.githubusercontent.com/103432143/213921908-077fcc08-c2e2-4746-bb4e-3bb06b8f772e.png)
  
![Screenshot 2023-01-23 at 15 10 34](https://user-images.githubusercontent.com/103432143/214075282-0581d278-6df1-4ef9-b8ee-88b088f4a4e6.png)
  
![Screenshot 2023-01-25 at 05 27 53](https://user-images.githubusercontent.com/103432143/214487232-ae405d81-d9c5-4fdd-9e8c-c2c30fd81abc.png)
  
The Search Filter page allows users to find the article they need through tags or words or phrases in the title.
  
![Screenshot 2023-01-25 at 15 45 00](https://user-images.githubusercontent.com/103432143/214609259-4c2fc7b2-a4d2-469c-b23f-b50eaa1e6965.png)

### Gallery
  
The Gallery section shows users official Release Eritrea pictures for a visual sense of what the organisation does. Admin can add, edit and delete pictures via the admin page. 
  
![Screenshot 2023-01-22 at 14 52 37](https://user-images.githubusercontent.com/103432143/213922368-746ba9ef-764c-48c4-8ffb-795fdecf57aa.png)
  
### Footer
  
The Footer contains social media links (which open in a new tag) providing methods of contacting Release Eritrea. As well as the charity number and company number.
  
![Screenshot 2023-01-22 at 14 55 03](https://user-images.githubusercontent.com/103432143/213922433-05ba2140-9515-49ff-9bf3-4a3db5520d29.png)
  
### Info
  
The Info page provides information on the profiles (not User profiles) of the Release Eritrea staff and team members with contact details in case users wish to get in touch with them directly. Locations details are also available. 
  
This data can be added, edited or deleted from the admin site.
  
![Screenshot 2023-01-22 at 14 57 00](https://user-images.githubusercontent.com/103432143/213922529-c847e206-6602-444c-a21a-a34841fbae0f.png)

![Screenshot 2023-01-22 at 14 57 05](https://user-images.githubusercontent.com/103432143/213922532-d4ffa149-4a84-4d37-bf24-0e42767b4eb6.png)

### Django Admin
  
Django provides an authentication system that allows users to create accounts, login using their accounts and logout. Those with staff permissions can access the django admin site to make changes to the database. 
  
![Screenshot 2023-01-22 at 14 58 01](https://user-images.githubusercontent.com/103432143/213922600-8709738a-ea90-4987-a120-a6facf3aef84.png)
  
![Screenshot 2023-01-22 at 14 57 31](https://user-images.githubusercontent.com/103432143/213922607-dbf21a3e-ff41-4816-9f11-f6f5f3cb38dc.png)

![Screenshot 2023-01-22 at 14 59 29](https://user-images.githubusercontent.com/103432143/213922672-17077265-3a0a-4422-bb55-762df0a21c41.png)

### Error Pages
  
Raising 400, 403, 404, 405 and 500 errors redirects the user to custom error pages with links to return to the home page.
  
Error page for a 404 error:
  
![Screenshot 2023-01-22 at 15 24 24](https://user-images.githubusercontent.com/103432143/213923915-eea4c96f-cc1a-4bac-a4c8-c8b21761bd9f.png)

### Future Features
  
1. Allow Users to Edit comments, which will then need to be re-approved by the Admin. [In the To Do section](https://github.com/users/Hasmelash95/projects/3).
2. Add a Donation feature via debit card and paypal. [In the To Do section](https://github.com/users/Hasmelash95/projects/3).
3. Add a Contact Us page to allow users to send direct messages to the organisation from the website. 
4. Offer a subscription service which will give users alerts when a new article is added to the site.
  
## Technologies Used 
  
HTML5
  
CSS3
  
Python 
  
JavaScript
  
Gitpod
  
Git
  
Heroku

Django
  
[Bootstrap v5.3](https://getbootstrap.com/)

[Cloudinary](https://cloudinary.com/)

[django-filter](https://django-filter.readthedocs.io/en/stable/)
  
[django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  
[django-summernote](https://github.com/summernote/django-summernote)
  
[Whitenoise](https://whitenoise.evans.io/en/latest/)

## Testing

### Validation
  
JavaScript was run on [JSHint](https://jshint.com/) and showed no errors. 
  
Python code was run on [PEP8](https://pep8ci.herokuapp.com/) and showed no errors.

![Screenshot 2023-01-25 at 05 32 35](https://user-images.githubusercontent.com/103432143/214487771-281f2329-94f9-48cf-a8e0-8fc85cf90996.png)

CSS style sheet was run through W3C CSS Validator [Jigsaw](https://jigsaw.w3.org/css-validator/validator) with no errors. 
  
![Screenshot 2023-01-23 at 15 26 19](https://user-images.githubusercontent.com/103432143/214079247-159c9e01-e4dc-4d52-a7ca-97f396e3cb37.png)

The Home Page was run through [W3C Markup Validator](https://validator.w3.org/) with no errors.

![Screenshot 2023-01-23 at 15 30 57](https://user-images.githubusercontent.com/103432143/214080111-2791ea55-b067-48d5-8791-cc1b90d4c37c.png)

Info Page 
  
![Screenshot 2023-01-23 at 15 32 28](https://user-images.githubusercontent.com/103432143/214080284-3cee95b7-415b-4a81-a09a-a1f1aec9f8de.png)
  
Article Detail 

![Screenshot 2023-01-23 at 15 46 22](https://user-images.githubusercontent.com/103432143/214083527-668433dd-e319-4fd4-b4ba-6cfb388ee875.png)

Post and Edit Article were run through the validator and showed no errors in the custom code except:

![Screenshot 2023-01-23 at 15 48 01](https://user-images.githubusercontent.com/103432143/214083892-9d04fa4e-c6c0-484c-ad53-b31e18798817.png)

This is the result of a Django widget. The text area for content is unused as summernote div was used instead so django had marked the content as hidden. This isn't available in the template so could not be adjusted.
  
Delete Article
  
![Screenshot 2023-01-23 at 15 49 37](https://user-images.githubusercontent.com/103432143/214084314-ef4a37d3-8c1c-4709-a30b-002ae89e0d86.png)
  
Add/Remove from Favorites
  
![Screenshot 2023-01-25 at 05 35 24](https://user-images.githubusercontent.com/103432143/214488094-f24cbba7-cb67-4339-8d4b-41cdbaf90485.png)

Favorites 
  
![Screenshot 2023-01-25 at 05 36 09](https://user-images.githubusercontent.com/103432143/214488159-459ba9ed-e8c9-40ca-8b84-6dc11a8b8a10.png)
  
Search Filters
  
![Screenshot 2023-01-25 at 05 36 50](https://user-images.githubusercontent.com/103432143/214488238-1dbce5d9-8f89-4430-9d34-cf248fd87f78.png)
  
Error 404 
  
![Screenshot 2023-01-25 at 05 37 45](https://user-images.githubusercontent.com/103432143/214488403-0879a2ce-7a63-4e57-ba32-ee61424acf14.png)
  
Sign In

![Screenshot 2023-01-25 at 05 39 39](https://user-images.githubusercontent.com/103432143/214488616-cd9724b3-b289-4870-a604-a881ee33a0de.png)
  
Logout 
  
![Screenshot 2023-01-25 at 05 38 43](https://user-images.githubusercontent.com/103432143/214488505-ad3e23d3-195e-4571-a9c8-92e149c0e128.png)

Sign Up 
  
![Screenshot 2023-01-25 at 05 41 08](https://user-images.githubusercontent.com/103432143/214488802-9f3a7e39-c2d8-4901-a2bd-fe097b32eb60.png)

### Performance
  
Lighthouse tests were run for each of the pages on the site:
  
Home
  
![Screenshot 2023-01-23 at 15 58 56](https://user-images.githubusercontent.com/103432143/214089235-e0ac8729-2224-4a33-8952-e1f496141139.png)
  
Info
  
![Screenshot 2023-01-23 at 15 59 44](https://user-images.githubusercontent.com/103432143/214089275-9be730ea-ba44-49e1-8df8-897229de2314.png)
  
Logout

![Screenshot 2023-01-23 at 16 00 20](https://user-images.githubusercontent.com/103432143/214089304-6d5ab95a-675d-4f2c-9913-6dbf914828eb.png)

Sign In
  
![Screenshot 2023-01-23 at 16 00 47](https://user-images.githubusercontent.com/103432143/214089325-edea0742-36fc-4557-aaee-38a7950e4066.png)
  
Sign Up
  
![Screenshot 2023-01-23 at 16 01 22](https://user-images.githubusercontent.com/103432143/214089370-70299a76-b267-4b0c-b49a-71e1e179f982.png)
  
Post Article
  
![Screenshot 2023-01-23 at 16 02 36](https://user-images.githubusercontent.com/103432143/214089409-9221c00a-3820-4855-87e3-0fed8a04175e.png)
  
Edit Article
  
![Screenshot 2023-01-23 at 16 04 08](https://user-images.githubusercontent.com/103432143/214089437-b90f5f37-eb0b-47a5-95de-79be433bf0c7.png)
  
Article Detail
  
![Screenshot 2023-01-23 at 16 03 38](https://user-images.githubusercontent.com/103432143/214089479-02acceed-8f88-4b27-9331-4a5174a57463.png)

Delete Article
  
![Screenshot 2023-01-23 at 16 05 07](https://user-images.githubusercontent.com/103432143/214089510-578a55e0-af42-4228-93fb-640059fb4e47.png)
  
Add/Remove from favorites
  
![Screenshot 2023-01-23 at 16 05 36](https://user-images.githubusercontent.com/103432143/214089538-11156f87-233f-447a-90de-7afee675e62f.png)

Favorites
  
![Screenshot 2023-01-23 at 16 06 08](https://user-images.githubusercontent.com/103432143/214089581-debda9da-e74a-4d6e-acde-0aecd35c0b38.png)
  
Search Filters
  
![Screenshot 2023-01-23 at 16 06 42](https://user-images.githubusercontent.com/103432143/214089621-5dc1940f-2eca-460e-bfa9-38eeea96a77a.png)

### Functional
  
Functional tests were carried out to ensure the features of the site were working correctly. 
  
[Manual Functional Tests](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/testing/functional-tests.pdf)

[Press Views Automatic Tests](https://github.com/Hasmelash95/release-eritrea/blob/main/press/tests.py)

[Info Views Automatic Tests](https://github.com/Hasmelash95/release-eritrea/blob/main/info/views.py)
  
![Test Screenshot](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/testing/automatic-test-screenshot.png)

### Responsive Design
  
[Home Page Mockups](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/mockups/home-page.png)
  
[Info Page Mockups](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/mockups/info-page.png)

[Article Detail Mockups](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/mockups/article-detail.png)
  
[Article Filter Mockups](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/mockups/article-filter.png)

### Browser Compatibility 
  
Website was tested on Safari, Firefox, Google Chrome, Microsoft Edge, iOS and Android devices and was compatible with all of them. 
  
### Testing User Stories
  
User Stories were tested for whether they fulfilled the acceptance criteria defined within [Issues](https://github.com/Hasmelash95/release-eritrea/issues). They fulfilled the criteria. 
  
The only exception are those User Stories that were labelled "won't do" as they'll be added in the next iteration.
  
[User Stories Test](https://github.com/Hasmelash95/release-eritrea/blob/main/README-assets/testing/release-user-stories.pdf)

## Bugs and Fixes
  
  ### Fixed Bugs
  1. Edit article did not keep the input fields filled in, leading users to an empty form. This was fixed by adding the 'article': article to the context.
  2. Post article did not keep the input fields when the user's form was invalid triggering a refresh of the page. This was fixed by adding article_form = ArticleForm() at the top of the function. 
  3. The spinner showed up when the user clicked the sign in/sign up buttons even if the input was empty. If statements were added to ensure the spinner showed up when the required fields were filled in. 
  4. Summernote was creating validation errors due to attributes used in the widget. This was resolved by copying the iframe file (found in the summernote div github) into a template in my directory and manually removing the attributes. 
  
  ### Unfixed Bugs
  1. There are no unfixed bugs remaining, besides the validation error triggered in the form pages due to the presence of an unsued django widget that could not be adjusted.

## Deployment

### Deploying the App
1. Create a Heroku account or log in if you have one.
2. Click on the "Create new app" button on the dashboard.
3. Give the app a unique name. 
4. Select your region.
5. On the resources tab, select the 'Heroku Postgres' add on.
6. Click on the settings tab.
7. Add a Config Var with the key PORT and the value 8000.
8. Add CLOUDINARY_URL and SECRET_KEY to the Config Vars and an env.py file (which will be placed in gitignore). The DATABASE_URL will be generated by Heroku and can be added to the env.py file as well. 
9. Set DISABLE_COLLECTSTATIC to 1 but remove this when deploying the app. 
10. Use pip3 freeze --local > requirements.txt to update the project with installed apps. 
11. Click on the deploy tab.
12. Connect to Github under deployment method, search the repository you wish to link to and click 'connect'.
13. Select either automatic or manual deploy. The former rebuilds the app everytime you git push.
14. You will see an "App was successfully deployed" message.
15. The application can be run by clicking 'Open App'.

### Cloning the Repository 
  
1. Log on to your Github account and head to the main page of the repository you wish to clone.
2. Click on the 'Code' button above the list of files and choose from HTTPS, SSH or Github CLI, to copy the URL provided.
3. Open terminal and ensure you are in the correct location.
4. Type in 'git clone' and paste the URL you'd copied in step 2 and press enter.
  
## Acknowledgements

I would like to thank my mentor Brian Macharia for his help during the project. I am more than grateful for his advice and guidance and he has truly helped me feel more confident in my code. 
  
A huge thanks to the tutor team at Code Institute for helping with difficulties during the automatic testing process. I'd also like to thank Code Insistute for their resources which taught me how to use the Django framework - such as Hello Django and I Think I Blog walkthroughs. The latter of which was helpful in building my Article and Comment models.
  
I'd like to thank Release Eritrea for the resources they'd given, such as images and articles to use for the website. 
  
The hero image was from [Unsplash by Eyasu Etsub](https://unsplash.com/photos/5wdR59K0nyI?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
  
[Font Awesome](https://fontawesome.com/icons) was used for the icons used throughout the site. 
  
Intersection Observer API from [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) for fade on scroll effect.
