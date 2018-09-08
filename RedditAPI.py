# PRAW
import praw
import prawcore.exceptions
import praw.exceptions

# Misc. helpers
from datetime import datetime

class RedditComment:
    def __init__(self, subreddit, numReplies, score, dateTime, commentText, id):
        self.subreddit = subreddit
        self.numReplies = numReplies
        self.score = score
        self.dateTime = dateTime
        self.date = self.dateTime.date()
        self.commentText = commentText
        self.id = id

    def getMinimalInfo(self):
        info = {'subreddit': self.subreddit, 'commentText': self.commentText,
                'score': str(self.score), 'date': str(self.date),
                'id': str(self.id)}
        return info

class RedditAPI:
    def __init__(self):
        self.reddit = praw.Reddit(client_id = ' ',
                                  client_secret = ' ',
                                  username = ' ',
                                  password = ' ',
                                  user_agent = ' ')

    def getUserComments(self, username):
        resultList = []
        for comment in self.reddit.redditor(username).comments.new(limit=100):
            resultList.append(RedditComment(
                comment.subreddit.display_name,
                0,
                comment.score,
                datetime.fromtimestamp(comment.created_utc),
                comment.body,
                comment.id))
        return resultList

    def userExists(self, username):
        exists = True
        if username is not None:
            try:
               self.reddit.redditor(username).fullname
            except prawcore.exceptions.NotFound:
                exists = False
            except prawcore.exceptions.BadRequest:
                exists = False
        return exists

    def submissionExists(self, submission):
        exists = True
        if submission is not None:
            try:
                self.reddit.submission(url=submission).fullname
            except prawcore.exceptions.NotFound:
                exists = False
            except praw.exceptions.ClientException:
                exists = False
        return exists

    def getSubmissionTopLevelComments(self, submissionURL):
        resultList = []
        submission = self.reddit.submission(url=submissionURL)
        for topLevelComment in submission.comments:
            resultList.append(RedditComment(
                topLevelComment.subreddit.display_name,
                0,
                topLevelComment.score,
                datetime.fromtimestamp(topLevelComment.created_utc),
                topLevelComment.body,
                topLevelComment.id))
        return resultList