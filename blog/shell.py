"""C:\Users\kparmar7\eclipse-workspace\django_project>py manage.py shell
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: kparmar7>]>
>>> User.objects.first()
<User: kparmar7>
>>> User.objects.filter(username='Kashyap')
<QuerySet []>
>>> User.objects.filter(username='Kashyap7')
<QuerySet []>
>>> User.objects.filter(username='kparmar7')
<QuerySet [<User: kparmar7>]>
>>> User.objects.filter(username='kparmar7').first()
<User: kparmar7>
>>> user= User.objects.filter(username='kparmar7').first()
>>> user
<User: kparmar7>
>>> user.id
1
>>> user.pk
1
>>>  user= User.objects.get(id=1)
TypeError: Post() got an unexpected keyword argument 'contnet'
>>> post_1=Post(title='Blog 1', content='First Post Content!!', author=user)
>>> Post.objects.all()
<QuerySet []>
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
>>>  exit()"""

"""C:\Users\kparmar7\eclipse-workspace\django_project>py manage.py shell
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)
] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>]>
>>> user= User.objects.filter(username='kashyap7').first()
>>> user
None
>>> user= User.objects.filter(username='kparmar7').first()
>>> user
<User: kparmar7>
>>> post_2=Post(title='Blog 2', content='Second Post Content!!', author_id=user.id)
>>> post_2.save()
>>> Post.objects.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
>>> post=Post.objects.first()
>>> post
<Post: Blog 1>
>>> post.content
'First Post Content!!'
>>> post.date_posted
datetime.datetime(2019, 10, 9, 12, 28, 9, 654625, tzinfo=<UTC>)
>>> post.author
<User: kparmar7>
>>> post.author.email
'kparmar7@dxc.com'
>>> user.post_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.
<locals>.RelatedManager object at 0x06381BF0>
>>> user.post_set.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
>>> user.post_set.create(title='Blog 3', content='Third Post Content!!')
"""