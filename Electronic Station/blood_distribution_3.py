#!/usr/bin/env checkio --domain=py run blood-distribution-3

# Your mission is to distribute available blood of different types to patients requiring transfusions, considering each blood type's compatibility restrictions.  The blood supply is not always sufficient to meet all demands. You'll be provided with the quantities of each blood type and the needs of each patient type.  Your goal is to optimally allocate the available blood, respecting compatibility rules.  Keep in mind that there could be multiple optimal solutions, those that utilize the maximum possible amount of the available blood supply.
# 
# Compatibility Restrictions:
# 
# 
# 
# Input:The blood quantities (blood_avail) and the blood needs (blood_needs) for each blood type as dictionaries(dict)with string keys (str) and integer values (int).
# 
# Output:The output will be the distribution of blood quantities for each blood type as dictionary of dictionaries(dict)with string keys (str) and integer values (int).
# 
# Examples:
# 
# 
# distribute_blood({'A': 30, 'B': 60, 'AB': 30, 'O': 60}, {'A': 30, 'B': 40, 'AB': 50, 'O': 60}) == 
# {
#    'A': {'A': 30, 'B': 0,  'AB': 0,  'O': 0},
#    'B': {'A': 0,  'B': 40, 'AB': 20, 'O': 0},
#   'AB': {'A': 0,  'B': 0,  'AB': 30, 'O': 0},
#    'O': {'A': 0,  'B': 0,  'AB': 0, 'O': 60}
# }
# 
# distribute_blood({'A': 40, 'B': 30, 'AB': 30, 'O': 40}, {'A': 30, 'B': 35, 'AB': 45, 'O': 30}) == 
# {
#    'A': {'A': 30, 'B': 0,  'AB': 10, 'O': 0},
#    'B': {'A': 0,  'B': 30, 'AB': 0,  'O': 0},
#   'AB': {'A': 0,  'B': 0,  'AB': 30, 'O': 0},
#    'O': {'A': 0,  'B': 5,  'AB': 5,  'O': 30}
# }
# 
# 
# END_DESC

def distribute_blood(
    blood_avail: dict[str, int], blood_needs: dict[str, int]
) -> dict[str, dict[str, int]]:
    # you code here
    return {}


if __name__ == "__main__":
    assert distribute_blood(
        {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}
    ) == {
        "A": {"A": 100, "B": 0, "AB": 50, "O": 0},
        "B": {"A": 0, "B": 100, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 0, "O": 0},
        "O": {"A": 0, "B": 0, "AB": 0, "O": 0},
    }
    assert distribute_blood(
        {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
    ) == {
        "A": {"A": 10, "B": 0, "AB": 0, "O": 0},
        "B": {"A": 0, "B": 10, "AB": 0, "O": 0},
        "AB": {"A": 0, "B": 0, "AB": 20, "O": 0},
        "O": {"A": 10, "B": 0, "AB": 10, "O": 0},
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")