from zhihu import Answer


def vote_up_with_id():
    data = Answer(id=14005147).vote_up()
    print(data)

if __name__ == '__main__':
    vote_up_with_id()