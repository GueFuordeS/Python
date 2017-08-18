def num_sum(numbers):
    nums = filter(lambda e: num_convert(e), numbers)
    nums = map(lambda e: int(e), nums)

    return sum(nums)


def num_convert(chunk):
    try:
        int(chunk)
        return True
    except ValueError:
        return False


def app(environ, start_response):
    total = num_sum(environ['PATH_INFO'][1:].split(','))
    total = str(total).encode()

    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(total)))
    ])

    return iter([total])
