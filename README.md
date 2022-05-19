# Personal-blog
This is  a personal blogging website where users can create and share their opinions and other users can read and comment on them it also has a feature to  display random quotes to inspire the  users. 
The project's live link is https://psl-blog.herokuapp.com/
## By Mercy Wairimu

<img src="https://raw.githubusercontent.com/Mercywairimu01/Personal-blog/main/app/static/photos/Screenshot%20from%202022-05-19%2015-34-12.png">
## Technology Used

1. Python3
2. Flask version 2
3. HTML, CSS and JavaScript
4. Flask Login, email validator, and password validator
5. Shell

## Project Requirements & Prerequisites

1. IDE of Choice
2. Python3
3. Browser

* Please ensure you're working from a Windows/MacOS/Linux
* Install Flask through `pip install flask`

## Project Setup and Installation

1. Proceed to this [link](https://github.com/Mercywairimu01/Personal-blog) and clone the repository.
2. Extract the folder and `cd` to the folder on your terminal or your prefered IDE
3. In the terminal, create a virtual/flask environment: `python3 -m venv virtual` and activate it through `source virtual/bin/activate`. In the case of flask, please use `source flask/bin/activate` or refer to this [documentation](https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask) for Flask virtual environment installation.
4. Install all dependencies from the `requirements.txt` file; use `pip` to install needed dependencies.
5. In the project folder, create a `start.sh` file which acts as a server at runtime.
6. In the terminal, and within the project folder, run `chmod +x start.sh` and `./start.sh` to start the project.
7. View the application on your browser on `http://127.0.0.1:5000`. If you have another project running on another port, use `flask run --host 0.0.0.0 --port 5001` to switch to a new port; You can use a different port number.

## Behavior Driven Development (BDD)

The BDD focuses on how a user interacts with the application.

At a minimum, this is what the user should experience in the application:


| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|

## Project Contribution or Development:

To contribute to this project, please follow the following steps:
* Fork this repository.
* Create a branch: `git checkout -b <branch_name>`.
* Make your changes and commit them: `git commit -m '<commit_message>'`
* Push to the original branch: `git push origin <flask-news>/<main>`
* Create the pull request.
* Once a PR is reviewed, the changes will be pushed to the main branch for integration.

Please see the GitHub documentation on [Creating a Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)

## Known Issues & bugs

No known bug at pduring development.If you come across a bug reach out to the contacts below.
[mercy.mambui@student.moringaschool.com](mailto: mercy.mambui@student.moringaschool.com)
## License
MIT

Copyright (c) 2022 Mercy Wairimu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
## Authors Info
Email: mercy.mambui@student.moringaschool.com