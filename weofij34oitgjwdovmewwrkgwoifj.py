#!/usr/bin/python3

from feedgen.feed import FeedGenerator

# chat jippity code below:

def main():
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif = FeedGenerator()
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.id("http://example.com/atom_feed")
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.title("test python rrss feed?")
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.author({"name": "Moltony uwu", "email": "moltonyx@gmail.com"})
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.link(href="http://example.com/atom_feed", rel="self")
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.link(href="http://example.com")
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.subtitle("this is a python rss slash atom feed tesat !!!!!!!!!!!!!!!!")
    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.language("en") # doubtful

    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444 = weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.add_entry()
    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444.id("http://example.com/posts/1")
    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444.title("this is a post")
    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444.link(href="http://example.com/posts/1")
    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444.summary("insert suymmar yhere")
    woeifjwonroignwioenwoidewoifio0ejwioejfioqejcoiqwjcwoidjgwoiejfwoirwjgwoeijfsorirjg4444.published("2022-02-22T22:22:22Z")

    weofijwefoijewrvoijwefoijwdvoiejrfoiwjcojwoijdfoirjeoifjweoif.atom_file("Koshitantan.atom")

if __name__ == "__main__":
    main()
