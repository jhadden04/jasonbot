import praw
import time

reddit = praw.Reddit(client_id='2WHqLvf5aRq3tQ',
                     client_secret='J1WHeJffj_QlK5pvom_qKPJUYsVA4Q',
                     user_agent='a reddit instance',
                     username='FranchescaScola',
                     password='mnkjoi09M)')


def subspam():
    misctext = """John here, original owner of thcdelivery, https://www.realthcdelivery.com/
messaging you all of you to let you know that the
REAL THC DELIVERY Will be doing a Friday Flash Sale :

SITE WIDE 50% OFF SALE

Use Coupon Code :
RealTHCD
At Checkout"""

    subname = 'CanadianMOMs+canadients'  # obviously you can add more subreddits to this
    usedusernames = []
    while True:
        for comment in reddit.subreddit(subname).stream.comments():
            name = comment.author.name
            title = f'Dear, {name}'
            nametxt = f'{name}\n'
            if name in usedusernames:
                continue
            b = open("names.txt", "r")
            if nametxt in b:
                continue
            try:
                text = misctext
                reddit.redditor(name).message(title, text)
            except:
                continue
            usedusernames.append(name)
            f = open("names.txt", "a")
            f.write(nametxt)
            print(f'u/{name} r/{comment.subreddit.display_name}')
            time.sleep(40)
            break


subspam()
