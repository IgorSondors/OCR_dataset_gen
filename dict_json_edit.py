import os
import json
import codecs

path_to_input = 'via_export_json.json'
path_to_output = 'output_1.json'

with codecs.open(path_to_input, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

for image_name in data:
    regions_dict = {}
    new_data = []
    j = 0
    for region in data[image_name]['regions']:
        x = str(region['shape_attributes']['x'])
        y = str(region['shape_attributes']['y'])
        width = str(region['shape_attributes']['width'])
        height = str(region['shape_attributes']['height'])

        metahash = x + y + width + height
        if not metahash in regions_dict.values():
            new_data.append(region)
            regions_dict[j] = metahash
            j += 1

    data[image_name]['regions'] = new_data

with codecs.open(path_to_output, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

