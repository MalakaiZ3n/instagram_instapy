from instapy import InstaPy
from instapy.util import smart_run
from secret import shamrock_username
from secret import shamrock_password

# login credentials
# insta_username = shamrock_username
# insta_password = shamrock_password

session = InstaPy(username=shamrock_username, password=shamrock_password,
                  headless_browser=True, disable_image_load=True, multi_logs=True)

with smart_run(session):
    """ Activity flow """

    # settings

    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=8500,
                                    max_following=8500,
                                    min_followers=100,
                                    min_following=33,
                                    min_posts=30,
                                    max_posts=None)

    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=False,
                                 peak_likes_hourly=60,
                                 peak_likes_daily=210,
                                 peak_comments_hourly=21,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=80,
                                 peak_unfollows_hourly=33,
                                 peak_unfollows_daily=48,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           no_profile_pic_percentage=100)

    session.set_do_follow(True, percentage=70, times=2)
    # session.set_do_comment(enabled=True, percentage=33)

    session.set_mandatory_language(enabled=True, character_set=['LATIN'])

    session.set_delimit_liking(enabled=True, max_likes=None, min_likes=12)

    session.like_by_tags(["cncmachining", "makinomachine", "cncmachine", "cncmachinist",
                          "aerospace", "aerospaceindustry", "5axis", "mechanicalengineering"], amount=6)

    session.set_dont_like(["naked", "nsfw", "peach", "booty", "sneaker", "airforceone",
                           "trump", "wood", "guitar", "decor", "challenge", "muzzle", "mexico", "france", ])


session.end()
