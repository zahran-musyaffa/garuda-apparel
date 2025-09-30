
# Garuda Apparel - Assignment 3 

## Why do we need data delivery in implementing a platform?
Data delivery enables the exchange of information between different system components and servers. it allows platforms to communicate dynamically, updating content, and provide interactive design. 
without Data delivery platform would be static and needed to refresh frequently make it limited due to functionality and scalability

## Which is better, XML or JSON
In my opinion JSON is better than xml because:
1. JSON has simpler and more easy to read compared to xml
2. JSON is supported by Javascript make it easy to use directly in web browsers

## Purpose of `is_valid()` method in Django forms and why do we need it
The `is_valid()` method in Django forms is used to validate form data submitted by users. It checks for correct data types and required fields.
We needed `is_valid()` method to ensure data is consistent before processing it. So it will prevent error in database and in application.

## Why do we need `CSRF_token` when making forms in Django ? What happen when we dont include `csrf_token` in Django form ?
CSRF token is needed to protect our Django project from Cross-Site Request Forgery attacks. CSRF token is security mechanism that protects our website against malicious website performing unauthorized action
Without CSRF token: 
1. attackers could delete modify or create data.
2. check and change our personal privacy such as email, address, password and many our sensitive information

## Explain how to implement checklist above :
1. first i create templates folder and add `base.html` file. this file is used as a generic view for other web pages in this project. 
Then i add templates in `DIRS , templates` in `settings.py` so base.html recognize as templates file. After that i extend base.html in `main.html` file 
2.  After that in `main` directory add `forms.py` file to display and accept users input 
3. Creating views to displaying and adding data. Then use `is_valid()` to makesure users input meets all validation.
4. Add url routes to access each view
5. Build `html templates` for list form and detail_news
6. Add xml and JSON format to data delivery views
9. Adding xml and json url patterns for accessing XML and JSON data 
10. Adding to git and pws by using `git add-commit-push`

## Postman Screenshots
image.png

## Any feedback for teaching assistant
none 

# Assignment 5

## CSS Selector Priority
1) inline Styles (styles="...")
2) ID selectors ( #header)
3) Classes Selectors ()
4) Elemeent Selectors (h1)
- !important overrides specificity but should be avoided except as last resort

## Responsive Design
### Why it matters
- Ensures UI of our website adapts to different screen sizes (mobile, tablet, desktop) and improving accessibility
- Reduce maintenance cost by not making seperate codebase for mobile/laptopby 

### Examples
- Implemented responsive:`instagram.com` that adapt grids to any device we use

## Box Model
- Margin: outside space around the element’s border used to separates the element from neighbors
- Border: the line surrounding padding and content and visible
- Padding: inside space between content and border used to expands the visual area.


## Layout Systems
### Flexbox
- One-dimensional layout (row or column).
- used for aligning and distributing space among items in a single line or column such as navbars card toolbars

### CSS Grid
- Two-dimensional layout (rows and columns).
- Ideal for complex page grids and dashboards where both axes matter.


## Tutorial — Styling, Edit/Delete, Navbar (Simple Box Summary)

1) Choose a styling framework (tailwind)
ensure it in `base.html`

2) Static files config (`settings.py`):
  - Add `whitenoise.middleware.WhiteNoiseMiddleware` under `SecurityMiddleware`.

3) Navbar (`templates/navbar.html`):
  - Create a responsive navbar and include it on page with `{% include 'navbar.html' %}`

4) Page styling for each in html and add `global.css`

5) Make product card that has [title, category, views, price] and put empty static image

6) add edit/delete features in `views.py` then add it in `urls/py` 
   make sure edit and delete features only work only if the owner of the product wanna customize it.
   add this feature to the `main.html` 
