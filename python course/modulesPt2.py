# I imported another file (module) I've created (modules.py), wich contains thes methods below
import modules

# importing like this we can directly use this function, without writing 'modules' first
from modules import kg_to_lbs

print(kg_to_lbs(90))

print(round(modules.kg_to_lbs(80)))
print(round(modules.lbs_to_kg(90)))
