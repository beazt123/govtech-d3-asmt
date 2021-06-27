# Endpoints
## Summary
- []

## `GET /<id:int>`
### Query params
Param | Description
-|-
`id` | The unique identifier of the url

### Response
Redirects the client to the URL stored in the database


## `POST /shortener`
### JSON parameters
```js
{
    "url": "https://........"
}
```

### Sample Response
```js
{
    "url": "https://........",
    "url-short" : "http://localhost:5000/675853425677"
}
```


