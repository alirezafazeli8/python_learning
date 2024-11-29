import sys
import requests
import hashlib


def request_api(query):
    try:
        url = f"https://api.pwnedpasswords.com/range/{query}"
        res = requests.get(url)

        if res.status_code != 200:
            raise RuntimeError(f"Fetching Error ! {res.status_code}-error")
        else:
            return res
    except:
        print("Something went wrong !")


def get_password_leaked_count(hashes, hash_to_checked):
    hash_line = (line.split(":") for line in hashes.splitlines("\n"))
    for hash, count in hash_line:
        if hash == hash_to_checked:
            return count
    return 0


def check_pwnd(password):
    hash_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_sha1, tail_sha1 = hash_password[:5], hash_password[5:]

    return get_password_leaked_count(request_api(first5_sha1).text, tail_sha1)


def main(argSys):
    if len(argSys) < 1:
        print("Pleas Enter Password To Check Hacked !")
    else:
        for password in argSys:
            count_password = check_pwnd(password)
            if count_password:
                print(
                    f"! Warning ! Your Password : ({password}) Leaked in {count_password} times. ! Change Your Password Now \n"
                )
            else:
                print(f"Yay! ({password}) Never Leaked in Pwned Database ... \n")


if __name__ == "__main__":
    main(sys.argv[1:])
