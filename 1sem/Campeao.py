golsTimeA = int(input("Gols time A:"))
golsTimeb = int(input("Gols time B:"))

if golsTimeA==golsTimeb:
    print("Empate")
else:
    if golsTimeA>golsTimeb:
        print("Time A é campeao")
    else:
        print("Time B é campeao")        
print("End GAME")