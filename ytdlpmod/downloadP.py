
import subprocess
import sh

from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(10)


def run_cmd(cmd):
	print("开始执行终端命令")    
	print(cmd)    
	# p=subprocess.Popen(cmd,shell=True)
	p=subprocess.Popen([cmd])
	# p=subprocess.call(cmd,shell=True)
	# p=subprocess.run(['bash','-c',cmd])
	print(p)
	return_code=p.wait() 
	print("终端命令执行完毕")    

def run_cmds(cmds):
	print("开始执行终端命令")    
	print(cmds)    
	p=subprocess.Popen(cmds)
	# print(p)
	return_code=p.wait() 
	print("终端命令执行完毕")         

def run_shell(cmd):
	print("开始执行终端命令")    
	print(cmd)    	
	re=sh.command_name(cmd)
	# print(re)
	print("终端命令执行完毕")       


def exe_command(command):
    """
    执行 shell 命令并实时打印输出
    :param command: shell 命令
    :return: process, exitcode
    """
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    with process.stdout:
        for line in iter(process.stdout.readline, b''):
            print(line.decode().strip())
    exitcode = process.wait()
    return process, exitcode


def work(url,_type):
    print(url)
    print(_type)

    if 'bilibili.com' in url:
        # executor.submit(run_cmds,["/opt/workspace/flask/ytdlpmod/you-get-download.sh",str(url),str(_type)])
        bbdown_base="/opt/workspace/flask/ytdlpmod/BBdown"
        if "mp3" == str(_type):
            executor.submit(run_cmds,[bbdown_base+"/audio.sh",str(url)])
        else:
            executor.submit(run_cmds,[bbdown_base+"/video.sh",str(url)])
    elif 'ixigua.com' in url:
        print("ixigua.com")
        executor.submit(run_cmds,["/opt/workspace/flask/ytdlpmod/you-get-download.sh",str(url),str(_type)])
    elif 'youtube.com' in url:
        executor.submit(run_cmds,["/opt/workspace/flask/ytdlpmod/download.sh",str(url),str(_type)])
    else:
        pass

