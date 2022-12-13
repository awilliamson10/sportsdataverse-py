"""
This files contains a function "get_docs" that returns a dictionary of
documentation for all functions in the package. The dictionary is used
to generate the documentation for the package.
"""

import inspect

from sportsdataverse import mbb


def parse_docstring(doc):
    """Given the following list of strings:
    ["espn_mbb_calendar - look up the men's college basketball calendar for a given season",
      '',
      'Args:',
      'season (int): Used to define different seasons. 2002 is the earliest available season.',
      'ondays (boolean): Used to return dates for calendar ondays',
      '',
      'Returns:',
      'pd.DataFrame: Pandas dataframe containing',
      'calendar dates for the requested season.',
      '',
      'Raises:',
      'ValueError: If `season` is less than 2002.',
      '']
    {
      "name": "espn_mbb_calendar",
      "description": "look up the men's college basketball calendar for a given season",
      "args": {
        "season": "Used to define different seasons. 2002 is the earliest available season.",
        "ondays": "Used to return dates for calendar ondays"
      },
      "returns": "pd.DataFrame: Pandas dataframe containing calendar dates for the requested season.",
      "raises": "ValueError: If `season` is less than 2002."
    }
    """
    args = {}
    returns = []
    raises = {}
    for i, line in enumerate(doc):
        if line == "Args:":
            for j in range(i + 1, len(doc)):
                if doc[j] == "":
                    break
                arg = doc[j].split(":")[0].strip()
                description = doc[j].split(":")[1].strip()
                args[arg] = description
        if line == "Returns:":
            for j in range(i + 1, len(doc)):
                if doc[j] == "":
                    break
                returns.append(doc[j].strip())
        if line == "Raises:":
            for j in range(i + 1, len(doc)):
                if doc[j] == "":
                    break
                raise_ = doc[j].split(":")[0].strip()
                description = doc[j].split(":")[1].strip()
                raises[raise_] = description
    return {
        "name": doc[0].split(" - ")[0],
        "description": doc[0].split(" - ")[1],
        "args": args,
        "returns": " ".join(returns),
        "raises": raises,
    }


def get_docs():
    """get_docs - returns a dictionary of documentation for all functions in the package

    Returns:
        dict: dictionary of documentation for all functions in the package
    """
    docs = {}
    for name, obj in inspect.getmembers(mbb):
        if inspect.isfunction(obj):
            if obj.__doc__ is not None and "espn" in obj.__doc__:
                # parse the docstring and create a dictionary
                docs[name] = parse_docstring([x.strip() for x in obj.__doc__.splitlines()])
    return docs
