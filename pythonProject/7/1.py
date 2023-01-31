months = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]

seasons = ["Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi", "Talvi"]

month_number = int(input("Enter a month number (1-12): "))
month_name = months[month_number - 1]
season = seasons[month_number - 1]


print(month_name, "kuuluu vuodenaikaan: ", season)
