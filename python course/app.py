# call the module 'utils.py' and use 'find_max'
from utils import find_max

numbers = [1, 3, 445, 56, 777]
print(find_max(numbers))

print(max(numbers))

# Now I'm importing a module that is inside a package (ecommerce)
import ecommerce.shipping
# or
from ecommerce import shipping
# or
from ecommerce.shipping import calc_shipping
calc_shipping()
