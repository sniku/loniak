import os
import json
from loniak_exceptions import ConfigurationError

def read_loniak_data_file(path):
    if not os.path.exists(path):
        raise ConfigurationError('Data file doesn\'t exist. Create {0}'.format(path))
    if not os.access(path, os.W_OK):
        raise ConfigurationError('Data file isn\'t writeable. Run "chmod +x {0}"'.format(path))
    if not os.access(path, os.R_OK):
        raise ConfigurationError('Data file isn\'t readable. Run "chmod +r {0}"'.format(path))

    raw_data = open(path, 'r').read()

    if raw_data.strip() == '':
        json_data = {}
    else:
        json_data = json.loads(raw_data)

    if 'already_downloaded' not in json_data:
        json_data['already_downloaded'] = []


    return json_data


def write_loniak_data_file(path, data):
    if not os.path.exists(path):
        raise ConfigurationError('Data file doesn\'t exist. Create {0}'.format(path))
    if not os.access(path, os.W_OK):
        raise ConfigurationError('Data file isn\'t writeable. Run "chmod +x {0}"'.format(path))
    if not os.access(path, os.R_OK):
        raise ConfigurationError('Data file isn\'t readable. Run "chmod +r {0}"'.format(path))

    with open(path, 'w') as f:
        raw_data = json.dumps(data, indent=4)
        f.write(raw_data)

