from flask import Flask
from flask import request
from ytdlpmod import downloadP
from link_keeper import link_keeper
from flask import Flask,request,current_app
from trade_web import caculator
import json
import sys
from logging.config import dictConfig
from flask_caching import Cache


config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 3600
}


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

############################################



@app.route("/link_keeper/add",methods=['POST', 'GET'])
def link_keeper_add():
    """
    新增一个链接
    """
    url = request.args.get('url', '')
    title = request.args.get('title', '')
    type = request.args.get('type', '')
    category = request.args.get('category', '')
    
    
    if title is None or "" == title:
        current_app.logger.info('查询title')
        title=link_keeper.getTitle(url)
    else:
        current_app.logger.info('自带title')

    # print("title:",title)
    # print("url:",url)
    current_app.logger.info('url:%s title:%s', url,title)

    link_keeper.add(url,title,type,category)

    result={}
    result['code']=200
    result['msg']='success'
    result['data']=None
    return json.dumps(result)


@app.route("/link_keeper/delete",methods=['POST', 'GET'])
def link_keeper_delete():
    """
    删除一个链接
    """

    id = request.args.get('id', '')
    type = request.args.get('type', '')
    link_keeper.delete(id,type)
    

    result={}
    result['code']=200
    result['msg']='success'
    result['data']=None
    return json.dumps(result)

############################################

@app.route("/youtube-dl", methods=['POST', 'GET'])
def youtube_dl():
    url = request.args.get('url', '')
    _type = request.args.get('type', '')
    downloadP.work(url,_type)
    return "下载已经开始了"

############################################

@app.route("/stocks/list",methods=['POST', 'GET'])
def tradebot_stocks_list():
    """
    罗列所有股票
    """
    result={}
    result['code']=200
    result['msg']='success'
    data=caculator.show_stocks()
    result['data']=data
    return json.dumps(result)
    # return {}


@app.route("/stocks/update",methods=['POST', 'GET'])
def tradebot_stocks_update():
    """
    更新某个股票
    """
    caculator.update_stock(request.get_data().decode("utf-8"))
    result={}
    result['code']=200
    result['msg']='success'
    return json.dumps(result)


@app.route("/stocks/remove/<stock_id>",methods=['POST', 'GET'])
def tradebot_stocks_remove(stock_id):
    """
    删除某只股票
    """
    caculator.remove_stock(stock_id)
    result={}
    result['code']=200
    result['msg']='success'
    return json.dumps(result)


@app.route("/stocks/calc/<stock_id>",methods=['POST', 'GET'])
# @cache.cached(timeout=1800)
def tradebot_stocks_calc(stock_id):
    """
    计算某只股票
    """
    result={}
    result['data']=caculator.calc_stock(stock_id)
    result['code']=200
    result['msg']='success'
    return json.dumps(result)



@app.route("/stocks/reset",methods=['POST', 'GET'])
def tradebot_stocks_reset():
    """
    重新设置股票列表
    """
    caculator.writeJson(request.get_data().decode("utf-8"))
    result={}
    result['code']=200
    result['msg']='success'
    return json.dumps(result)


@app.route("/stocks/calc-position",methods=['POST', 'GET'])
def tradebot_stocks_calc_position():
    """
    计算所有的股票的价位
    """
    result={}
    result['data']=caculator.read2calc()
    result['code']=200
    result['msg']='success'
    return json.dumps(result)


