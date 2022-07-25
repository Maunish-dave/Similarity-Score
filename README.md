# Similarity-Score
Flask API for calculating similarity of two sentences

To run this project follow follwing steps.

**build docker container**
```cmd
sudo docker build --tag  similarity .
```

**run docker container**
```cmd
sudo docker run -d -p 5000:5000 similarity
```

you can test it using this command or postman

```cmd
curl -X POST -H "Content-type: application/json" -d "{\"sentence1\" : \"how are you?\", \"sentence2\" : \"how are you doing\"}" "localhost:5000/similarity/"
```
**postman example**

![image](https://github.com/Maunish-dave/Similarity-Score/blob/main/postman_example.png)