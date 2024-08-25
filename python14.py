"""
#
# Part: Python PIP
#PIP is a package manager for Python packages, or modules if you like.
#pip --version
#pip install camelcase
#pip list
#pip uninstall camelcase
#https://pypi.org/project/pip/
"""
import camelcase
camel = camelcase.CamelCase()
txt ="hello world my friend"
print(camel.hump(txt))

#pip list
#pip install camelcase
#pip uninstall camelcase