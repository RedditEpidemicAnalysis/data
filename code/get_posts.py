import pathlib
import praw
import jsonlines as jl
import progressbar as pb
from argparse import ArgumentParser
from typeguard import typechecked

@typechecked
def get_posts(subreddit: str, file_out: pathlib.Path) -> None:
    """
    Parameters
    ----------
    subreddit : str
        The name of the subreddit
    file_out : pathlib.Path
        File containing the posts measures
    """

    reddit = praw.Reddit()
    print(f'Read-Only mode: {reddit.read_only}')

    posts = 1
    widgets = [ 'Posts # ', pb.Counter(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']'), ' ', pb.Timer()]
    with pb.ProgressBar(widgets = widgets) as bar:
        with open(file_out, 'w', encoding = 'utf-8') as fp:
            with jl.Writer(fp, compact = True, sort_keys = True) as writer:
                for submission in reddit.subreddit(subreddit).new():
                    bar.update(posts)
                    posts = posts + 1
                    json = _extract_post(submission)
                    writer.write(json)

@typechecked
def _extract_post(submission: praw.models.reddit.submission.Submission) -> dict:
    result = {}
    
    result['id'] = submission.id
    result['text'] = submission.selftext
    result['date'] = submission.created_utc
    result['author'] = submission.author_fullname
    result['comments'] = submission.num_comments
    result['votes'] = submission.ups
    result['score'] = submission.score

    return result

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-subreddit', '--subreddit',
        help = 'The name of the subreddit',
        type = str,
        required = True)
    parser.add_argument(
        '-out', '--file-out',
        help = 'File containing the posts measures',
        type = pathlib.Path,
        required = True)
    args = parser.parse_args()
    print(f'subreddit: {args.subreddit}')
    print(f'file out: {args.file_out}')
    get_posts(args.subreddit, args.file_out)
