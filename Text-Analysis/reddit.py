import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="c7WTK4PN9373N4ZyLVbgcA",
    client_secret="oPwLcsM3brsybFsN2VYp1CkaM9YTWA",
    user_agent="my-app by u/Wild_Ambassador_2813"
)

keywords = ["ManchesterUnited", "NBA"]

title_data = []

for key in keywords:
    subreddit = reddit.subreddit(key)

    top_posts = subreddit.top(limit=100)
    # new_posts = subreddit.new(limit=100)

    for post in top_posts:
        print("Title - ", post.title)
        title_data.append({"Title": post.title, "Category": key})
        # print("ID - ", post.id)
        # print("Author - ", post.author)
        # print("URL - ", post.url)
        # print("Score - ", post.score)
        # print("Comment count -", post.num_comments)
        # print("Created -", post.created_utc)
        # print("\n")

df = pd.DataFrame(title_data)
print(df)

df.to_csv("./Text-Analysis/dataset/reddit_titles.csv", index=False)
