counties = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]

for key, value in zip(counties, capitals):
    print(f"{key} -> {value}")

# zip = {key: value for key, value in zip(input().split(", "), input().split(", "))}
#
# for k, v in zip.items():
#     print(f"{k} -> {v}")
