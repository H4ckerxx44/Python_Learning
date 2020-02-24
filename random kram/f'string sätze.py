wortmann = ['Dennis', 'Jenni', 'Thomas', 'ehem. Monika', 'Ruth', 'Ewald']
wortmann_ages = ['20', '25', '56', '53', '82', '85']
wortmann_living_in = ['Hamm', 'Herbern', 'Hamm', 'Porta Westfalica', 'Hamm', 'Hamm']

for names, ages, location in zip(wortmann, wortmann_ages, wortmann_living_in):
    print(f'{names} ist {ages} Jahre alt und wohnt in {location}.')
