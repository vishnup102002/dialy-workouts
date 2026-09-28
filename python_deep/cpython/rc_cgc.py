import gc
import sys

print("--- 1. REFERENCE COUNTING ---")
my_list = [1, 2, 3]
print("Initial ref count:", sys.getrefcount(my_list))

list_dup = my_list
print("Ref count after pointing:", sys.getrefcount(my_list))
del list_dup
print("Ref count after deleting pointing:", sys.getrefcount(my_list))

print("\n--- 2. CYCLIC GARBAGE COLLECTOR (Gen 0) ---")
class Node:
    def __init__(self, name):
        self.name = name
        print(f"-> Object '{self.name}' created in memory")
    def __del__(self):
        print(f"X Object '{self.name}' destroyed and memory freed!")

# Temporarily disable automatic GC
gc.disable()

def create_rc():
    print("Inside function: creating objects...")
    obja = Node("A")
    objb = Node("B")
    obja.partner = objb
    objb.partner = obja
    print("Cycle created! Variables obj_a and obj_b are about to go out of scope.")

create_rc()

print("\nFunction finished. Notice neither object was destroyed yet because of the cycle!")
print("GC counts (Gen 0, Gen 1, Gen 2):", gc.get_count())

print("\n--- Forcing Cyclic GC to run ---")
collect_count = gc.collect()
print(f"Cyclic GC cleaned up {collect_count} objects.")
print("GC counts after cleanup:", gc.get_count())


print("\n--- 3. DEMONSTRATING GEN 1 AND GEN 2 PROMOTIONS ---")

# Let's create a permanent list that will survive multiple cleanups
survivor_list = [Node("Survivor_1"), Node("Survivor_2")]

print("\nCounts right after creating survivors (all start in Gen 0):", gc.get_count())

# Step 1: Collect Generation 0. 
# Because survivor_list is still active, these objects survive and move to Gen 1!
print("\n--> Forcing Gen 0 collection...")
gc.collect(0) 
print("GC counts after Gen 0 collection (Notice Gen 0 count dropped, others shifted):", gc.get_count())

# Step 2: Collect Generation 1.
# Because they survived Gen 0 and are still alive, they now get promoted to Gen 2!
print("\n--> Forcing Gen 1 collection...")
gc.collect(1)
print("GC counts after Gen 1 collection (Objects promoted to Gen 2!):", gc.get_count())

# Clean up our survivor list at the very end so it doesn't leak
del survivor_list
gc.enable()
print("\nSurvivor list deleted and GC re-enabled.")