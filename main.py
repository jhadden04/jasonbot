import praw
import time
reddit = praw.Reddit(client_id='2WHqLvf5aRq3tQ',
                     client_secret='J1WHeJffj_QlK5pvom_qKPJUYsVA4Q',
                     user_agent='a reddit instance',
                     username='FranchescaScola',
                     password='12qwaszxX@1zp')

def subspam():
    misctext = """Message from John, original owner of thcdelivery, https://www.realthcdelivery.com/

Want to let you know that the REAL THC DELIVERY has extended its sale until this thursday:

SITE WIDE 50% OFF SALE

Use Coupon Code : RealTHCD At Checkout"""  # you need to change this to your message

    subname = 'CanadianMOMs+canadients'  # obviously you can add more subreddits to this
    usedusernames = []
    for comment in reddit.subreddit(subname).stream.comments():
        name = comment.author.name
        title = f'Dear, {name}'
        if name in usedusernames:
            continue
        try:
            text = misctext
            reddit.redditor(name).message(title, text)
        except:
            continue
        usedusernames.append(name)
        print(f'u/{name} r/{comment.subreddit.display_name}')
        time.sleep(40)
subspam()
