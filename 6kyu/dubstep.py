def song_decoder(song):
    result = list(filter(str.strip, song.split("WUB")))

    return ' '.join(result)


song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"

print(song_decoder(song))
