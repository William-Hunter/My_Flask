#!/bin/bash


PORT=5000

work_dir=/opt/workspace/flask

function _start(){
    cd $work_dir
    nohup /usr/local/bin/flask run --host=0.0.0.0 --port=$PORT > ./flask.log 2>&1 &
}

function _stop(){
    kill -9 `lsof -i:$PORT |awk 'NR==2{print $2}'`
}


case $1 in
    'start')
        _start
        echo "启动信号已经发出"
        ;;
    'restart')
        _stop && _start
        echo "重启信号已经发出"
        ;;
    'stop')
        _stop
        echo "关闭信号已经发出"
        ;;
    'check')
        resu=`lsof -i:$PORT`
        if [ "" == "$resu" ]; then
            _start
            echo "程序挂起，启动。。。。"
        else 
            echo '一切正常运行中'
        fi
        ;;
    *)
        echo "请输入参数"
        exit 0
esac

