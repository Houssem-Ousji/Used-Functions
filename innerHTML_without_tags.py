def clean_data(data):
    clean_data = []
    data_lines = data.split('\n')
    for x in data_lines:
        if x.count('<') != 1 and  x != '':
            y = ''
            test = False
            while test == False:
                x = x[x.index('>')+1:]
                if len(x) == 0:
                    test = True
                elif x[0] != '<':
                    if len(y) == 0:
                        y += x[:x.index('<')]
                    else:
                        y += ' '+ x[:x.index('<')]
            clean_data.append(y)
    print(clean_data)

data = '''
<h3>Brand Overview</h3>
<p><span>Founded:</span> 2003</p>
<p><span>Founder:</span> Elon Musk / J. B. Straubel / Martin Eberhard / Marc Tarpenning / Ian Wright</p>
<p><span>Headquarters:</span> Palo Alto, California, U.S.</p>
<p><span>Official Site:</span> <a href="//www.tesla.com/" rel="noopener noreferrer" target="_blank">www.tesla.com</a></p>
<div class="overview">
<p>Tesla, Inc. (formerly Tesla Motors, Inc.), is an American electric vehicle and clean energy company based in Palo Alto, California. The company specializes in electric vehicle manufacturing, battery energy storage from home to grid-scale and, through its acquisition of SolarCity, solar panel and solar roof tile manufacturing.</p>
<p>Tesla Motors was founded in July 2003 by engineers Martin Eberhard and Marc Tarpenning. <strong>The company's name is a tribute to inventor and electrical engineer Nikola Tesla.</strong></p>
<p>Tesla Model 3 was the world's best selling EV from 2018 to 2019 and had a maximum electric range of 500 km (310 miles) according to the EPA. It’s ahead of the competition in terms of powertrain technology, infotainment technology, and semi-autonomous driving features.</p>
<p style="text-align:center">Learn More: <a href="//en.wikipedia.org/wiki/Tesla,_Inc." rel="noopener noreferrer" target="_blank">Tesla Wiki</a></p>
'''
clean_data(data)
