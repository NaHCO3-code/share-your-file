# share-your-file
you can share you file to others.

# get started
1. mask sure you installed **`flaskr`, `gevent`, and `execjs`**.
2. implement database with command **`flask init-db`**
3. **`flask run`!**


# user ID
user ID = int(str(random.randint(10,99))+str(int(time.time()*1000)))


# fileNode
> filesharer/ *`(main forder)`*
>
>> database/ *`(implement database)`*
>>
>>> database.py *`(implement database commands and functions)`*
>>>
>>> db.sql *`(database commands)`*
>
>> static/ *`(static files)`*
>>
>>> css/
>>
>>> fonts/
>>
>>> js/
>>>
>>>> md5.js *`(md5 encryption)`*
>
>> templates/ *`(Jinja templates)`*
>
>> app.py
>
>> 历史小测.md (雾霾)