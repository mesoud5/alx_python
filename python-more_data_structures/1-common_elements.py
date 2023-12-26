def common_elements(set_1, set_2):
    return set_1 & set_2
if __name__ == "__main__":
    set_1 = { "python", "c", "javascript" }
    set_2 = { "Bash", "c", "Ruby", "Perl" }

c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
    