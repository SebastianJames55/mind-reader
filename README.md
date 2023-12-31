Mind-reader is an app built using [mindsdb](https://mindsdb.com/). The app aims to provide mental support to people who are going through tough times. 

## Features 
- Chat support

## Local Setup
- [Get an OpenAI API key](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)
- [Set up mindsdb locally](https://docs.mindsdb.com/setup/self-hosted/pip/source)
  - `mind-reader` relies on OpenAI. So, for the `mindsdb` setup, additionally install the dependencies at `mindsdb/integrations/handlers/openai_handler/requirements.txt`
  - Start the server: `python -m mindsdb`
- Clone the mind-reader repo: `git clone https://github.com/SebastianJames55/mind-reader.git`  

- Create a new [virtual environment](https://www.geeksforgeeks.org/python-virtual-environment/) (recommended)

  Following are the steps to follow on Windows  
  Create virtual environment: `python -m venv mind-reader-venv`  
  
  Create a file `venv_vars.bat` in `\mind-reader-venv\Scripts\`.  
  In `venv_var.bat` add the following:
  ```
  @echo off
  set OPENAI_API_KEY=your-openai-api-key
  ```
  At the end of `activate.bat` in `\mind-reader-venv\Scripts\`, add: `call venv_vars.bat`
  
  Now, activate the venv:  `.\mind-reader-venv\Scripts\activate.bat`
- Install the prerequisities: `pip install -r requirements.txt`
- Run the mind-reader app: `py app.py`
- Navigate to ```http://127.0.0.1:5000/api/v1/```.  
  Under `predict`, click on `Try it out`. Enter a text against `request_message` and click on `Execute`.  
  Here's an example of a chat input and reply.  
  ![Chat input](assets/simple%20rq.PNG)  
  
  ![Chat reply](assets/good%20rs.PNG)  
- Please refer to the [demo](https://www.youtube.com/watch?v=qmnaoTaws3w) & [article](https://sebastianjames.hashnode.dev/mind-reader-your-buddy-to-chat-with-when-you-are-on-a-low) for more details on the idea and implementation

### Additional Info
- API documentation included for the ```/api/v1/predict``` endpoint using Flask-RESTx. 
- The Swagger documentation will be available at ```/api/v1/swagger.json``` or ```/api/v1/``` when you run the application.
