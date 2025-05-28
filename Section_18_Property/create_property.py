from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Color shortcuts
CYBER = Fore.CYAN + Style.BRIGHT
WARNING = Fore.YELLOW + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL

def cyber_section(title):
    print(Fore.BLUE + "\n[ CYBER-SECTION ] " + WARNING + title)

# =============================
# Why Use Property in Python?
# =============================
# This script shows the evolution of a class from basic to advanced.
# It includes:
# - No validation
# - Manual validation
# - Manual getter/setter
# - property() usage (classic style)
# - @property usage (modern style)

# ASCII Art Header
header = """
    ██████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
    ██╔═══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
    ██║   ██║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
    ██║   ██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
    ╚██████╔╝██║ ╚████║   ██║   ██╔╝ ██╗
     ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
    """

print(CYBER + header)
print(CYBER + "=" * 40)
print(" PROPERTY EVOLUTION DEMO ".center(40))
print(f"by {ERROR +'@Onyxwizard'+ RESET}".center(50))
print(CYBER+ "=" * 40 + RESET)

# -----------------------------
# 1. Employee: Basic Version (No Validation)
# -----------------------------
cyber_section("🧱 Class: Employee (No Validation)")
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{SUCCESS}Name: {self.name} | Type: {type(self.name)}\n" \
               f"Age: {self.age} | Type: {type(self.age)}"

employee = Employee('AK', '26')
print(employee)
print(WARNING + "⚠️  WARNING: Anyone can assign invalid data!")

# -----------------------------
# 2. Employee1: Add Validation During Initialization
# -----------------------------
cyber_section("🔧 Class: Employee1 (Init-time Validation)")
class Employee1:
    def __init__(self, name, age):
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        try:
            check_age = int(age)
            if check_age < 0:
                raise ValueError("Age should be positive")
            return check_age
        except ValueError:
            raise ValueError(f"Invalid age value: {age}")

    def __str__(self):
        return f"{SUCCESS}Name: {self.name} | Type: {type(self.name)}\n" \
               f"Age: {self.age} | Type: {type(self.age)}"

employee1 = Employee1('AK', '1')
print(employee1)
print(WARNING + "⚠️  INFO: Only validates during __init__")

# -----------------------------
# 3. Employee2: Manual Getter/Setter
# -----------------------------
cyber_section("⚙️  Class: Employee2 (Manual Getter/Setter)")
class Employee2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Name must be string, got {type(value)}")
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        if not isinstance(value, (int, float)):
            try:
                value = int(value)
            except:
                raise TypeError(f"Age must be numeric, got {type(value)}")
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value

    def __str__(self):
        return f"{SUCCESS}Name: {self.get_name()} | Type: {type(self.get_name())}\n" \
               f"Age: {self.get_age()} | Type: {type(self.get_age())}"

employee2 = Employee2('AK', '3')
print(employee2)
print(WARNING + "⚠️  CAUTION: Direct access still possible")

# -----------------------------
# 4. Employee3: Using property() Function (Classic Style)
# -----------------------------
cyber_section("⚡  Class: Employee3 (property() Function)")
class Employee3:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Name must be string, got {type(value)}")
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        if not isinstance(value, (int, float)):
            try:
                value = int(value)
            except:
                raise TypeError(f"Age must be numeric, got {type(value)}")
        if value < 0:
            raise ValueError("Age must be positive")
        self._age = value

    def __str__(self):
        return f"{SUCCESS}Name: {self.name} | Type: {type(self.name)}\n" \
               f"Age: {self.age} | Type: {type(self.age)}"

    # Classic property assignment
    name = property(get_name, set_name)
    age = property(get_age, set_age)

try:
    employee3 = Employee3("Bob", 25)
    print(employee3)
    employee3.age = -10  # Should raise error
except Exception as e:
    print(ERROR + f"[ERROR] Validation Error: {e}")

# -----------------------------
# 5. Final Version: Using @property Decorator (Modern & Best Practice)
# -----------------------------
cyber_section("🚀  Class: Employee4 (@property)")
class Employee4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ---- Name Property ----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Name must be a string, got {type(value)}")
        self._name = value

    # ---- Age Property ----
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, (int, float)):
            try:
                value = int(value)
            except:
                raise TypeError(f"Age must be numeric, got {type(value)}")
        if value < 0:
            raise ValueError("Age must be a positive number")
        self._age = value

    def __str__(self):
        return f"{SUCCESS}Name: {self.name} | Type: {type(self.name)}\n" \
               f"Age: {self.age} | Type: {type(self.age)}"

try:
    emp = Employee4("Alice", "30")  # String → converted
    print(emp)
    emp.age = -10  # Should raise error
except Exception as e:
    print(ERROR + f"[ERROR] Validation Error: {e}")

try:
    emp.name = 123  # Not a string
except Exception as e:
    print(ERROR + f"[ERROR] Validation Error: {e}")

print(SUCCESS + "\n✅  All property versions tested successfully.")