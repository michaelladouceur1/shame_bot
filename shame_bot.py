import praw
import re
import time

reddit = praw.Reddit(
	client_id='uRhOwwuU0flp4g',
	client_secret='rSG28eU22-7hCXwp0MNNlwRyap4',
	username='emoji_shame_bot',
	password='B1ackb1rd!23',
	user_agent='/u/emoji_shame_bot'
	)

# subreddits = ['funny', 'aww', 'interestingasfuck', 'oddlysatisfying']

emoji = ['😂','🤣','😍','🔥','💯','😳','👀','👌🏼','🤦🏼‍♂️','💀','😭']

reply = "This is the emoji_shame_bot! You've used an emoji.. Shame on you! We don't do that here!"

subreddit = reddit.subreddit('memes')
# print(subreddit)

comment_ids = []


def find_emoji_scum():
	for comment in subreddit.stream.comments():
		try:
			for em in emoji:
				if em in comment.body and comment.id not in comment_ids:
					reply = f"This is the emoji_shame_bot! You've used an emoji.. Shame on you, {comment.author}! We don't do that here!"
					print(reply)
					print(comment.body)
					comment.reply(reply)
					comment_ids.append(comment.id)
					print('waiting')
					time.sleep(20)
				else:
					continue
		except praw.exceptions.APIException as e:
			print(e)
			print('sleeping')
			if (e.error_type == 'RATELIMIT'):
				delay = re.search("(\d+) minutes", e.message)
				print(float(int(delay.group(1))))
				totTime = 0
				if delay:
					# delay_seconds = float(int(delay.group(1)) * 60)
					while totTime < float(int(delay.group(1))):
						print(totTime*60)
						time.sleep(30)
						totTime += 0.5
					find_emoji_scum()



find_emoji_scum()