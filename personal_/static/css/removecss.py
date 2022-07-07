import json

with open('Coverage-20220707T220216.json') as json_data:
    raw_code_coverage_list = json.load(json_data)
    #print(data_dict)



for raw_code_coverage in raw_code_coverage_list:

    # print(raw_code_coverage.keys())
    # dict_keys(['url', 'ranges', 'text'])
    file_name=raw_code_coverage['url']

    

    #print(raw_code_coverage['url'])

    ranges_list = raw_code_coverage['ranges']

    #print(type(ranges_list))
    #print(type(ranges_list[0]))
    #print(ranges)

    code = raw_code_coverage['text']

    code_clean = ''     
    for ranges in ranges_list:
        code_clean += code[ranges['start']:ranges['end']]

    f= open(f"new{file_name}","w+")

    f.write(code_clean)

    f.close()