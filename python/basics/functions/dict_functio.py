from email.policy import default

album_={}
def album(artist, title=None):
    album_[artist]=title
    return album_

while True:
    start_exit=input('Enter true or False') or True
    if start_exit:
        break
    artist = input('Enter a artist: ')
    title = input('Enter a title: ')
    album(artist, title)


print(album('honey','yoyo'))
print(album('diljit','4peg'))
print(album('japreet'))


