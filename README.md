# Parsing Science: Now in Flask

## Running locally
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Go to `http://0.0.0.0:5000/`

## Hosted Version

This is hosted by Dreamhost at [www.parsingscience.com](www.parsingscience.com).

I followed the tutorial [here](https://mattcarrier.com/flask-dreamhost-setup/) to get the site hosted. 

### Notes
* I couldn't get the interpreter code to work so I posted in the results of `which python`. 
* I had to change my Flask app to use a Blueprint instead of regular routes. I'm not sure why.
* I was not able to get [logging](https://help.dreamhost.com/hc/en-us/articles/215769548-Passenger-and-Python-WSGI) to work. I believe this may partly be because the examples on Dreamhost are written for Django. 
