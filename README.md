## InstaScraper
A cool little bot that scrapes an instagram posts' comments does the following
- sentiment analysis
- complaint detection
- Is it computer science related or not?
- If the comment has been replied to if not a screen shot is taken!


### How to use it
```bash
git clone https://github.com/fear-the-reaper/instaScrape.git
```

### Using it locally
**Note: use a virtual environment!**

After the cloning the repo go in it
```bash
cd instaScrape
```

Install the required dependencies
```bash
pip install -r requirements.txt
```

Run the api
```bash
cd src
uvicorn main:app --reload
```

### Using docker
**Note: please make sure you have Docker installed in your system!**

Just up the `docker compose` file
```bash
docker-compose up
```


