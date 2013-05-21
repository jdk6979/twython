from .compat import basestring, is_py2, str


def _transparent_params(_params):
    params = {}
    files = {}
    for k, v in _params.items():
        if hasattr(v, 'read') and callable(v.read):
            files[k] = v
        elif isinstance(v, bool):
            if v:
                params[k] = 'true'
            else:
                params[k] = 'false'
        elif isinstance(v, basestring) or isinstance(v, int):
            params[k] = v
        else:
            continue
    return params, files


def _encode(value):
    if is_py2 and isinstance(value, str):
        value.encode('utf-8')
    return value
