回答
==========
.. module:: zhihu


点赞
-------
::

    import logging::
    logging.basicConfig(level=logging.INFO)

    from zhihu import Answer
    data = Answer(id=14005147).vote_up()
    或者
    data = Annswer(url="https://www.zhihu.com/question/60231684/answer/173983544").vote_up()
    print(data)
    {"voting": 1, "voteup_count": 314}

反对
--------
::

    data = Answer(id=14005147).vote_down()
    print(data)
    {"voting": 1, "voteup_count": 314}

中立
---------------------
::

    data = Answer(id=14005147).vote_neutral()
    print(data)
    {"voting": 1, "voteup_count": 314}

感谢
--------------------
::

    >>> from zhihu import Answer
    >>> Answer(url="https://www.zhihu.com/question/60231684/answer/173983544").thank()
    {'is_thanked': True}

取消感谢
--------------------
::

    >>> Answer(url="https://www.zhihu.com/question/60231684/answer/173983544").thank_cancel()
    {'is_thanked': False}
    >>>


.. module:: zhihu.models.answer
.. autoclass:: Answer
    :members:

