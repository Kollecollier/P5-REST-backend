# The METAL BLOG - API
The Metal Blog is a social media image and blog based platform for metal lover's. Here, users can share there images and express themself freely on a metal based webpage. We also invite users to interact with each other by commenting and liking other user's content. This section of the project is the backend API database built to support the ReactJS frontend, and it is powered by the Django Rest Framework.

#### DEPLOYED BACKEND API: [Click Me!](https://p5backend.herokuapp.com/)
#### DEPLOYED FRONTEND: [Click Me!](https://p5front.herokuapp.com/)
#### FRONTEND REPOSITORY:[Click Me!](https://github.com/Kollecollier/p5reactfront)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
+ [Technologies Used](#technologies-used "Technologies Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")

# User Stories:
All User Stories have been documented in their own file instead of in a project with issues, you can find there [HERE!](https://github.com/Kollecollier/backend_p5/blob/main/Userstories)

# Database:
![SQL Database model](https://res.cloudinary.com/kolle1993/image/upload/v1672656063/P5%20Readme/Namnl%C3%B6s_mgnecq.png)

# Testing:

### Validator Testing: 
## State: Pep8 online is down, instead pycodestyle has been installed on this and all red marked codes have beem corrected!


### Manual Testing:
1. Manually verified each url path created works & opens without error.

2. Verified that the CRUD functionality is available in each app via the development version: Comments, Followers, Likes, Posts, Profiles
 - Checked this by going to each link.
 - Creating a new item.
 - Checking new item URL path. 
 - Editing the item (not available for Likes, Followers or Users)
 - Deleting the item (Not available for Users or Profiles)

## In general the backend seem's to be working good without any error's.

### Unfixed Bugs
- No more bugs can be found.

# Technologies Used:
### Main Languages Used:
- Python

# Frameworks & Programs Used:
- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Extention's used:
 - Auto Close Tag
 - Auto open preview panel
 - Prettier
 - Bootstrap 4
 - django
 - ES7
 - Groovy lint
 - Html Css support
 - isort 
 - Jupyter, keymap, notebook
 - python
 - React snippet

 # Deployment:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:

- 'django<4'
- dj3-cloudinary-storage
- Pillow
- djangorestframework
- django-filter
- dj-rest-auth
- 'dj-rest-auth[with_social]'
- djangorestframework-simplejwt
- dj_database_url psycopg2
- gunicorn
- django-cors-headers

5. Created the Django project with the following command:

django-admin startproject project_name .

6. Back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:

 - ALLOWED_HOST - p5backend.herokuapp.com

 - CLIENT_ORIGIN - https://p5front.herokuapp.com

 - CLIENT_ORIGIN_DEV - https://3000-kollecollie-p5reactfron-jgtdnujaug5.ws-eu71.gitpod.io

 - CLOUDINARY_URL - cloudinary://198849925326778:f_9w7ZNkDTNqiCeNBCrLQjvLcVU@kolle1993

- DATABASE_URL - postgres://xzkbajpjeeapee:142aa55701463f2746804464962a0fcbf50f7db52b9c2b68d9267cf10b0b998e@ec2-63-35-156-160.eu-west-1.compute.amazonaws.com:5432/d57ajabqmul1ti

- DISABLE_COLLECTSTATIC - 1

- SECRET_KEY - Value Hidden

8. Created the env.py file, and added the following variables:

import os
- os.environ['CLOUDINARY_URL'] = 'cloudinary' / hidden
- os.environ['DEV'] = '1'
- os.environ['SECRET_KEY'] = "hidden"
- os.environ['DATABASE_URL'] = "postgres hidden"

## In Settings.py:

9. Installed apps:

![Settingsapps](https://res.cloudinary.com/kolle1993/image/upload/v1672658346/P5%20Readme/apps_h5ueea.png)


10. Import's for database:

![Imports](https://res.cloudinary.com/kolle1993/image/upload/v1672658565/P5%20Readme/imports_buhyks.png)

11. Cloudinary and media storage.

![Mediastorage](https://res.cloudinary.com/kolle1993/image/upload/v1672658565/P5%20Readme/storage_exqhck.png)

- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```

12. Rest Framework: include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],

    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DATETIME_FORMAT': '%d %b %y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```

15. User Serializers:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'DEV' in os.environ
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```

18. Added the Heroku app ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [Code Institute Rest walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost'
]

if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [os.environ.get('CLIENT_ORIGIN')]


if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
 ```

20. Corsheader's middleware added:
```
'corsheaders.middleware.CorsMiddleware',
```

21. Cros Credentials (As recommended in walkthrough):

```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```

### Final steps:
- Created a Procfile with the following:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn p5backend.wsgi
```
- Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- Froze requirements:
```
pip3 freeze --local > requirements.txt
```
- Added, committed & pushed the changes to GitHub
Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
-  Deployed the branch.

# CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- Giving some credit to the C.I Tutor and Mentor support for being a solid source of help.

## Contact:
If you have any question's or need to contact me:

- Email: kristoffer.collier@live.se
- [GitHub](https://github.com/Kollecollier)
- [Facebook](https://www.facebook.com/kristoffer.collier/)
- [Linkedin](https://www.linkedin.com/in/kristoffer-collier-2b972b40/)
