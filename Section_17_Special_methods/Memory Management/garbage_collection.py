import gc
import ctypes
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Color shortcuts
CYBER = Fore.CYAN + Style.BRIGHT
WARNING = Fore.YELLOW + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

# Helper Functions
def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_exists(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return True
    return False

# Fancy header with ASCII Art
def cyber_header(text):
    print(Fore.BLUE + """
    ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
    ██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
    ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
    ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
    ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    """ + RESET)
    print(CYBER + f"{'=' * 40}")
    print(f"{text.center(40)}")
    print('=' * 40 + RESET)

# Print section headers
def cyber_section(title):
    print(Fore.BLUE + "\n[ CYBER-SECTION ] " + WARNING + title)

# Classes
class ParentObject:
    def __init__(self):
        self.child = ChildObject(self)
        print(f"ParentObject {id(self)} | ChildObject {id(self.child)}")

class ChildObject:
    def __init__(self, parent):
        self.parent = parent
        print(f"ParentObject {id(self.parent)} | ChildObject {id(self)}")

# Main Script
gc.disable()

cyber_header("Garbage Collection Hacker Mode 🧹💻")

cyber_section("GC Status")
print(WARNING + "[!] Garbage Collector: Disabled")

cyber_section("Creating Objects 🎉")

# Create a ParentObject instance (i.e., our 'parent_object')
parent_instance = ParentObject()  # This is effectively our 'parent_object'

# Save memory addresses
parent_id = id(parent_instance)                     # Address of parent_object
child_id = id(parent_instance.child)                 # Address of child
child_parent_id = id(parent_instance.child.parent)    # Should match parent_id

cyber_section("Saved Memory Addresses 🧠")
print(SUCCESS + f"ParentObject ID   : {parent_id}")
print(f"ChildObject ID    : {child_id}")
print(f"Child's Parent ID : {child_parent_id}")

cyber_section("GC Check (Before) 🔍")
print(f"ParentObject exists: {object_exists(parent_id)}")
print(f"ChildObject exists : {object_exists(child_id)}")

cyber_section("Reference Counts (Initial) 📊")
print(f"ParentObject RefCount: {ref_count(parent_id)}")
print(f"ChildObject RefCount : {ref_count(child_id)}")

cyber_section("Removing External Reference 🚫")
parent_instance = None  # Simulate deletion of external reference to parent_object
print(WARNING + "[!] parent_instance = None — external link removed")

cyber_section("Ref Count After Removal 📉")
print(f"ParentObject: {ref_count(parent_id)}")
print(f"ChildObject : {ref_count(child_id)}")

cyber_section("GC Check (After p = None) 🕵️")
print(f"ParentObject: {object_exists(parent_id)}")
print(f"ChildObject : {object_exists(child_id)}")

cyber_section("Running GC — Cleaning Up Cycles 🧹")
collected = gc.collect()
print(SUCCESS + f"[+] Collected {collected} objects")

cyber_section("GC Check (After GC Run) ✅")
print(f"ParentObject: {object_exists(parent_id)}")
print(f"ChildObject : {object_exists(child_id)}")

cyber_section("Final Ref Counts 🔍")
try:
    print(ERROR + "ParentObject:", ref_count(parent_id))
    print("ChildObject :", ref_count(child_id))
except:
    print(ERROR + "Reference no longer valid (freed by GC)")

cyber_header("Memory Cleanup Complete 🛡️✅")