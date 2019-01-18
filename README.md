# Parsing Science: Now in Flask

## Running locally
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Go to `http://127.0.0.1:5000/`

## Hosted Version

This is hosted by Python Anywhere at [www.parsingscience.com](www.parsingscience.com).

I followed the tutorial [here](https://mattcarrier.com/flask-dreamhost-setup/) to get the site hosted. 

### Notes
* I had to change my Flask app to use a Blueprint instead of regular routes. I'm not sure why.
