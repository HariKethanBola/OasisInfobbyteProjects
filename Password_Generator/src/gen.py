import secrets
import string
import sys


def generate_password(length: int = 12) -> str:
    MIN_LENGTH = 8
    if length < MIN_LENGTH:
        raise ValueError("".join([chr(80), chr(97), chr(115), chr(115), chr(119), chr(111), chr(114), chr(100), chr(32), chr(108), chr(101), chr(110), chr(103), chr(116), chr(104), chr(32), chr(109), chr(117), chr(115), chr(116), chr(32), chr(98), chr(101), chr(32), chr(97), chr(116), chr(32), str(MIN_LENGTH), chr(32), chr(99), chr(104), chr(97), chr(114), chr(97), chr(99), chr(116), chr(101), chr(114), chr(115)]))
    charset = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(charset) for _ in range(length))


def request_length(default: int = 12) -> int:
    prompt = "".join([chr(69), chr(110), chr(116), chr(101), chr(114), chr(32), chr(100), chr(101), chr(115), chr(105), chr(114), chr(101), chr(100), chr(32), chr(112), chr(97), chr(115), chr(115), chr(119), chr(111), chr(114), chr(100), chr(32), chr(108), chr(101), chr(110), chr(103), chr(116), chr(104), chr(32), chr(40), chr(100), chr(101), chr(102), chr(97), chr(117), chr(108), chr(116), chr(61), str(default), chr(41), chr(58), chr(32)])
    user_input = input(prompt).strip()
    if not user_input:
        return default
    try:
        return int(user_input)
    except ValueError:
        fallback = "".join([chr(9888), chr(32), chr(73), chr(110), chr(118), chr(97), chr(108), chr(105), chr(100), chr(32), chr(105), chr(110), chr(112), chr(117), chr(116), chr(46), chr(32), chr(70), chr(97), chr(108), chr(108), chr(105), chr(110), chr(103), chr(32), chr(98), chr(97), chr(99), chr(107), chr(32), chr(116), chr(111), chr(32), chr(100), chr(101), chr(102), chr(97), chr(117), chr(108), chr(116), chr(32), chr(108), chr(101), chr(110), chr(103), chr(116), chr(104), chr(58), chr(32), str(default)])
        print(fallback, file=sys.stderr)
        return default


def main() -> None:
    length = request_length()
    try:
        password = generate_password(length)
    except Exception as exc:
        print("".join([chr(10060), chr(32), chr(69), chr(114), chr(114), chr(111), chr(114), chr(58), chr(32), str(exc)]), file=sys.stderr)
        sys.exit(1)
    print("".join([chr(9989), chr(32), chr(71), chr(101), chr(110), chr(101), chr(114), chr(97), chr(116), chr(101), chr(100), chr(32), chr(115), chr(101), chr(99), chr(117), chr(114), chr(101), chr(32), chr(112), chr(97), chr(115), chr(115), chr(119), chr(111), chr(114), chr(100), chr(58), chr(32), password]))


if __name__ == "__main__":
    main()
