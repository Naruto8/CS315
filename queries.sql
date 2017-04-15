/*Selects ID of tweets which are short and tweeted by someone with followers>100*/
SELECT tweet_id
FROM tweets
WHERE LENGTH(tweet_text) < 50
	user_id IN(
	SELECT user_id
	FROM users
	WHERE followers_count > 100
)

/*User name of those whose location starts with "In" and account created in 2017*/
SELECT screen_name
FROM users
WHERE location="In*" AND CAST(created_at as DATE) >= '2017-01-01'

/*Selects ID and text of tweets by those with a particular name format and friends<100*/
SELECT tweet_id, tweet_text
FROM tweets T,users U
WHERE T.name="A(n|s)*r" 
	AND U.friends_count < 100
	AND T.user_id = U.user_id

/*Selects popular short tweets*/
SELECT tweet_text
FROM tweets
WHERE retweet_count > 200 AND LENGTH(tweet_text) < 80

/*Find the ones with max followers in each location*/
SELECT name,screen_name,MAX(followers_count)
FROM users
GROUP BY location
ORDER BY location