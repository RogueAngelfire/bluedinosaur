### Blue Dinosaur Animation

* This project is for Peter Collins Stop Motion Animatior and Director of Blue Dinosaur animation.

* It will show case his work with the Use of Videos and images still from his projects

* I will have contact information and booking forms for assignments

* Services will be listed

### UX/UI

User Experience will be simple to navigate with ease of use. With user interface gathering information from the website with the option to see various music videos and a promo.

The idea that this won't be an over complicated website.

A test audience said they loved the website.

### Wire Fames and Mock ups

These Wireframe where designed 14 months prior to this design and was put on hold for
numerous reasons.

Since these designs I have started to use Adobe XD for wireframes as give an accurate
and more in depth look at what the final design would look like.

Noible changes I made was rather than have the logo transform I made the mouth operate
which is a lot better than I set out to do.

Home Page
![Wireframe Home Menu](bluedinosaur/media/wireframes/blue1.png)

About
![Wireframe Home Menu](bluedinosaur/media/wireframes/blue2.png)

Portfolio
![Wireframe Home Menu](bluedinosaur/media/wireframes/blue3.png)
Due to the limit in content the decision was made to consolodate the
Portfolio and service pages to feature on the about page only until
the time to expand with the clients additonal projects.

Services
![Wireframe Home Menu](bluedinosaur/media/wireframes/blue4.png)

Contact
![Wireframe Home Menu](bluedinosaur/media/wireframes/blue5.png)
Telephone number was dropped in the interest of establishing contact
client to client first. Blue Dinosaur have their number displayed therefore 
a client can contact Blue Dinosaur for ugent matter.

### User Stories

User Stories were concieved only from the point of view of the client  and what he requires at this stage.

1 Easy Navigation.
2 State Clearly my service.
3 Do not feature costs but have a web form for quote(s).
4 Have access to email data base as back up.
5 Display my previous work.
6 Link to Social media.
7 Receive mail from customers and return confirmation messages.

### Usability and Visual impact

This is probably the most simplistic navigation I have done on a website for 12 years but the simplicity adds to the magic of old school stop motion animation styles.

With the Dinosaur gif you are instantly drawn into the design and should be a selling point to my brothers skills in stop motion animation.

### Suitability for Purpose

This website is for my brothers Stop Motion Animation business.
It's sole purpose is to draw in indivials and small companies who would like a promotional video. Previous clients are mainly bands.

Ideally I think he would like to get a gig doing a christmas indent for a Television company.

### Navigations

Navigation is simple and has been reduced from 5 links to 3 those are Home, About and Contact.

### Ease of Use

The is a basic simplicity with only 3 pages to navigate. Home, about and contact
the about page features most of the information about the host and his portfolio of work.

The website can be navigated through easily. 

### Information and Achitecture

### Defensive Design

I do need to address some minor media queries on completion. However, I am happy with the responsive design as larger screens the dinosaur is walking from Right to left accoss the screen in a panning camera effect but reducing the screen to the smaller or portrait style format and it become an image of the same dinosaur but walking towards the device.

This is achieved using media queries and Bootstrap.

### Layout and Visual Impact: Responsive Design

### Image Presentation

### Colour Scheme and Typography

I went with a blue and black theme that kept continuty with the logo design.
I did try other colours but stuck with the basics.

After completion I am thinking of reducing the white text to a less intrusive and bright grey
but my brother the client is happy therefore, not a reason to change it for now.

The font Lato is used and so is Alfa Slab One. I intended to use Impact but a licence to use was required. This is the closest to the logo design of Blue Dionsaur animation.

### Languages Used for Blue Dinosaur Animations

I used the following for this assignment HTML, CSS, JavaScript and Python. I also used Markdown for this README document.

### Application features

* Home Page
* About Page
* Contact Page
* Web Form that contacts host and acknowledges client
* Links to web designer
* Social media links
* Focus on mobile first application
* Stores email information in administration

