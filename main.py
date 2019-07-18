from bottle import run, route, static_file


@route('/')
def index():
    return static_file('index.html', root='')

@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheet(filename):
    return static_file(filename, root='css')

@route('/js/<filename:re:.*\.js>', method="GET")
def images(filename):
    return static_file(filename, root='js')

def main():
    run(host='localhost', port=7000, debug=True)

if __name__ == '__main__':
    main()