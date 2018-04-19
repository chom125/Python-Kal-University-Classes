#Create a folder in a suitable place on your file system and switch into it. I generally keep a
# dedicated folder in my home directory called Projects to use for all of my projects, and give
# each project a folder within it - in this case the project is called django_tutorial_blog_ng.


#Now, we’ll use Git to keep track of our source code. If you prefer Mercurial, feel free to use that,
# but this tutorial will assume use of Git, so you’ll want to adapt the commands used accordingly. Start
# tracking your project with the following command from the shell, when you’re in the project directory:

$ git init
Next, we set up our virtualenv. Run the following command:
$ virtualenv venv --distribute

#Followed by:

$ source venv/bin/activate

#Every time you come back to work on this project, you’ll need to run the previous command to make sure
# you’re running the version of Python installed under venv/ rather than your system Python. You can tell
# it’s using this because your shell prompt will be prefixed with (venv).
#install Django, as well as several other useful Python modules. Run the following command:

$ pip install django-toolbelt South

#Once the installation is complete, run the following command to record the new modules installed:

$ pip freeze > requirements.txt

#edit it manually to look like this, as when we deploy it to Heroku, it will need to be correct to
# ensure that our application can be deployed successfully:

Django==1.6.1
South==0.8.4
dj-database-url==0.2.2
dj-static==0.0.5
django-toolbelt==0.0.1
gunicorn==18.0
psycopg2==2.5.1
static==0.4
wsgiref==0.1.2

#Next, we’ll commit these changes with Git:
$ git add requirements.txt
$ git commit -m 'Committed requirements'

#Also want to ignore any compiled Python files (identifiable by the .pyc suffix):
#venv/

*.pyc

#Let’s commit that too:

$ git add .gitignore
$ git commit -m 'Added a gitignore file'

#Now, let’s generate our project’s basic skeleton:

$ django-admin.py startproject django_tutorial_blog_ng .

#This application skeleton includes a basic configuration which will be sufficient
# for now, but you will also want to add the SQLite database file to your .gitignore:

env/
*.pyc
db.sqlite3
Let’s commit what we’ve done:
$ git add .gitignore django_tutorial_blog_ng/ manage.py
$ git commit -m 'Created project skeleton'

#Now, before we create our database, we need to ensure we are using South. Go into
# django_tutorial_blog_ng/settings.py and find INSTALLED_APPS. Edit it to look like this:

INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'south',
)

#Now, you can create your database. Run the following command:
$ python manage.py syncdb

#You’ll be prompted to create a superuser - go ahead and fill in the details. Now, run the following command:
$ python manage.py runserver

#This will run Django’s built-in web server on port 8000, and if you click here, you should see a
# page congratulating you on your first Django-powered page. Once you’re finished with it, you can stop
# the web server with Ctrl-C.
#Don’t forget to commit your changes:

$ git add django_tutorial_blog_ng/settings.py
$ git commit -m 'Added South to installed apps'

#Run the following command to create a basic skeleton for this app:

$ python manage.py startapp blogengine

#Next, we need to amend our settings to install this app:

INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'south',
'blogengine',
)

#Run the following command to create your initial migration:
$ python manage.py schemamigration --initial blogengine

#That creates the file for your first migration,but doesn’t run it. To migrate your database
# structure to the latest version, run the following:Open up blogengine/tests.py and amend it as follows:

from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from blogengine.models import Post
# Create your tests here.
class PostTest(TestCase):
def test_create_post(self):
# Create the post
post = Post()
# Set the attributes
post.title = 'My first post'
post.text = 'This is my first blog post'
post.pub_date = timezone.now()
# Save it
post.save()
# Check we can find it
all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 1)
only_post = all_posts[0]
self.assertEquals(only_post, post)
# Check attributes
self.assertEquals(only_post.title, 'My first post')
self.assertEquals(only_post.text, 'This is my first blog post')
self.assertEquals(only_post.pub_date.day, post.pub_date.day)
self.assertEquals(only_post.pub_date.month, post.pub_date.month)
self.assertEquals(only_post.pub_date.year, post.pub_date.year)
self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
self.assertEquals(only_post.pub_date.second, post.pub_date.second)
class AdminTest(LiveServerTestCase):
def test_login(self):
# Create client
c = Client()
# Get login page
response = c.get('/admin/')
# Check response code
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)