### E-Commerce

E-Commerce will be a stretch goal at a later stage in the meantime those requirements have been added now to reduce workload later.

### Authentication and Security Information

### Software Development Practises

Using Heroku see below for details

### Directory Structure and File naming

### Version Control

For this particular project I used Visual Studio Code and GitHub.

### Testing and Write Up

### Comments and Diary

### Django Instructions

Working with Visual Studio Code

  => ls (list)

	=> cd desktop (selects desktop file)

	=> mkdir bluedinosaur (this creates a folder called bluedinosaur)

	=> cd bluedinosaur (selects the folder)

	=> python3 -m venv venv ( creates a file venv)

	=> ls (check the listed file venv exists)

	=> source venv/bin/activate (This will activate the virtual environment - to check this works => which python )

	=> pip list

	=> pip install django (this will install django)

(Django will install)

ls ( This will show manage.py)

python3 manage.py runserver

(you will see local server and add to browser)

http://127.0.0.1:8000/

(Note 18 unapplied migration(s)  Therefore add the following:

python manage.py migrate

Ok will appear along side each migration.

I encountered an issue of the app missing manage.py so I added the following => django-admin startproject bluedinosaur

Now create a Super User for the Admin Panel.

  => python manage.py createsuperuser

Add your name, email address and create a password. Write this down and keep it safe or just memorise it.

In the terminal type the following:

  => python manage.py Runserver

In the URl add /admin like below:

http://127.0.0.1:8000/admin

Then apply your require credentials.

After the Admin type the following:

  => python manage.py startapp gwangi  (Gwangi is a famous blue dinosaur so couldn't resist)

NB The name gwangi was changed to keep continuity to bluedinosauranimation.

### Deployment Write ups

#### Setting up Heroku

* Log into the Heroku App with two tier security using authenticator on hand held device.

* Name the app in for example my_first_app

* If the required name is available you can proceed to the next step.

* Click on the resorces tab and select and type postgres in the seach part.

* In visual studio code click in the terminal and type the following: pip install dj_database_url if there is any problems try pip3 install dj_database_url

* Then: pip install psycopg2

* Now freeze the requirements in the terminal using the following.

* pip freeze > requirements.txt

* Click on the requirements.txt file to check these were installed correctly.

* Database information is now updated in the settings.py location.

* Now in the terminal I typed the following:

* python manage.py showmigrations

* Listed migrations will be shown. Then type:

* python manage.py makemigrations (A dry run can be done if required).

* Now type:

* python manage.py migrate

* I then set up a superuser with the following:

* python manage.py createsuperuser

* Apply the information required when prompted.

* An if statement was created on the database.py

* Now go back to the terminal and install gunicorn:

* pip install gunicorn

* Now on the same leve where there is the requirements.txt create new file and call it Procfile 

* Then time into Procfile the following:

* web: gunicorn herokuapplicationnamegoeshere.wsgi:application

* Now using the terminal log into Heroku.

* heroku login -i 

* Type in the following after login:

* heroku config:set DISABLE_COLLECTSTATIC=1 --app herokuapplicationnamegoeshere

#### AWS (Amazon Web Services)

* I logged into AWS as I have been here before I navigated easiy to S3

* Click the orange tab create bucket.

* I then turned on the static website hosting on clicking on my bucket. 

* I Added index.html and error.html where prompted.

* I then clicked on the permissions tab and then pasted in code from the CORS (Cross origin Resorce Sharing).

* Select Bucket Policy then policy generator so as to create a security policy.

* Policy type is S3 Bucket Policy Allow all policies by adding * to the box, Action is get object.

* From the previous tab still open from when opening the policy generator.

* Now copy the bucket ARN (Amazon Resorce Name) then paste it at the bottom of the policy generator where prompted.

* Click add statement then generate the policy.

* Copy the Json Code in the document and paste in bucket policy editor.

* Before saving add a */ within the quotations after the project name.

* Click Save

* Now scroll down to access control list and click edit.

* Check the list box for Everyone (Public Access) then click the box stating you understand the effects of the changes made on the objects and buckets.

* Save again

* I then click sevices link.

* Select set group name and add name - again I made this simple and similar to previous names

* Now click next step twice and create the group
The click policy then policies and select the Json tab.

* Then click import managed policy from the pre build amazon policies.

* Use the filter search and type S3 and import the AmazonS3Fullaccess Policy.

* Using the Bucket ARN from the previous created bucket policy page in S3.

* Copy and paste it in the Json code on the line with resources as follows: line 7, "resources": [ line 8, "arn:information goes here", line 9, "arn:information goes here/*" line 10, ]

* Click review policy

* Give it a name and a description I added -policy after the title.

* Click Create policy then groups select the one just made followed by permissions.

* Then attach policy

* Search for policy just created and select it and click attach policy.

* Now create a user to put in the group, so click users on the far left side of the panel.

* Then add user

* Add username (your project name)-staticfiles-user.

* Allow programmatic access

* Then select next

* Now click Appropriate policy then click the next:tag then next:review

* Then click create user

* Now download the .CSV file

* IMPORTANT to download and save as cannot do this again.

* Then close the window

* At this stage add the AWS instructions to the settings.py page
After deploying to Heroku and Github with push command simultaneously

* Click on the bucket in S3

* Within the object tab next to the word lits version click the refresh button and the static file will appear.

* Add the cache control statement that can be seen in settings.py
Now goto S3 and on the bucket overview click create folder and call it media and click create folder.

* Now click on that folder

* Inside click upload and add files.

#### Linking Heroku to a Fasthosts Domain

I already had a domain for the client for the past 3 years with Fasthosts.

* Log into Heroku
* You will be prompted by authenticator for two tier seccurity. Allow access.
* Select the appropriate project.
* Go to settings and scroll down to and click add domain.
* Add you purchased domain and make sure you add www. to the domain name.
* Heroku will generate a code below which needs to be copied.
* Log into Fasthosts
* Click on the Domain Names in the left hand panel.
* Your domain will be listed here click DNS on the appropriate domain if you have more than one.
* Scroll down to CNAME Record and click add.
* HOST NAME should be www
* POINTS TO should be the code obtain from Heroku. Paste it here and save.
* Scroll back to the top of the page and click the tab for web forwarding below the domain name.
* Enable Forwarding with check box.
* Add destination URL rather than http I used https as will be useful if this site uses eCommerce in the future.
* Select Redirection Type 301 - Moved Permanently
* Then Save. This can take time to change experience says 3 minutes to 3 hours. However, after ten minutes I generally double check for spellling errors.
* Head Back to Heroku
* Click on overview and click on configure Dynos I then added dyno for $7 per month to enable an SSL Certificate.
* This can now be seen on the settings page.
* Type you domain address and if executed correctly you will see you website from domain location address.

### Stretch Goals - What is for the future

Future plans will be to have a login and payment system with a clients area.

As It stands it will remain a static website until client choses to progress.

If addditional content is added to for example the about page. I will add an arrow for
quick scroll back to top of the page.

### Media

All images and videos supplied by Peter Collins at Blue Dinosaur Animation

Blue Dinosaur Logo Design is by Robin Collins (Myself).

### Technologies Used


* Django
* GitHub
* Visual Studio Code
* Heroku
* Google Fonts
* HTML Formatter
* Bootstrap 
* Balsamiq
* Adobe Photoshop
* Homebrew
* Repl.it
* Django Key Generator
* AWS S3 Bucket
* Allauth
* GUincorn
* Boto3
* Gmail
* PIP
* Psycopg2
* DJ_Database
* S3Transfer


### Credits and Acknowledgements

Write up is by Peter Collins

A special thank you goes to Ashur Kanwal who reminded me I have the skills, thanks mate for the support.