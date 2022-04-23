import matplotlib.pyplot as plt

def get_values():
    chadDict = {}
    with open("scripts/data/values_light_project.csv", 'r', encoding="UTF-8") as csvFile:
        data = csvFile.readlines()
        del data[0:2]
        for line in data:
            wavelength, bariumNitrate, copperChloride, sodiumChloride = \
                line.replace(',', '.').strip().split(';')
            if wavelength not in chadDict.keys():
                chadDict[wavelength] = {
                    "barium_nitrate": float(bariumNitrate)*3,
                    "copper_chloride": float(copperChloride)*3,
                    "sodium_chloride": float(sodiumChloride)*3,
                    "nbr_values": 1
                }
            else:
                chadDict[wavelength]["barium_nitrate"] += float(bariumNitrate)*3
                chadDict[wavelength]["copper_chloride"] += float(copperChloride)*3
                chadDict[wavelength]["sodium_chloride"] += float(sodiumChloride)*3
                chadDict[wavelength]["nbr_values"] += 1

    for val in chadDict:
        chadDict[val]["barium_nitrate"] /= chadDict[val]["nbr_values"]
        chadDict[val]["copper_chloride"] /= chadDict[val]["nbr_values"]
        chadDict[val]["sodium_chloride"] /= chadDict[val]["nbr_values"]
        del chadDict[val]["nbr_values"]

    return chadDict


def create_graphic(data):
    wavelengthList = list(data.keys())
    bariumNitrateList = [data[item]["barium_nitrate"] for item in data]
    copperChlorideList = [data[item]["copper_chloride"] for item in data]
    sodiumChlorideList = [data[item]["sodium_chloride"] for item in data]
    
    # plt.plot(wavelengthList, copperChlorideList, c="purple", label="Intensité en luxmètres d'une flamme de Chlorure de Cuivre")
    # plt.plot(wavelengthList, bariumNitrateList, c="pink", label="Intensité en luxmètres d'une flamme de Nitrate de Barium")
    plt.plot(wavelengthList, sodiumChlorideList, c="purple", label="Intensité en luxmètres d'une flamme de Chlorure de Sodium")
    plt.title("Courbes des intensités de différentes flammes en fonction des longueurs d'onde")
    plt.legend()
    plt.xticks([len(wavelengthList)*i/8 for i in range(8)])
    plt.xlabel("Longeur d'onde en nm")
    plt.ylabel("Intensité en luxmètre")
    return plt.show()


create_graphic(get_values())
