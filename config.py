from random import randint

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***IMPORTANT***

Please be aware of Instagram's daily limits for likes and comments to avoid getting banned

https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Local path to chrome driver
chromedriver_path = "C:/Users/JohnC/Desktop/Instagram-Like-Comment-Bot/chromedriver.exe"


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Make adjustments below to tweak the bot to your liking

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# List of hashtags to go through
hashtag_list = ['맛집리뷰']

# List of comments to be randomly chosen from
comments_list = ['Love this!', 'Nice shot :)', 'Amazing~', 'Looks great! :)', 'Beautiful']
# Number of posts to go through per hashtag
number_of_posts = 100

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 2

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(0, 1)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
wait_to_comment = randint(0, 1)

# If Want to Enable "Like"
enable_like = True

# If Want to Enable "Comment"
enable_comment = False