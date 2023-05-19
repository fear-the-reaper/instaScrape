import instaloader
import utils
import requests
import db
import sentiment
import screenshot


def detect_complaint(text: str) -> bool:
    # List of complaint keywords
    complaints = ['customer service', 'response time', 'refunds']
    
    # Iterate over each complaint keyword
    for complaint in complaints:
        # Check if the complaint keyword is present in the text (case-insensitive)
        if complaint in text.lower():
            # Return True if a complaint keyword is found
            return True  
    
    # Return False if no complaint keywords are found
    return False  

def detect_cs_comment(comment: str) -> bool:
    cs_keywords = ['algorithm', 'programming', 'machine learning', 'data structures', 'coding']
    comment = comment.lower()  # Convert the comment to lowercase for case-insensitive matching
    
    for keyword in cs_keywords:
        if keyword in comment:
            return True
    
    return False

def has_replies(comment) -> bool:
    answers = comment.answers
    num_of_answers = len(list(answers))
    if num_of_answers > 0:
        return True
    return False

def get_screenshot():
    pass

def scrape_comments(post_url: str) -> dict | None:
    # Instagram username to use for authentication
    username = "notsosane_khan"
    
    try:
        # Create an Instaloader instance
        loader = instaloader.Instaloader()
        
        # Initialize an empty dictionary to hold the scraped comments
        scraped_comments = {
            "post_url": post_url, "comments": []
        }
        
        # Load session from file using the specified username
        loader.load_session_from_file(username, "session_file")
        
        
        # Extract the shortcode from the post URL
        short_code = utils.get_shortcode(post_url)
        

        # Get the Post object for the specified shortcode
        post = instaloader.Post.from_shortcode(loader.context, short_code)
        
        # Get the comments for the Post
        comments = post.get_comments()
        
        print(f"Scraping comments for post {post_url}")

        # Loop through each comment and e   xtract the username and text
        for comment in comments:
            try:
                sentiment_analysis = sentiment.analyze_sentiment(comment.text)
                is_complaint = detect_complaint(comment.text)
                is_cs_comment = detect_cs_comment(comment.text)
                # print(f"comment id: {comment.id}")
                comment_url = f"{post_url}?comment_id={comment.id}"
                print(f"comment text: {comment.text}")
                print(f"comment url: {comment_url}")
                replied = False
                replied = has_replies(comment)
                if not replied:
                    print(f"getting the ss")
                    screenshot.get_screenshot(comment.text, comment_url)
                scraped_comment = {
                    "username": comment.owner.username, 
                    "comment": comment.text,
                    "is_complaint": is_complaint,
                    "is_cs_comment": is_cs_comment,
                    "sentiment": sentiment_analysis if sentiment_analysis is not None else "-"
                }
                scraped_comments["comments"].append(scraped_comment)
            except Exception as e:
                # Handle individual comment parsing errors
                print(f"Error parsing comment: {e}")
        
        # Check if any comments were scraped
        if len(scraped_comments["comments"]) > 0:
            return scraped_comments  # Return the dictionary of scraped comments
        
        return None  # If no comments were scraped, return None
    
    except instaloader.exceptions.InstaloaderException as e:
        # Handle Instaloader-related exceptions
        print(f"Instaloader Error: {e}")
        return None
    
    except ValueError as e:
        # Handle ValueErrors
        print(f"ValueError: {e}")
        return None
    
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")
        return None
    

def generate_alert(post_url: str, username: str, comment_text: str) -> None:
    url = 'https://hooks.zapier.com/hooks/catch/2783520/34lzy4k/'
    data = {
        "post_url": post_url,
        "username": username,
        "comment_text": comment_text
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
    except requests.exceptions.HTTPError as http_error:
        print(f'HTTP error occurred: {http_error}')
    except Exception as error:
        print(f'An error occurred: {error}')

print("Running..")
scraped_comments = scrape_comments("https://www.instagram.com/p/CrTdpzkra0-/")
# if scraped_comments is not None and len(scraped_comments) > 0:
#     db_pool = db.createDbPool()
#     if db_pool is not None:
#         try:
#             conn = db_pool.getconn()
#             for comment in scraped_comments["comments"]:
#                 data_to_insert = {
#                     "post_url": scraped_comments["post_url"],
#                     **comment
#                 }
#                 utils.insert_comment(conn, data_to_insert)
#         except Exception as e:
#             pass
#     else:
#         pass