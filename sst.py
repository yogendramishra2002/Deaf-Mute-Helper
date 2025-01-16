import pvleopard


leopard = pvleopard.create(access_key='lF57Y8NTRNiCaqGFNMB7q+UA9TUl7bbAiAAEOrGALAF5rPgKyIZsiA==')


transcript, words = leopard.process_file('audio.ogg')
print(transcript)
def leopard1():
    print("leopard")
    return leopard