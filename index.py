import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read('gitosis.conf')

for section in config.sections():
    print section
    for option in config.options(section):
        print " ", option, "=", config.get(section, option)
