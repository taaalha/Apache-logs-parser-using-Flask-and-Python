import re                       #required to use regex
from collections import Counter

from flask import Flask
from flask import render_template
from flask import request 

app = Flask(__name__)

def parse(data):
    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' #this extracts the ip's from a given file. You can test it out by going to https://regex101.com/
    ips = re.findall(pattern, data)

    results = Counter(ips).most_common(10) #only returns the 10 most common ip's in the file.
    return results 


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        log = request.files['log_file'].read() #flask reads the file in bytes format. we need to convert it into utf8
        txt = str(log, 'utf8')
        result = parse(txt)
    
        ban = []
        for key, value in result:
            if value > 10:                  #if the ip count is more than 10, ban it. 
                ban.append({'ip': key, 'counts': value})
       
        return render_template('index.html', ips=ban)      
    else:
        
        return render_template('index.html', )



if __name__ == '__main__':
    app.run(debug=True)