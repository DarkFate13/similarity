import json

def JSON_stripper(infile):
    input_file=open(infile, 'r')
    result = list()
    json_decode=json.load(input_file)

    for i, item in enumerate(json_decode['questionList']):
        result.append(json_decode['questionList'][i]['question'])
        
    return result
    
    
if __name__ == '__main__':

    infile = 'data.json'
    
    print JSON_stripper(infile, outfile)[0]
    
    
#change function names, get, strip