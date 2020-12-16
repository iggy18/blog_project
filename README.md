# Lab: Django Models

Overview
Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

Today you’ll build out a project with one model and wire up that model using Django Views.

Feature Tasks and Requirements
- [x] create blog_project project
- [x] create blog app
- [x] migrate data
- [x] create Post model
- [x] add title as a CharField with maximum length of 64 characters.
- [x] add author ForeignKey related to Django’s built in user model with CASCADE delete option.
- [x] add body TextField
- [x] add model to admin
- [x] modify Post model have user friendly display in admin
- [x] create migrations and migrate data
- [x] create a super user
- [x] Add a few posts via Admin panel
- [x] Addtemplates folder in root of project
- [x] register templates folder in project settings
- [x] create HomePageView
- [x] extend ListView
- [x] give a template of home.html
- [x] associate Post model
- [x] create home.html template
- [x] use Django Templating Language to display each post’s title
- [x] create base.html ancestor template
- [x] add main html document
- [x] use Django Templating Language to allow child templates to insert content
- [x] update url patterns for app and project
- [x] view home page and confirm posts showing properly
- [x] add detail view
- [x] link post_detail.html template
- [x] associate Post model
- [x] create post_detail.html template
- [x] template should extend base
- [] content should display post title and body
- [x] update app urlpatterns to handle detail view
- [x] account for primary key in url
- [x] add link in home page template to related post detail page

- Implementation Notes
- The instructions are becoming more conceptual.
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client (aka the instructors.)
- TLDR - make your lab project like the demo project.

- User Acceptance Tests
- Test HomePageViewTest
- verify status code
- verify correct template use
- use url name instead of hard coded path
- We can’t test PostDetailView until next class.
- Can you figure out why?
- Configuration
- Create django-models GitHub repository.
- Use poetry to manage virtual environment and dependencies.
- Refer to Lab Submission Instructions for detailed instructions.

- Stretch Goals
- add styling
- create static folder at root of project
- update STATICFILES_DIRS
- create base.css file which styles base.html elements
- load static css in base.html file
- Test PostDetailView
- Test Post model
- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp