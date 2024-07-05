# Python web scraping learning project

only requires the website domain, and it will get through a POST request all the emails found on it

## Improvements :

- Taking an string input as domain url
- Checks if its a valid url
- Gives a view of the logs currently running
- Gives the object and the option to download it
- Timeout if website too big (no scraping on ytb for example)

## how to use :

launch the server endpoint (in py_email_scraping folder) :

```
python app.py
```

then your server is now listening to your queries so you can (modify your scraped domain as you like) :

```
curl -X POST http://127.0.0.1:5000/scrape -H "Content-Type: application/json" -d '{"domain": "example.com"}'
```
