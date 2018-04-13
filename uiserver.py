# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,redirect,url_for ,jsonify
from werkzeug.utils import secure_filename
import os

import sys   
reload(sys) 
sys.setdefaultencoding('utf8')  

app = Flask(__name__)



@app.route('/test', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        print '进入了post'
        try:
            if not request.form:
                return jsonify(error_mes['0'])
            # if 'un' in request.form and type(request.form['un']) != unicode:
            #     return jsonify(error_mes['0'])
            # username = request.values.get('un')
            # password = request.values.get('pwd')


            return jsonify({
                'ret':200,
                'data':'获取文件成功'
            })
        except Exception as e:
            print 'fail:',e
            return jsonify({
                'ret':2001,
                'data':'获取文件失败'
            })
    elif request.method == 'GET':
        print '进入了get'

        
        # return redirect(url_for('/api/upload'))
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
    # app.run(debug = True)