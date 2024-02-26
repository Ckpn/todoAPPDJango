from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.

#modelse slug eklemek icin 'django autoslug' pip yapmak lazım
class Todo(models.Model):
    todo = models.CharField(max_length = 100) #charfield ile text input alırız
    slug = AutoSlugField(populate_from='todo',unique = True)  #sabit bir kalıp olarak autoslug ekleriz
    user = models.ForeignKey(User,on_delete =  models.CASCADE) #silindiğinde ilişkiyi bitir 
    # on_delete eşitliği bunu sağlar
    
    def __str__(self):
        return self.todo

