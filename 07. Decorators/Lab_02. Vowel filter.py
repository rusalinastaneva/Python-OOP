def vowel_filter(function):
    def is_vowel(letter):
        return letter in ('a', 'e', 'o', 'u', 'i')

    def wrapper():
        result = function()
        return list(filter(is_vowel, result))

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
