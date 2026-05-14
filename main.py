import json


print("MEMORY AS INFRASTRUCTURE")
print("-------------------------")


with open(
    "field-observation-engine/observations.json",
    "r"
) as file:

    observations = json.load(file)


for site in observations:

    print()
    print("PLACE:", site["place"])

    harmonic_score = (
        site["rhythm"]
        + site["memory_persistence"]
        + site["commons_health"]
        - site["contradiction"]
        - site["spectacle"]
    )

    print("HARMONIC SCORE:", harmonic_score)

    if harmonic_score > 10:
        print("STATUS: stable memory system")

    else:
        print("STATUS: distortion increasing")
