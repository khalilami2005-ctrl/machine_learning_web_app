## Heroku [Optional]
![](Readme_img/heroku.png)

- https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd
- https://towardsdatascience.com/deploying-a-basic-streamlit-app-to-heroku-be25a527fcb3
- https://www.analyticsvidhya.com/blog/2021/06/deploy-your-ml-dl-streamlit-application-on-heroku/

## Podcasts

## [optional] Ship the Dockerfile to DockerHub   

![](Readme_img/dockerhub.png)

So that one can run this project with one simple Docker commandline.


## Save your machine learning model as local file

![](Readme_img/modelling.jpg)


##  [optional] Frontend plus Backend, in Docker Compose 


## MySQL Docker
Add:
![](Readme_img/mysql.png)

If ever you need a MySQL backend ... use Docker!

```shell script
sudo docker network create mysql-network
sudo docker run --name=container_mysql -p7106:3306 -e MYSQL_ROOT_HOST='%' -e MYSQL_ROOT_PASSWORD=lundechen -d --net mysql-network mysql/mysql-server 
sudo docker run --name container_phpmyadmin --link container_mysql:db -p 7880:80 -d  -e PMA_HOST=container_mysql --net mysql-network phpmyadmin/phpmyadmin
```

```mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'lundechen';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'lundechen';
```