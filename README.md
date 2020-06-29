# Bilder
#### A Django personal photo gallery app, 29/06/2020
#### By [Collin Owino](https://github.com/Collin9726)

### [Bilder app](https://mybilderapp.herokuapp.com/)

<img src="./static/app-images/bilder-home.png"
     alt="Bilder home image"
     style="width=100%;" />

## Description

<table>
<tr>
<td>
Bilder is a personal web gallery app made with Django. Through the app users can view the photos you post, search for photos by category, sort photos by location, and view a single photo together with it's details and captions. Users are also able to share links to the images they like. 
<br><br>
The app has an admin page through which an account owner is able to upload, update or delete an image. Here, they can also create new categories and locations and tag them to their images.
</td>
</tr>
</table> 

#### Latest updated version is on 15th June 2020.

## Technologies used

1. Python v3.6
2. Flask 1.1.2
3. Postgres
4. SQLAlchemy
5. Flask-Bootstrap
6. HTML & CSS

## Development

The app has been developed with Flask 1.1.2. It uses PostgreSQL database and SQLAlchemy. Database migrations are tracked with ALembic. Email communication uses the Google SMTP server. The app is deployed on Heroku. It's source code is available on GitHub at https://github.com/Collin9726/codescripts

## Setup & Run instructions
- Install the dependencies listed on `requirements.txt`.
- Configure your app to include `SECRET_KEY`, `MAIL_USERNAME`, `MAIL_PASSWORD`, among other environment variables as listed in `start.sh.sample`
- Run your app on `development` config for debugging purposes.

To contribute to this project on any modules, follow these easy steps:

- Fork the repo
- Create a new branch in your terminal (git checkout -b improve-feature)
- Make appropriate changes in file(s)
- Add the changes and commit them (git commit -am "Improve App")
- Push to the branch (git push origin improve-app)
- Create a Pull request

## Support and contact details
For any queries, issues, ideas or concerns contact [Collin Owino](owino.collin@gmail.com). Your feedback is highly appreciated. 
### [License](LICENSE)
MIT license
Copyright (c) 2020 **Collin Owino**