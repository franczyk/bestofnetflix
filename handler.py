import random
import urllib
import re
import json
import random

def best_of_netflix(event, context):
    print(event)

# Download the movie list HTML page
    link = "http://collider.com/best-movies-on-netflix-streaming/"
    myfile = urllib.urlopen(link).read()
    f = open('/tmp/content.html', 'w')
    f.write(myfile)
    f.close()
    myfile = open('/tmp/content.html', 'r')


# Get the javascript line that contains the JSON table
    myline = ""
    for line in myfile:
        if re.search('var slides', line):
            myline = line

# Clean up the output to strip out javascript so that it is plain JSON
    myline = myline.replace('  var slides =', '')
    myline = myline.replace('""}];', '""}]')

    json_array = json.loads(myline)

# Random array length of json array
    x = [i for i in range(len(json_array))]
    random.shuffle(x)

# Make a complete list of movies as a single string to read
    complete_list = ""
    for item in x:
        if not re.search('Need More Recommendations', json_array[item]["title"]):
            complete_list+=json_array[item]["title"] + ", "

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The movies are ' + complete_list
            }
        }
    }

    return response