# Log the user in
c.login(username='bobsmith', password="password")
# Check response code
response = c.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)

#Used to log in don’t exist. Let’s resolve that.
#Now, you could put your own credentials in there, but that’s not a good idea because it’s a
# security risk. Instead, we’ll create a fixture for the test user that will be loaded when the tests are run. Run the following command:

$ python manage.py createsuperuser

#Give the username as bobsmith, the email address as bob@example.com, and the password as password.
# Once that’s done, run these commands to dump the existing users to a fixture:

$ mkdir blogengine/fixtures
$ python manage.py dumpdata auth.User --indent=2 > blogengine/fixtures/users.json

#This will dump all of the existing users to blogengine/fixtures/users.json. You may wish to edit this
#file to remove your own superuser account and leave only the newly created one in there.
#Next we need to amend our test to load this fixture:

class AdminTest(LiveServerTestCase):
fixtures = ['users.json']
def test_login(self):
# Create client
c = Client()
# Get login page
response = c.get('/admin/')
# Check response code
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)
# Log the user in
c.login(username='bobsmith', password="password")
# Check response code
response = c.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)

#Now, if you run python manage.py test, you should find that the test passes. Next, we’ll test that we can log out:

class AdminTest(LiveServerTestCase):
fixtures = ['users.json']
def test_login(self):
# Create client
c = Client()
# Get login page
response = c.get('/admin/')
# Check response code
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)
# Log the user in
c.login(username='bobsmith', password="password")
# Check response code
response = c.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)
def test_logout(self):
# Create client
c = Client()
# Log in
c.login(username='bobsmith', password="password")
# Check response code
response = c.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)
# Log out
c.logout()
# Check response code
response = c.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)

#This test works along very similar lines. We log in, verify that ‘Log out’ is in the response,
# then we log out, and verify that ‘Log in’ is in the response. Run the tests again, and they should pass.
# Assuming they do, let’s commit our changes again:

$ git add blogengine/
$ git commit -m 'Added tests for admin auth'

#This code is a little repetitive. We create the client twice, when we could do so only once. Amend the AdminTest class as follows:
class AdminTest(LiveServerTestCase):
fixtures = ['users.json']
def setUp(self):
self.client = Client()
def test_login(self):
# Get login page
response = self.client.get('/admin/')
# Check response code
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)
# Log the user in
self.client.login(username='bobsmith', password="password")
# Check response code
response = self.client.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)
def test_logout(self):
# Log in
self.client.login(username='bobsmith', password="password")
# Check response code
response = self.client.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log out' in response
self.assertTrue('Log out' in response.content)
# Log out
self.client.logout()
# Check response code
response = self.client.get('/admin/')
self.assertEquals(response.status_code, 200)
# Check 'Log in' in response
self.assertTrue('Log in' in response.content)

#The setUp() method is automatically run when the test runs, and ensures we only need to start up the
# client once. Run your tests to make sure they pass, then commit your changes:

$ git add blogengine/
$ git commit -m 'Refactored admin test'

#Now, we’ll implement a test for creating a new post. The admin interface implements URLs for
# creating new instances of a model in a consistent format of /admin/app_name/model_name/add/, so the
# URL for adding a new post will be /admin/blogengine/post/add/.

#Add this method to the AdminTest
class:
def test_create_post(self):

# Log in
self.client.login(username='bobsmith', password="password")

# Check response code
response = self.client.get('/admin/blogengine/post/add/')
self.assertEquals(response.status_code, 200)

#Try running it and this will fail, because we haven’t registered the Post model in the Django admin.
# So we need to do that. To do so, open a new file at blogengine/admin.py and add the following code:

import models
from django.contrib import admin
admin.site.register(models.Post)

#Now, run python manage.py test and the test should pass. If you want to confirm that the post model
# appears in the admin, run python manage.py runserver and click here.
#So now we can reach the page for adding a post, but we haven’t yet tested that we can submit one. Let’s remedy that:

def test_create_post(self):

