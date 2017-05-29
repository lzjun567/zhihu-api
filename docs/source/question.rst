问题
==========
.. module:: zhihu


关注
-------
::

    import logging::
    logging.basicConfig(level=logging.INFO)

    from zhihu import Question
    data = Question(id=60231684).follow_question()
    或者
    data = Question(url="https://www.zhihu.com/question/60231684").follow_question()
    print(data)
    {'is_following': True}

取消关注
--------
::

    data = Question(id="60231684").unfollow_question()
    print(data)
    {'is_following': False}


.. module:: zhihu.models.question
.. autoclass:: Question
    :members:

