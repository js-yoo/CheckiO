# https://py.checkio.org/en/mission/conversion-from-camelcase/
# Difficulty : Elementary

def from_camel_case(name):

    name=name[0].lower()+name[1:]

    answer=""

    for i in range(len(name)):

        if name[i].isupper():

            a="_"+name[i].lower() 

            answer+=a

        else:

            answer+=name[i]

    return answer
    
# Example)
# from_camel_case("MyFunctionName") == "my_function_name"
# from_camel_case("IPhone") == "i_phone"
# from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
# from_camel_case("Name") == "name"
