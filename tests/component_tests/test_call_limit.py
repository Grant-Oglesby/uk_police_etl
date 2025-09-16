from src.extract import call_limit


def test_call_limit():
    call_limit.check_rate()
    assert call_limit.CALLS == 15
    assert call_limit.RATE_LIMIT == 1


if __name__ == "__main__":
    test_call_limit()
    print("All tests passed.")
