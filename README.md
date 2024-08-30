# Today-API

Today is a social media platform designed to cultivate gratitude and positivity in everyday life. Our platform provides users with a space to share the highlights of their day with others in a supportive online community.

## Features
- Highlight Sharing: Easily post and share the highlights of your day, complete with text descriptions and images.
- Interactive Features: Engage with other users' posts through likes, comments, and following other users.
- Search and Discovery: Explore posts by keywords and by following other users to find inspiration and connect with like-minded individuals.
- User Profiles: View your profile and share your posts with other users.
- Follow and Un-follow: Follow and un-follow other users to build a more engaged online community.

## Technologies Used
- A full list of the requirements and the versions used can be found in the requirements.txt file. The requirements.txt file.

## Languages And Frameworks
- Python
- Django Rest Framework

## Libraries And Tools
- Cloudinary - Image storage
- Pillow - Image processing
- Django Rest Auth - Authentication
- Django AllAuth - Authentication
- Psycopg2 - Python PostgreSQL Database Adapter
- Cors Headers - Cross-Origin Resource Sharing
- Gunicorn - Python WSGI HTTP Server
- PostgreSQL - Database

## Validation & Testing
- All files were passed through the Code Institute PEP8 Validation Tool and came back with no errors.

## Bugs
- There are no known unfixed bugs.

## Deployment
- Log into Heroku.
- Create a new app.
- Link the Heroku app to the repository.
- Go to Settings, click on Reveal Config Vars and add the ElephantSQL `DATABASE_URL`, `ALLOWED_HOST`, `CLIENT_ORIGIN` and the `CLOUDINARY_URL`.
- Click on **Deploy**.

