#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.php', methods=['GET', 'POST'])
def index():
    def safe_filter(s):
        blacklist1 = ['{import','{getattr','{os','{class','{subclasses','{mro','{request','{args','{eval','{if','{for','{subprocess','{file','{open','{popen','{builtins','{compile','{execfile','{from_pyfile','{local','{self','{item','{getitem','{getattribute','{func_globals','{config']
        blacklist_strong = blacklist1 + ['{{', '}}']
        for no in blacklist_strong:
            if no in s:
                return '1'
            else:
                continue

        blacklist = ['import','getattr','os','class','subclasses','mro','request','args','eval','if','for',' subprocess','file','open','popen','builtins','compile','execfile','from_pyfile','local','self','item','getitem','getattribute','func_globals','config']
        for no in blacklist:
            while True:
                if no in s:
                    s =s.replace(no,'')
                else:
                    break
        return s
    if request.method == 'POST':
        name = request.form['name']
        template = 'hello {}!'.format(name)
        name1 = render_template_string(safe_filter(template))
        print name1
        if name1 == '1':
            template1 = u'''
            <strong>Parse error:</strong> syntax error, unexpected T_STRING, expecting '{' in <strong>\\var\\WWW\\html\\test.php</strong> on line <strong>13</strong>
                '''
            return render_template_string(template1)
        else:
            return render_template('index.html', name=name1)

    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
