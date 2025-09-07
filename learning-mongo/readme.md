# Install mogosh

https://www.mongodb.com/docs/mongodb-shell/install/

brew install mongosh

# Installing mongo

https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/

docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest

docker container ls

# Connect to the MongoDB Deployment with mongosh

mongosh --port 27017