# Log in
self.client.login(username='bobsmith', password="password")
# Check response code
response = self.client.get('/admin/blogengine/post/add/')
self.assertEquals(response.status_code, 200)
# Create the new post
response = self.client.post('/admin/blogengine/post/add/', {
'title': 'My first post',
'text': 'This is my first post',
'pub_date_0': '2013-12-28',
'pub_date_1': '22:00:04'
},
follow=True
)
self.assertEquals(response.status_code, 200)
# Check added successfully
self.assertTrue('added successfully' in response.content)
# Check new post now in database

all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 1)

#Here we submit the new post via HTTP POST, with all the data passed through. This mirrors the
# form created by the Django admin interface - if you take a look at the HTML generated by the
# admin, you’ll see that the inputs are given names that match these. Note that the pub_date field,
# because it represents a datetime object, is split up into a separate date and time field. Also
# note the parameter follow=True - this denotes that the test client should follow any HTTP redirect.
#We confirm that the POST request responded with a 200 code, denoting success. We also confirm that
# the response included the phrase ‘added successfully’. Finally we confirm that there is now a
# single Post object in the database. Don’t worry about any existing content - Django creates a
# dedicated test database and destroys it after the tests are done, so you can be sure that no
# posts are present unless you explicitly load them from a fixture.
#We can now test creating a post, but we also need to ensure we can test editing and deleting them.
# First we’ll add a test for editing posts:

def test_edit_post(self):
# Create the post
post = Post()
post.title = 'My first post'
post.text = 'This is my first blog post'
post.pub_date = timezone.now()
post.save()

# Log in
self.client.login(username='bobsmith', password="password")

# Edit the post
response = self.client.post('/admin/blogengine/post/1/', {
'title': 'My second post',
'text': 'This is my second blog post',
'pub_date_0': '2013-12-28',
'pub_date_1': '22:00:04'
},
follow=True
)
self.assertEquals(response.status_code, 200)
# Check changed successfully
self.assertTrue('changed successfully' in response.content)
# Check post amended
all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 1)
only_post = all_posts[0]
self.assertEquals(only_post.title, 'My second post')
self.assertEquals(only_post.text, 'This is my second blog post')

#Here we create a new blog post, then verify we can edit it by resubmitting it with
# different values, and checking that we get the expected response, and that the data in
# the database has been updated. Run python manage.py test, and this should pass.

#Finally, we’ll set up a test for deleting posts:
def test_delete_post(self):

# Create the post
post = Post()
post.title = 'My first post'
post.text = 'This is my first blog post'
post.pub_date = timezone.now()
post.save()
# Check new post saved
all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 1)
# Log in
self.client.login(username='bobsmith', password="password")
# Delete the post
response = self.client.post('/admin/blogengine/post/1/delete/', {
'post': 'yes'
}, follow=True)
self.assertEquals(response.status_code, 200)
# Check deleted successfully
self.assertTrue('deleted successfully' in response.content)
# Check post amended
all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 0)


#Again, this is pretty similar to what we did before. We create a new post, verify that
# it is the sole post in the database, and log into the admin. Then we delete the post via
# the admin, and confirm that the admin interface confirmed it has been deleted, and the
# post is gone from the database.

#I think it’s now time to commit again:
$ git add blogengine/
$ git commit -m 'Post admin tests in place'

#So we now know that we can create, edit and delete posts, and we have tests in place to
# confirm this. So our next task is to be able to display our posts.
#For now, to keep things simple, we’re only going to implement the index view - in other words,
# all the posts in reverse chronological order. We’ll use Django’s generic views to keep things really easy.
#Django’s generic views are another really handy feature. As mentioned earlier, a view is a
# function or class that describes how a specific route should render an object. Now, there are
# many tasks that recur in web development. For instance, many web pages you may have seen may be a
# list of objects - in this case, the index page for a blog is a list of blog posts. For that reason,
# Django has the ListView generic view, which makes it easy to render a list of objects.
#Now, like before, we want to have a test in place. Open up blogengine/tests.py and add the
# following class at the end of the file:

class PostViewTest(LiveServerTestCase):
def setUp(self):
self.client = Client()
def test_index(self):

# Create the post
post = Post()
post.title = 'My first post'
post.text = 'This is my first blog post'
post.pub_date = timezone.now()
post.save()

# Check new post saved
all_posts = Post.objects.all()
self.assertEquals(len(all_posts), 1)

# Fetch the index
response = self.client.get('/')
self.assertEquals(response.status_code, 200)

