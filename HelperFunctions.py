def find_common_element(list_of_iterables: list[str]) -> list:
    # we can just use set(a) & set(b) & set(c)
    # but because someone has shown me this, so we are not going do that
    # we are ORIGINAL!!! we are hip, as the cool kids say these days

    # so list of iterables must have at least 2 iterables in the list
    # I guess we also have to catch cases for iterables with mixed type elements in the future
    # that is another day's problem
    if len(list_of_iterables) < 2:
        print("The list of iterables has to contain at least two iterables to find the common element.")
        return []

    first_group = list(dict.fromkeys(sorted(list_of_iterables.pop(0))))
    while list_of_iterables:
        common_items = list()
        second_group = list(dict.fromkeys(sorted(list_of_iterables.pop(0))))
        while first_group and second_group:
            if first_group[0] == second_group[0]:
                common_items.append(first_group[0])
                first_group.pop(0)
                second_group.pop(0)
                # if there is only one common item GUARANTEED or there is only 2 iterables to compare with
                # break
            elif first_group[0] < second_group[0]:
                first_group.pop(0)
            else:
                second_group.pop(0)

        first_group = common_items

    return first_group
