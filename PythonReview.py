def create_youtube_video(title, description):
    return {
        "title": title,
        "description": description,
        "likes": 6,
        "dislikes": 2,
        "comments": {"nice", "really helped me", "very good"}
    }

def like(video):
    if "likes" in video:
        video["likes"] += 1
    return video

def dislike(video):
    if "dislikes" in video:
        video["dislikes"] += 1
    return video

def add_comment(video, username, comment_text):
    video["comments"][username] = comment_text
    return video

my_video = create_youtube_video("Python Basics Tutorial", "Learn the fundamentals of Python programming.")
print(my_video)