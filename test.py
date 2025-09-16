# import libraries for requests and limit api calls
from ratelimit import limits, sleep_and_retry

# Number of requests per time period in seconds
CALLS = 15
RATE_LIMIT = 1

base_api = 'https://data.police.uk/api/'


@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
def check_rate():
    pass


if __name__ == "__main__":
    # Check rate limit
    check_rate()
    print(f"Rate limit {CALLS}/{RATE_LIMIT} second(s)")
