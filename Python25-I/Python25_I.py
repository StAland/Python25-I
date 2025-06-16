def main():
    satz = "Hallo Welt Hallo"
    wort_haufigkeit(satz)
    satz2 = "Test TEst Test TeSt"
    wort_haufigkeit(satz2)
    
def wort_haufigkeit(text):
    woerter = text.split()
    haeufigkeit = {}

    for wort in woerter:
        if wort in haeufigkeit:
            haeufigkeit[wort] += 1
        else:
            haeufigkeit[wort] = 1
    return haeufigkeit


main()