# Check the post title is in the response
self.assertTrue(post.title in response.content)

# Check the post text is in the response
self.assertTrue(post.text in response.content)

# Check the post date is in the response
self.assertTrue(str(post.pub_date.year) in response.content)
self.assertTrue(post.pub_date.strftime('%b') in response.content)
self.assertTrue(str(post.pub_date.day) in response.content)

#Here we create the post, and assert that it is the sole post object. We then fetch the index page,
# and assert that the HTTP status code is 200 (ie. the page exists and is returned).
# We then verify that the response contains the post title, text and publication date.
#Note that for the month, we need to do a bit of jiggery-pokery to get the month name. By
# default Django will return short month names (eg Jan, Feb etc), but Python stores months as
# numbers, so we need to format it as a short month name using %b.
#If you run this, you will get an error because the index route isn’t implemented. So let’s
# fix that. Open up the existing django_tutorial_blog_ng/urls.py file and amend it to look like this:

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
# Examples:
# url(r'^$', 'django_tutorial_blog_ng.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
url(r'^admin/', include(admin.site.urls)),
# Blog URLs
url(r'^.*$', include('blogengine.urls')),
)

#Then, create a new file at blogengine/urls.py and edit it as follows:
from django.conf.urls import patterns, url
from django.views.generic import ListView
from blogengine.models import Post
urlpatterns = patterns('',
# Index
url('^$', ListView.as_view(
model=Post,
)),
)

#A little explanation is called for. The project has its own urls.py file that handles routing
# throughout the project. However, because Django encourages you to make your apps reusable, we
# want to keep the routes in the individual apps as far as possible. So, in the project file, we
# include the blogengine/urls.py file.

#In the app-specific urls.py, we import the Post model and the ListView generic view.
# We then define a route for the index page - the regular expression ^$ will match only
# an empty string, so that page will be the index. For this route, we then call the
# as_view() method of the ListView object, and set the model as Post.

#Now, if you either run the tests, or run the development server and visit the index page,
# you’ll see that it isn’t working yet - you should see the error TemplateDoesNotExist:
# blogengine/post_list.html. This tells us that we need to create a template called
# blogengine/post_list.html, so let’s do that. First of all, add the following at the end of
# django_tutorial_blog_ng/settings.py:

# Template directory
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#Next, create the folders for the templates, and a blank post_list.html file:
$ mkdir templates
$ mkdir templates/blogengine
$ touch templates/blogengine/post_list.html

#Now, run your tests again, and you’ll see that the template now exists, but a new error is showing up:
Creating test database for alias 'default'...
......F

#======================================================================
#FAIL: test_index (blogengine.tests.PostViewTest)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#File "/Users/matthewdaly/Projects/django_tutorial_blog_ng/blogengine/tests.py", line 189, in test_index
#self.assertTrue(post.title in response.content)
#AssertionError: False is not true
#----------------------------------------------------------------------
#Ran 7 tests in 2.162s
#FAILED (failures=1)
#Destroying test database for alias 'default'...

#To fix this, we make sure the template shows the data we want. Open up
# templates/blogengine/post_list.html and enter the following:
#<html>
#<head>
#<title>My Django Blog</title>
#</head>
#<body>
#{% for post in object_list %}
#<h1>{{ post.title }}</h1>
#<h3>{{ post.pub_date }}</h3>
#{{ post.text }}
#{% endfor %}
#</body>
#</html>

#This is only a very basic template, and we’ll expand upon it in future.
#With that done, you can run python manage.py test, and it should pass. Well done! Don’t forget to commit your changes:
$ git add django_tutorial_blog_ng/ templates/ blogengine/
$ git commit -m 'Implemented list view for posts'

#And that’s all for this lesson! We’ve done a hell of a lot in this lesson - set up our project,
# created a comprehensive test suite for it, and implemented the basic functionality. Next time
# Make it a bit prettier using Twitter Bootstrap, as well as implementing more of the
# basic functionality for the blog.

$ python manage.py migrate

#This won’t actually make any changes, but it will ensure that all future changes to your models for the
# blogengine app are handled by South. Let’s commit our app skeleton:
$ git add django_tutorial_blog_ng/settings.py blogengine/
$ git commit -m 'Added blogengine app skeleton'