from app import app, models

app.debug = True

#app.host = '0.0.0.0'
#app.port = 8080


models.mysql_db.create_tables([models.Blogpost], safe=True)

app.run(host='0.0.0.0', port=8080)

db = models.mysql_db
