#! /usr/bin/python3
import configparser

__version__ = "1.0"

def add_section_header(properties_file, header_name):
    # configparser.ConfigParser requires at least one section header in a properties file.
    # Our properties file doesn't have one, so add a header to it on the fly.
    yield '[{}]\n'.format(header_name)
    for line in properties_file:
        yield line

def read_config(configfile):
    
    config = []
    fh_config = open(configfile, encoding="utf_8")

    config = configparser.ConfigParser()
    config.read_file(add_section_header(fh_config, 'dummy_header'), source=configfile)  # add a header for
    t_config = config['dummy_header']
    config = {}
    for param in t_config:  
        config[param] = t_config[param].strip('"')
    return config
