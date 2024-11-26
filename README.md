## For llm-app
### Creating a simple fast api application using llm - 
``` 
pip install "fastapi[all]"
uvicorn main:app --reload
```
### Using Postman for testing

url - http://0.0.0.0:80/response

method - POST

Body(raw) - json

``` json
{
    "text": "who won the election?"
}
```
### Docker
```
docker build -t llm-app .
docker run -d -p 8080:80 llm-app
```
