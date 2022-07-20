from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water","Fire"])
table.align = "c"
table.min_table_width_table_width = 10000
print(table)

