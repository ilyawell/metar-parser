metar = "22003KT 36012KT 36018KT FAKEKT VRB05 1234XKT VRBXXKT 00000KT VRB01KT VRB08KT 22008G18KT VRB18G28KT 27020G42KT 16008KT 130V220 25005KT 200V270 11005KT 080V180 24008KT VRB02KT 19012KT 00000KT 140P99KT 12006G18KT 24016G28KT 02010KT 27080GP99KT 350V070 ///10KT 240//KT /////KT"
# checking the wind
piece = metar.split()

# TODO: VRBXXKT (not a real group) elimination
def is_wind(piece):
    n = len(piece)
    for i in range(n):
        if piece[i].endswith('KT') and (piece[i][0:5].isdigit() or piece[i][0:3] == "VRB"):
            print(piece[i])

is_wind(piece)

