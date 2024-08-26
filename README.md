# Python Flask Paginate Test Server
This is a simple server that host an API that paginages through a set of users. I use
it for demo purposes and to test out clients.

- Build Docker container
```
docker build -t paginate .
```
- Run Docker container
```
docker run -d --name paginate --rm -p 5000:5000 paginate:latest
```

## Createw DB with different dataset
- Make sure you have python3 and flask installed on the machine you build the contianer

- Generate users database from users.csv
```
flask shell
>>> from shelltools import load_users_from_csv
>>> load_users_from_csv("./users.csv")
```
