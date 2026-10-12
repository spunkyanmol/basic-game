import nava, random

play_ts = {
    1: "./audios/fahh1.wav",
    2: "./audios/laugh2.wav",
    3: "./audios/laugh1.wav"
}

rand_aud = random.randrange(1, 4)
to_play = play_ts[rand_aud]
nava.play(to_play)
