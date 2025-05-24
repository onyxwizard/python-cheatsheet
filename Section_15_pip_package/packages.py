import sys,site

#sys -> Python stores all system packages here.
print(sys.prefix)

# site ->  pip to install third-party packages, Python stores these packages here.
print(site.getsitepackages())