## For llm-app
### Creating a simple fast api application using llm - 
``` 
pip install "fastapi[all]"
uvicorn main:app --reload
```
### using Postman for testing

url - http://0.0.0.0:80/response
method - POST
Body(raw) - json

``` json
{
    "text": "who won the election?"
}
```
### docker
```
docker build -t llm-app .
docker run -d -p 8080:80 llm-app
```
