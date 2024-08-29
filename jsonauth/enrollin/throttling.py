from rest_framework.throttling import UserRateThrottle

class randomuser(UserRateThrottle):
    rate = '2/minute'  # 10 requests per minute
    scope = 'user'  # scope for the rate limit, can be 'user', 
    # 'anon' or 'user,anon'
    # If you want to limit the rate for a specific view, you can pass the view function
    # as the scope argument, like this: scope=view_func
    